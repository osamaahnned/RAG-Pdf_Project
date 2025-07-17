import streamlit as st
from streamlit_chat import message
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import tempfile
import os

st.set_page_config(page_title="PDF RAG Chatbot", layout="wide")
st.title("PDF RAG Chatbot with Streamlit")

# Sidebar for API key
google_api_key = st.sidebar.text_input("Google API Key", type="password")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and google_api_key:
    # Save uploaded PDF to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_pdf_path = tmp_file.name

    # Load PDF
    loader = PyMuPDFLoader(tmp_pdf_path)
    docs = loader.load()
    texts = [doc.page_content for doc in docs]

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        add_start_index=True,
        chunk_size=600,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.create_documents(texts)

    # Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=google_api_key
    )

    # Use a temp directory for ChromaDB
    chroma_dir = tempfile.mkdtemp()
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=chroma_dir,
        collection_name="my_chunks"
    )
    retriever = db.as_retriever()

    # LLM
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        google_api_key=google_api_key
    )

    # Prompt
    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentence maximum and keep the answer concise. "
        "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("human", "{input}")],
    )
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    # Chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    st.write("## Chat with your PDF")
    user_input = st.text_input("Ask a question about the PDF:", key="input")
    send = st.button("Send")

    if send and user_input:
        with st.spinner("Thinking..."):
            result = chain.invoke({"input": user_input})
            answer = result["answer"]
            st.session_state["messages"].append((user_input, answer))

    # Display chat history
    for i, (user_msg, bot_msg) in enumerate(st.session_state["messages"]):
        message(user_msg, is_user=True, key=f"user_{i}")
        message(bot_msg, is_user=False, key=f"bot_{i}")

    # Clean up temp file
    os.remove(tmp_pdf_path)

elif not google_api_key:
    st.info("Please enter your Google API Key in the sidebar.")
elif not uploaded_file:
    st.info("Please upload a PDF to get started.") 