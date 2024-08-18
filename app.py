# app.py

import streamlit as st
from pdf_processing import process_pdf
from vector_db_setup import store_text
from llama_index import LLM

# Initialize Llama 3.1 model
model = LLM(model_name="llama-3.1")

def answer_question(question, db_text):
    # Query the Vector DB with the question and text
    answer = model.answer_question(question, db_text)
    return answer

def main():
    st.title("Virtual Assistant Chat Tool")
    
    # Upload PDF
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        # Process PDF and store text
        pdf_text = process_pdf(uploaded_file)
        store_text(pdf_text)
        st.success("PDF processed and stored successfully.")
    
    # Ask a question
    question = st.text_input("Ask a question:")
    if question:
        # Retrieve text from Vector DB (mocked here as `db_text`)
        db_text = "Mocked text from Vector DB"
        answer = answer_question(question, db_text)
        st.write(f"Answer: {answer}")

if __name__ == "__main__":
    main()
