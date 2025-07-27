import streamlit as st
from utils.retrieve import retrieve_semantic_recs
from utils.display import display_books
import re

st.markdown(f"""
    <style>
    .st-emotion-cache-9fqyt2 {{
        font-family: "Source Sans", sans-serif;
        font-size: 1rem;
        margin-bottom: 0rem;
        color: inherit;
    }}
    .reportview-container {{
        background: url("https://images.unsplash.com/photo-1605647601778-865aeff15565?q=80&w=1930&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    }}
    </style>
    """, unsafe_allow_html=True
)

st.write("""
# Bookish,
### a smart book recommender 📚
---
""")
query = st.text_input("What type of book would you like to read?")

col1, col2 = st.columns(2)

category = col1.selectbox(
    "Fiction/Nonfiction",
    ("Both", "Fiction", "Nonfiction"),
    index=0,
    placeholder="Fiction/NonFiction/Both"
)

tone = col2.selectbox(
    "Genre",
    ("All", "Adventure", "Comedy", "Horror", "Romance", "Thriller", "Nonfiction"),
    index=0,
    placeholder="😂😠😱😯😭"
)

# st.image("static/cover-not-found.jpg")
#
cols = st.columns(4)

if st.button("Go", type="primary"):
    if query:
        with st.spinner("Browsing the stacks..."):
            recs = retrieve_semantic_recs(query,category,tone)
            results = display_books(recs)
            for i, (img_url, caption, desc) in enumerate(results):
                with cols[i % 4]:  # Rotate through 3 columns
                    # st.markdown(
                    #     f'<img src="{img_url}" style="height:200px; width:auto;">',
                    #     unsafe_allow_html=True
                    # )
                    # st.image(img_url, use_container_width=True)
                    # st.markdown(caption, unsafe_allow_html=True)
                    st.markdown(f"""
                                    <style>
                                    .st-emotion-cache-1w723zb {{
                                        width: 100%;
                                        padding: 6rem 1rem 10rem;
                                        max-width: 900px;
                                    }}
                                    .book-card{{
                                        border: 0px solid rgb(204, 204, 204); 
                                        border-radius: 10px; 
                                        padding: 2px; 
                                        margin: 5px; 
                                        margin-bottom: 1.5rem; 
                                        text-align: center;
                                    }}
                                    .book-img{{
                                        height:auto;
                                        width:auto;
                                        border-radius:6px;
                                    }}
                                    .flip-container {{
                                      width: 100%;
                                      height: 420px;
                                      perspective: 1000px;
                                    }}
                                    .flipper {{
                                      width: 100%;
                                      height: 100%;
                                      transition: transform 0.6s;
                                      transform-style: preserve-3d;
                                      position: relative;
                                    }}
                                    .flip-container:hover .flipper {{
                                      transform: rotateY(180deg);
                                    }}
                                    .front, .back {{
                                      position: absolute;
                                      width: 100%;
                                      height: 100%;
                                      backface-visibility: hidden;
                                      -webkit-backface-visibility: hidden;
                                      border-radius: 12px;
                                      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                                      background-color: #f2f4ef;
                                    }}
                                    .front {{
                                      z-index: 2;
                                      display: flex;
                                      flex-direction: column;
                                      align-items: center;
                                      padding: 6px;
                                    }}
                                    .front img {{
                                      width: 100%;
                                      height: 70%;
                                      object-fit: cover;
                                      border-radius: 8px;
                                    }}
                                    .front h2 {{
                                      margin-top: 4px;
                                      font-size: 18px;
                                      text-align: center;
                                    }}
                                    .back {{
                                      transform: rotateY(180deg);
                                      padding: 4px;
                                      background-color: #eee7d7;
                                      max-height: 100%; 
                                      overflow-y: auto; 
                                      border-radius: 6px;
                                    }}
                                    .back p {{
                                      font-size: 14px;
                                      color: #333;
                                      text-align: center;
                                    }}
                                    .book-btn{{
                                        background-color: #4CAF50; /* Soft green */
                                        color: white;
                                        padding: 8px 16px;
                                        border: none;
                                        border-radius: 6px;
                                        cursor: pointer;
                                        font-size: 14px;
                                        transition: background-color 0.3s ease;
                                        margin-top:5px;
                                    }}
                                    .book-btn:hover{{
                                        background-color: #45a049; /* Darker green on hover */
                                    }}
                                    </style>
                                    <div class="book-card">
                                        <div class="flip-container">
                                            <div class="flipper">
                                              <!-- Front Side -->
                                              <div class="front">
                                                <img src="{img_url}" class="book-img"><br>
                                                <div style="margin-top:4px;">{caption}</div>
                                              </div>
                                              <!-- Back Side -->
                                              <div class="back">
                                                <p style="margin: 15px; padding-top:10px; padding-bottom:10px ">
                                                    {desc}<br>
                                                    <a href="https://www.google.com/search?q={re.sub('<[^<]+?>', '', caption)}", target="_blank">
                                                        <button class="book-btn">Go</button>
                                                    </a>
                                                </p>
                                              </div>
                                            </div>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
        # st.dataframe(recs, hide_index=True)
    else:
        st.error("Please enter your query")

