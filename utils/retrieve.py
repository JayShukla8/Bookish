__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd

books = pd.read_csv("datasets/books_with_emotion_scores_02.csv")
huggingface_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

books_db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=huggingface_embeddings
)

def retrieve_semantic_recs(
        query: str,
        category: str,
        genre: str,
) -> pd.DataFrame:
    recs = books_db.similarity_search(query, k=50)
    isbns_list = []
    for i in range(len(recs)):
        isbns_list += [recs[i].page_content.split()[0].strip().lstrip('"').rstrip(':')]
    if not category=="Both":
        filtered_books = books[(books["isbn10"].isin(isbns_list)) & (books['simple_categories']==category)]
    else:
        filtered_books = books[books["isbn10"].isin(isbns_list)]
    if genre=="Nonfiction":
        genre="neutral"
    if not genre=="All":
        filtered_books.sort_values(by=genre, ascending=False, inplace=True)
    return filtered_books.head(n=16)