# pdf_processing.py

from llama_index import LLM


def process_pdf(pdf_path):
    # Initialize Llama 3.1 model
    model = LLM(model_name="llama-3.1")

    # Read PDF and extract text
    with open(pdf_path, 'rb') as file:
        pdf_text = model.extract_text(file)

    return pdf_text
