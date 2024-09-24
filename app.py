# we use streamlit library for making our website because it is easy to use, we can also use flask.
import streamlit as st
import pickle
import requests
import pandas as pd

import numpy as np

print(f"np======> {np.version.version}")
print(f"pd------>{pd.__version__}")


# function to fetch poster from api
def fetch_poster(movie_title):
    response = requests.get(' http://www.omdbapi.com/?t={}&apikey=7a197950'.format(movie_title))
    data = response.json()
    if data.get('Response') == 'False':
        return image_not_found

    return data.get('Poster', image_not_found)

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
with open('likeliness.pkl', 'rb') as file:
    likeness = pickle.load(file)

with open('movies.pkl', 'rb') as file:    
    movies = pickle.load(file)

# writing simple text
st.image('image_logo.png')
st.write(":orange[Project showcasing content based recommendation system by Pete Chisamba.] ")
st.write(":red[Let NLP (Natural Language Processing) recommend the next Movies for you.]")
st.divider()
title = 'Content Based Recommender System.'
main_title = f'<ul><p style="font-family:Arial; color:red; font-size: 36px; font-weight:bold";text-align: justify>{title}</p></ul>'
st.markdown(main_title, unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Which film would you like to search for? :green[(This app recommends the next closest to your preference.)]',
    movies['title'].values)

image_not_found = "https://media.istockphoto.com/id/1055079680/vector/black-linear-photo-camera-like-no-image-available.jpg?s=612x612&w=0&k=20&c=P1DebpeMIAtXj_ZbVsKVvg-duuL0v9DlrOZUvPG6UJk="

# click on Recommend button
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.text(names[0])
        st.image(posters[0], use_column_width=True)
    with col2:
        st.text(names[1])
        st.image(posters[1], use_column_width=True)
    with col3:
        st.text(names[2])
        st.image(posters[2], use_column_width=True)
    with col4:
        st.text(names[3])
        st.image(posters[3], use_column_width=True)

    st.write('---------------------')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(names[4])
        st.image(posters[4], use_column_width=True)
    with col2:
        st.text(names[5])
        st.image(posters[5], use_column_width=True)
    with col3:
        st.text(names[6])
        st.image(posters[6], use_column_width=True)
    with col4:
        st.text(names[7])
        st.image(posters[7], use_column_width=True)

#st.write('\n\n\n --------------------')
#st.write(':green[For connect with me :]')
#st.write("Linkedin Profile : [link](https://linkedin.com/in/kanti-kumar)")
#st.write("Github : [link](https://github.com/Kanti-Kumar)")


