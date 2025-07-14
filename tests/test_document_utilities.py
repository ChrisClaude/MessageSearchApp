import os
import pytest
from src.document_utilities import find_all_pdfs

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


def test_find_all_pdfs_returns_pdfs_in_directory(sample_pdf_directory):
    
    pdfs = find_all_pdfs(str(sample_pdf_directory))
    assert len(pdfs) == 3
    assert all(pdf.suffix == ".pdf" for pdf in pdfs)