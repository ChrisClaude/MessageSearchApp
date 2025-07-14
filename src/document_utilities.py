from langchain_unstructured import UnstructuredLoader

from pathlib import Path

def find_all_pdfs(directory_path: str):
    print("\n\nFinding all pdfs\n\n")
    base_path = Path(directory_path)
    return [p for p in base_path.rglob("*") if p.suffix.lower() == ".pdf" and p.is_file()]

def load_documents(directory_path: str):
    print("\n\nLoading documents\n\n")
    file_paths = find_all_pdfs(directory_path)
    loader_local = UnstructuredLoader(
    file_paths=file_paths,
    strategy="hi_res",
    )
    docs_local = []
    for doc in loader_local.lazy_load():
        docs_local.append(doc)
