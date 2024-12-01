from crewai_tools import tool
from PyPDF2 import PdfReader
from fpdf import FPDF


@tool("PDF Reader")
def pdf_reader(pdf_path: str) -> str:
    """
    Reads the content of a PDF file and returns the extracted text.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        reader = PdfReader(pdf_path)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


