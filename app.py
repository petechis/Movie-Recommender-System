# importing important python/streamlit libraries.
import streamlit as st
from streamlit.runtime.media_file_storage import MediaFileStorageError

#For API requests and web operations
import requests

#For numerical operations
import numpy as np
import pandas as pd

#For file operations
import os
import pickle

# To ignore deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# function to fetch poster from api
def fetch_poster(movie_title):
    response = requests.get(' http://www.omdbapi.com/?t={}&apikey=7a197950'.format(movie_title))
    data = response.json()
    if data.get('Response') == 'False':
        return image_not_found

    return data.get('Poster', image_not_found)

def image_aligment_colums(num):
    try:
        poster = posters[num]
        if "use_container_width" in st.image.__code__.co_varnames:
            st.image(poster, use_container_width=True)
        else:
            st.image(poster)
    except Exception as e:
        st.warning("⚠️ Image unavailable!")
        st.caption(str("It seems one image was removed from the dataset, or the API is currently unavailable."))
        #print(e)

# function for recommandations
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = likeness[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommend_movies = []
    recommended_movie_posters = []
    for i in movie_list:

        recommend_movies.append(movies.loc[i[0], 'title'])

        # fetch poster from api
        recommended_movie_posters.append(fetch_poster(movies.loc[i[0], 'title']))

    return recommend_movies,recommended_movie_posters

# reading compressed data
with open('likeliness.pkl', 'rb') as file1:
    try:
        likeness = pickle.load(file1)
    except Exception as e:
        st.error(f"Error ===========>loading likeliness.pkl: {e}")
    finally:
        file1.close()

with open('movies.pkl', 'rb') as file2:    
    try:
        movies = pickle.load(file2)
    except Exception as e:
        st.error(f"Error ===========>loading movies.pkl: {e}")
    finally:
        file2.close()
    
# writing simple text
#st.image('image_logo.png')
# Define the text with HTML and CSS
html_title = """
<p style='font-size:48px; color:red; font-family: 'Arial Rounded MT Bold';'>
<strong>Movie Recommender System.</strong>
</p>
"""
# Display the text using st.markdown
st.markdown(html_title, unsafe_allow_html=True)
st.write(":red[NLP & ML-Powered Recommendation | AI Recommendation algorithms from User Preferences.]")
st.write(":orange[Objective: Showcasing Content Based Recommendation System (Pete Chisamba).]")
st.divider()
title = 'Content-based filtering | Machine Learning.'
main_title = f'<ul><p style="font-family:Arial; color:red; font-size: 30px; font-weight:bold";text-align: center;>{title}</p></ul>'
st.markdown(main_title, unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "### Which film would you like to search for? (SELECT🎬HIER ↓)  :green[[Recommending next 8 closest films to your preference.]]",
    movies['title'].values
    )

image_not_found = "https://media.istockphoto.com/id/1055079680/vector/black-linear-photo-camera-like-no-image-available.jpg?s=612x612&w=0&k=20&c=P1DebpeMIAtXj_ZbVsKVvg-duuL0v9DlrOZUvPG6UJk="

# click on Recommend button
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.text(names[0])
        image_aligment_colums(0)        
    with col2:
        st.text(names[1])
        image_aligment_colums(1)
    with col3:
        st.text(names[2])
        image_aligment_colums(2)
    with col4:
        st.text(names[3])
        image_aligment_colums(3)

    st.write('---------------------')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(names[4])
        image_aligment_colums(4)
    with col2:
        st.text(names[5])
        image_aligment_colums(5)
    with col3:
        st.text(names[6])
        image_aligment_colums(6)
    with col4:
        st.text(names[7])
        image_aligment_colums(7)
