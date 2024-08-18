# vector_db_setup.py

from vector_db import VectorDB

def store_text(text):
    db = VectorDB()
    db.add_document(text)
    db.save()
