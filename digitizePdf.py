import fitz  # PyMuPDF
import pytesseract
import re
import json
import os

def extract_elements_from_text(text):
    # Define regular expressions to match specific elements like Name, Age, Address, etc.
    procedure_pattern = r"Procedure(s)\s*(.*)"
    tariff_pattern = r"(Tariff|Charges)\s*(.*)"

    # Extract elements using regular expressions
    procedure = re.search(procedure_pattern, text, re.IGNORECASE)
    tariff = re.search(tariff_pattern, text, re.IGNORECASE)

    # Create a dictionary for the extracted elements
    extracted_elements = {
        "Procedure": procedure.group(1) if procedure else None,
        "Tariff": tariff.group(1) if tariff else None
        # Add more elements as needed
    }
    return extracted_elements
    
def perform_ocr(image_path):
    # Perform OCR on the image using Tesseract
    text = pytesseract.image_to_string(image_path)
    return text

def extract_pdf_content(pdf_file_path):
    extracted_content = {}
    pdf_document = fitz.open(pdf_file_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image_list = page.get_pixmap()
        image_path = f"temp_image_{page_num}.png"
        image_list.save(image_path)
        # Perform OCR on the extracted image
        ocr_text = perform_ocr(image_path)
        os.remove(image_path)
        elements=extract_elements_from_text(ocr_text)
        extracted_content[f"Page_{page_num+1}"]=elements

    pdf_document.close()
    return extracted_content

if __name__ == "__main__":
    pdf_path = 'Excercise 2 data_pdf_file2.pdf'
    output_json_path="output.json"
    extracted_content = extract_pdf_content(pdf_path)
    with open(output_json_path, 'w') as output_file:
        json.dump(extracted_content, output_file, indent=4)
