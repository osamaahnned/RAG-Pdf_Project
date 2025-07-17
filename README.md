# RAGPROJECT

## Project Overview

This project is focused on Retrieval-Augmented Generation (RAG) using Python, with support for Jupyter notebooks and persistent data storage. It includes modular scripts, a dedicated notebooks directory, and a data directory for storing embeddings and resources.

## Folder Structure

```
RAGPROJECT/
│
├── data/                  # Stores datasets and persistent vector DBs
│   ├── chroma_langchain_db/   # Chroma vector database files
│   │   └── 130c4f94-7688-46f6-b020-02e89289e1cf/  # Internal DB files
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
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── ...                   # Other project files and folders
```

## Setup Instructions

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
   (Add a `requirements.txt` file if not present, or install as needed)
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the main script:
  ```bash
  python src/ragproject.py
  ```
- Explore or run the Jupyter notebooks for experimentation:
  ```bash
  jupyter notebook
  ```

## Notes

- The `data/chroma_langchain_db` directory contains files for a Chroma vector database, likely used for storing embeddings.
- The `notebooks/` directory contains all Jupyter notebooks for the project.
- The `src/` directory contains all main Python scripts and modules.
- The `data/technology.pdf` file is an example PDF for processing.

## Suggestions for Further Organization

- Add a `requirements.txt` file listing all dependencies.
- Use the `src/` directory for all new scripts and modules.
- Keep the root directory clean by storing all resources and code in their respective folders.
