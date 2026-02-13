
# 🎬 AI-Powered Movie Recommendation System  

### *Content-Based Filtering with Python, NLP & Streamlit*

[English](readme.md) | [Deutsch](../DE/readme.md)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Content--Based-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Cosine%20Similarity-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![API](https://img.shields.io/badge/API-OMDb-lightgrey)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)

---

## 🇬🇧 English

## 🧠 **Project Overview**

This project implements a **content-based movie recommendation system** that suggests movies to users based on **semantic similarity of movie metadata**.  
It is designed as a **developer-centric, technically transparent application** showcasing applied **Machine Learning, NLP, and API integration**.

The system is built with **Python**, **Scikit-learn**, and **Streamlit**, and integrates real-time movie metadata via the **OMDb API**.

---

## 🎯 **Purpose & Motivation**

- Demonstrate **applied ML engineering skills**
- Implement **content-based filtering** at scale
- Bridge **model training → inference → UI**
- Serve as a **blueprint for recommendation systems** in:
  - E-commerce
  - Streaming platforms
  - Automotive sales
  - Digital content personalization

---

## 🧩 **What Is a Movie Recommendation System?**

A movie recommendation system is a **decision-support algorithm** that suggests items by analyzing:

- User preferences
- Item attributes
- Similarity patterns in high-dimensional feature spaces

This project focuses on **content-based filtering**, avoiding cold-start dependency on other users.

---

## ⚙️ **How It Works (Technical Flow)**

### 🧮 **Algorithm: Content-Based / Item-Item Filtering**

1. **Feature Engineering**
   - Movie metadata transformed into vectors (genres, keywords, overview)
2. **Vectorization**
   - NLP techniques (e.g. TF-IDF)
3. **Similarity Computation**
   - Cosine similarity matrix
4. **Inference**
   - Top-N most similar movies retrieved
5. **Presentation**
   - Results rendered dynamically in Streamlit

---

## 🗂️ **Data Pipeline**

```text
Raw Movie Metadata
        ↓
Feature Extraction (NLP)
        ↓
Vector Space Model
        ↓
Cosine Similarity Matrix (.pkl)
        ↓
Real-Time Inference (Streamlit)
````

---

## 🔑 **Vital Variables & Artifacts**

- **movies.pkl** → Movie metadata DataFrame
- **likeness.pkl** → Precomputed similarity matrix
- **movie_index** → Lookup index for inference
- **distances** → Cosine similarity vector
- **recommend_movies** → Top-N predictions

---

## 🧪 **Model Evaluation**

Although content-based systems are often qualitative, evaluation can include:

- **RMSE** (Root Mean Square Error)
- **MAPE** (Mean Absolute Percentage Error)
- Manual relevance inspection
- Offline A/B comparison (future work)

---

## 🧰 **Tech Stack**

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Streamlit**
- **OMDb REST API**
- **Pickle (model persistence)**

---

## 📦 **requirements.txt**

```txt
requests
pandas==1.4.2
numpy==1.26.4
scikit-learn>=1.3.0
streamlit>=1.30.0
```

### 🔁 **Alternatives**

* `fastapi` (API-first architecture)
* `sentence-transformers` (semantic embeddings)
* `faiss` (approximate nearest neighbors)

---

## 🌐 **Movie Data Source**

### 🎥 OMDb API – The Open Movie Database

* RESTful movie metadata service
* Posters, titles, genres, descriptions
* Poster API available for patrons

```http
http://www.omdbapi.com/?t={MOVIE_TITLE}&apikey={YOUR_KEY}
```

---

## 🧩 **Key Code Snippet (Inference Logic)**

```python
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = likeness[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:9]

    recommend_movies = []
    recommended_movie_posters = []

    for i in movie_list:
        recommend_movies.append(movies.loc[i[0], 'title'])
        recommended_movie_posters.append(fetch_poster(movies.loc[i[0], 'title']))

    return recommend_movies, recommended_movie_posters
```

---

## 🧭 **How to Navigate the App**

1. Select a movie from the dropdown
2. Click **Recommend**
3. View top-N similar movies
4. Posters loaded dynamically via API

---

## 🎥 **App Demonstration**

```md
![Movie Recommendation Demo](assets/movie_recommender_demo.gif)
```

*Demonstrates real-time inference, UI interaction, and API calls.*

---

## 🎁 **Gains for App Users**

- Personalized movie discovery
- Reduced search friction
- Explainable recommendations
- Real-time interaction

---

## 🧠 **Developer Takeaways**

- End-to-end ML lifecycle implementation
- NLP-driven similarity modeling
- Model persistence & fast inference
- Clean UI-ML separation
- API-driven enrichment

---

## 🧪 **Use Case Utility**

- Streaming platforms (Netflix-like)
- E-commerce recommendation engines
- Automotive product matching
- Content personalization systems
- Research & ML prototyping

---