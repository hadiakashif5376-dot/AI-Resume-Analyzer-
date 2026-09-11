from io import BytesIO
from pathlib import Path
from pypdf import PdfReader
from docx import Document

ALLOWED_EXTENSIONS = {".pdf", ".docx"}


def validate_resume(uploaded_file):
    extension = Path(uploaded_file.name).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Only PDF and DOCX resumes are supported.")


def extract_resume_text(uploaded_file):
    validate_resume(uploaded_file)
    extension = Path(uploaded_file.name).suffix.lower()
    data = uploaded_file.getvalue()

    if extension == ".pdf":
        return _extract_pdf(data)
    return _extract_docx(data)


def _extract_pdf(data):
    reader = PdfReader(BytesIO(data))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages).strip()


def _extract_docx(data):
    document = Document(BytesIO(data))
    paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip()]
    return "\n".join(paragraphs).strip()
