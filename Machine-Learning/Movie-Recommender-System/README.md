# 🎬 Movie Recommender System

A **content-based movie recommendation system** built using **Python** and **Streamlit** that suggests similar movies based on user selection. The system analyzes movie metadata and recommends titles with the highest similarity scores.

---

## 📌 Project Overview

This project recommends movies by comparing their content (such as genres, keywords, cast, and overview) using **text vectorization** and **cosine similarity**. It provides an interactive web interface where users can select a movie and instantly get recommendations.

The application is designed for:
- Learning recommender system concepts
- Demonstrating Machine Learning skills
- Portfolio and deployment showcase

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Web Framework:** Streamlit  
- **Model Persistence:** Pickle  
- **Version Control:** Git & Git LFS  
- **Dataset:** TMDB 5000 Movies Dataset  

---

## ⚙️ How It Works

1. Movie metadata is preprocessed and combined into a single text feature.
2. Text data is converted into numerical vectors using vectorization techniques.
3. **Cosine similarity** is calculated between movies.
4. When a user selects a movie, the system recommends the most similar movies.
5. Movie posters are fetched dynamically using the TMDB API.

---

## 🚀 Features

- Interactive Streamlit web interface
- Content-based recommendations
- Fast similarity search using precomputed matrices
- Movie poster integration via API
- Clean and modular code structure

---

## 📂 Project Structure
