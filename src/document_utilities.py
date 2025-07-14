from langchain_unstructured import UnstructuredLoader

from pathlib import Path

def find_all_pdfs(directory_path: str):
    print("Finding all pdfs\n\n")
    base_path = Path(directory_path)
    return list(base_path.rglob("*.pdf"))

def load_documents(directory_path: str):
    print("Loading documents\n\n")
    file_paths = find_all_pdfs(directory_path)
    loader_local = UnstructuredLoader(
    file_paths=file_paths,
    strategy="hi_res",
    )
    docs_local = []
    for doc in loader_local.lazy_load():
        docs_local.append(doc)
