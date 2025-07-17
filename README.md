# RAGPROJECT

## Overview

RAGPROJECT is a Retrieval-Augmented Generation (RAG) chatbot platform built with Python and Streamlit. It enables users to upload PDF documents and interactively query their contents using advanced language models and vector search. The project leverages LangChain, ChromaDB, and Google Generative AI for document processing and retrieval.

## Features

- **PDF Upload & Parsing:** Upload PDF files and extract their content for analysis.
- **Text Chunking:** Automatic splitting of documents into manageable chunks for efficient retrieval.
- **Vector Database:** Uses ChromaDB for fast similarity search over document embeddings.
- **Conversational AI:** Query your documents using Google Generative AI models via a chat interface.
- **Streamlit UI:** Clean, interactive web interface for seamless user experience.

## Folder Structure

```
RAGPROJECT/
│
├── data/                  # Stores datasets and persistent vector DBs
│   └── technology.pdf     # Example PDF for processing
│
├── env/                  # (Optional) Python virtual environment
│
├── notebooks/            # Jupyter notebooks for experimentation
│   └── RAG.ipynb         # Main notebook (rename as needed)
│
├── src/                  # Source code modules and scripts
│   └── ragproject.py     # Main Python script for the project
│
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── ...                   # Other project files and folders
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd RAGPROJECT
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv env
   # On Unix/macOS:
   source env/bin/activate
   # On Windows:
   env\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Run the Streamlit app:**
  ```bash
  streamlit run src/ragproject.py
  ```
- **Explore Jupyter notebooks:**
  ```bash
  jupyter notebook
  ```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes

- The `data/chroma_langchain_db/` directory is ignored in version control to avoid uploading large or sensitive database files.
- All dependencies are listed in `requirements.txt`.
- For production or deployment, review and update the `.gitignore` and dependency files as needed.
