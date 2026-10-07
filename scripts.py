import pdfplumber
import spacy


def exact_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text +=page.extract_text() + "\n"

    return text.strip()

path =  "Manish_Kumar_Thakur_Resume_03-06-2026.pdf"
print(exact_text_from_pdf(path))