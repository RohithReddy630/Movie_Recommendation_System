import streamlit as st
from recommender import movies, similarity


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# -------------------------------
# Custom Styling
# -------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.movie-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #444;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# Title
# -------------------------------

st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find movies similar to your favorite movie using machine learning.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------------------
# Recommendation Function
# -------------------------------

def recommend(movie_title):

    movie_index = movies[
        movies["title"] == movie_title
    ].index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores[1:6]:
        recommendations.append({
            "title": movies.iloc[index]["title"],
            "score": score
        })

    return recommendations


# -------------------------------
# Movie Selection
# -------------------------------

st.subheader("🔎 Choose a Movie")

selected_movie = st.selectbox(
    "Select a movie from the list:",
    movies["title"].values
)


# -------------------------------
# Recommendation Button
# -------------------------------

if st.button("🎯 Recommend Movies", use_container_width=True):

    recommendations = recommend(selected_movie)

    st.subheader(
        f"🍿 Movies similar to **{selected_movie}**"
    )

    for i, movie in enumerate(recommendations, 1):

        score = movie["score"] * 100

        st.markdown(
            f"""
            <div class="movie-card">
                <h3>#{i} {movie["title"]}</h3>
                <p>Similarity Score: <b>{score:.1f}%</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )


# -------------------------------
# About Section
# -------------------------------

st.divider()

st.subheader("ℹ️ About This Project")

st.write("""
This project uses a content-based recommendation approach.
Movie information such as genres, keywords, overview, cast and
director is combined into a single feature representation.

TF-IDF vectorization converts the movie descriptions into numerical
vectors, and cosine similarity is used to identify movies with similar
content.
""")

st.caption(
    "Built with Python • Pandas • Scikit-learn • Streamlit"
)