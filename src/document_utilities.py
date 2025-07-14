from xml.dom.minidom import Document
from langchain_unstructured import UnstructuredLoader

from pathlib import Path

def find_all_pdfs(directory_path: str):
    print("\n\nFinding all pdfs\n\n")
    base_path = Path(directory_path)
    return [p for p in base_path.rglob("*") if p.suffix.lower() == ".pdf" and p.is_file()]

def load_documents(directory_path: str) -> list[Document]:
    print("\n\nLoading documents\n\n")
    file_paths = find_all_pdfs(directory_path)
    docs_local = []
    
    # Create a loader for each file and process individually
    for file_path in file_paths:
        loader_local = UnstructuredLoader(
            file_path=str(file_path),  # Pass a single file path as a string
            strategy="hi_res",
        )
        for doc in loader_local.lazy_load():
            docs_local.append(doc)
    
    return docs_local
