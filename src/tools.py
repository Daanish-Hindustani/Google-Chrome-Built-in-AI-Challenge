from crewai_tools import tool
from PyPDF2 import PdfReader

@tool("PDF Reader")
def pdf_reader(pdf_path: str) -> str:
    """Takes in a pdf_path and reads the content then returns the text"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

