# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python,
Scikit-learn and Streamlit.

## 📌 Overview

This application recommends movies based on their similarity to a
selected movie.

The system analyzes movie information including:

- Genres
- Keywords
- Overview
- Cast
- Director

## 🧠 How It Works

The project follows these steps:

1. Load the TMDB movie datasets
2. Merge movie and credits information
3. Clean and preprocess the data
4. Combine movie information into tags
5. Convert text into numerical vectors using TF-IDF
6. Calculate similarity using cosine similarity
7. Recommend the top 5 similar movies

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📂 Project Structure

```text
Movie_Recommendation_System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
└── .gitignore