import os
from pathlib import Path
import pytest
from src.document_utilities import find_all_pdfs, load_documents

@pytest.fixture
def sample_pdf_directory(tmp_path):
    """Create a temporary directory with sample PDF files."""
    d = tmp_path / "sample_pdfs"
    d.mkdir()
    (d / "doc1.pdf").touch()
    (d / "doc2.pdf").touch()
    (d / "subfolder").mkdir()
    (d / "subfolder" / "nested.pdf").touch()
    return d


# region find_all_pdfs tests
def test_find_all_pdfs_returns_pdfs_in_directory(sample_pdf_directory):
    pdfs = find_all_pdfs(str(sample_pdf_directory))
    assert len(pdfs) == 3
    assert all(pdf.suffix == ".pdf" for pdf in pdfs)
    
    
def test_find_all_pdfs_empty_directory(tmp_path):
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    
    pdfs = find_all_pdfs(str(empty_dir))
    assert pdfs == []
    
# This test depends on the data folder being in the correct place with the correct count of pdfs
def test_find_all_pdfs_in_data_folder():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    pdfs = find_all_pdfs(str(data_dir))

    assert len(pdfs) == 9
    assert all(p.suffix == ".pdf" for p in pdfs)
    
    
def test_find_all_pdfs_nested_structure(tmp_path):
    root = tmp_path / "root"
    nested = root / "nested"
    nested.mkdir(parents=True)
    (nested / "nested_doc.pdf").touch()
    (root / "root_doc.pdf").touch()

    pdfs = find_all_pdfs(str(root))
    assert len(pdfs) == 2
    assert any("nested_doc.pdf" in str(p) for p in pdfs)
    assert any("root_doc.pdf" in str(p) for p in pdfs)
    
    
def test_find_all_pdfs_ignores_non_pdf_files(tmp_path):
    (tmp_path / "file.txt").touch()
    (tmp_path / "image.png").touch()
    (tmp_path / "doc.pdf").touch()

    pdfs = find_all_pdfs(str(tmp_path))
    assert len(pdfs) == 1
    assert pdfs[0].name == "doc.pdf"
      
        
def test_find_all_pdfs_uppercase_extension(tmp_path):
    (tmp_path / "upper.PDF").touch()
    pdfs = find_all_pdfs(str(tmp_path))
    assert len(pdfs) == 1
    
# endregion find_all_pdfs tests

# region load_documents tests
# This test depends on the data folder being in the correct place with the correct count of pdfs
def test_load_documents_in_data_folder():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    docs = load_documents(str(data_dir))

    assert len(docs) > 10
    
def test_load_documents_excludes_files():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    docs = load_documents(str(data_dir), exclude=["65-0124 Birth Pains VGR.pdf"])

    assert len(docs) == 0
# endregion load_documents tests