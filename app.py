import streamlit as st
import numpy as np
import pandas as pd 

df = pd.read_csv('book_500.csv')
doc_sim_df = pd.read_csv("similarity.csv")

book_list = df['Book'].values
description_list = df['description'].values

def book_recommender(book_title, books=book_list, descriptions=description_list, doc_sims=doc_sim_df):
    # find book id
    book_idx = np.where(books == book_title)[0][0]
    # get book similarities
    book_similarities = doc_sims.iloc[book_idx].values
    # get top 5 similar book IDs
    similar_book_idxs = np.argsort(-book_similarities)[1:6]
    # get top 5 books
    similar_books = books[similar_book_idxs]
     # get top 5 books description
    similar_description = descriptions[similar_book_idxs]
    # Create a DataFrame with game titles and descriptions
    similar_books_df = pd.DataFrame({
        'Book': similar_books,
        'Content': similar_description
    })
    # return the top 5 books
    return similar_books_df



st.title('Sistem Rekomendasi Buku 📒')
st.header('Menggunakan algoritma TF-IDF dan Cosine Similarity', divider='blue')

# user_input = st.text_input(
#     'Judul Buku', 
#     '', 
#     placeholder='Masukkan!'
# )
# user_input = user_input.lower()

#user_input = st.selectbox('Pilih Judul Buku', book_list)

user_input = st.selectbox('Judul Buku', ['Pilih Judul Buku'] + list(book_list))

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    try:
        st.session_state.output = book_recommender(user_input, book_list, description_list, doc_sim_df)
    except:
        st.session_state.output = 'Buku tidak ditemukan'
   

st.button('cari', on_click=btn_action)
st.write(st.session_state.output)
