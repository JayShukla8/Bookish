# Bookish 📚

**A smart book recommender**

An AI-powered book recommendation system leveraging **Semantic Search**, **Zero-Shot Text Classification** and **Sentiment Analysis.**

check it out [here](https://youtu.be/dL-JtwobiNw)

## Features ✨

- Get personalised book recommendations based on your query.
- Filter books based on the category of Fiction/Nonfiction.
- Filter books based on the Genre of the book.
- Get the description along with a link to google search results.

## Structure
```
Bookish/
├── .devcontainer/          # for GitHub spaces
├── .streamlit/             # for custom theme
├── chroma_db/              # vector database 
├── datasets/               # Book datasets (csv)
├── image/                  # images for readme
├── notebooks/              # steps to build the project
├── utils/                  # functions doing the work
├── stream_interface.py     # the main file
├── requirements.txt        # requirements
├── README.md               # Simple docs
└── LICENSE                 # you can contribute
```
---

## Mechanics ⚙️

### Semantic Search
- Uses an Open Source [sentence-transformer](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model for creating the vector database from the book dataset.
- Performs similarity search between your query and the books vector database.

### Zero-Shot Text Classification
- Uses an Open Source [zero-shot text classification](https://huggingface.co/facebook/bart-large-mnli) model to classify books into Fiction/Nonfiction Category.
- This way helps in filling-in the missing data from the dataset.

### Sentiment Analysis
- Uses a [sentiment analysis](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) model to classify books based on the emotional tone of the description.
- Calculates a score from 0-1 for Ekman's 6 basic emotions from the book description.

## Contribution

This project will remain open for contribution, please feel free to help.

## Acknowledgments

Thanks to Arjav for helping out with the CSS part and Dr. Jodie Burchell for being such a great instructor.


**This project is based on an OpenSource book [dataset](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata) from Huggingface.**

---
made with 🫶🏻