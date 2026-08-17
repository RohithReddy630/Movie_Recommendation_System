import streamlit as st
from recommender import movies, similarity


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 35px;
}

.movie-card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.3);
    margin-bottom: 15px;
}

.rank {
    font-size: 16px;
    font-weight: bold;
    opacity: 0.7;
}

.movie-title {
    font-size: 22px;
    font-weight: bold;
}

.info-box {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.3);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Discover movies similar to your favorites using
    Machine Learning and Natural Language Processing
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# RECOMMENDATION FUNCTION
# =========================================================

def recommend(movie_title):

    movie_matches = movies[
        movies["title"] == movie_title
    ]

    if movie_matches.empty:
        return []

    movie_index = movie_matches.index[0]

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

        movie_data = movies.iloc[index]

        recommendations.append({
            "title": movie_data["title"],
            "score": score,
            "genres": movie_data["genres"],
            "director": movie_data["director"],
            "overview": movie_data["overview"]
        })

    return recommendations


# =========================================================
# PROJECT STATISTICS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🎥 Movies",
        f"{len(movies):,}"
    )

with col2:
    st.metric(
        "🧠 Recommendation Method",
        "Content-Based"
    )

with col3:
    st.metric(
        "📊 Similarity Method",
        "Cosine"
    )

st.divider()


# =========================================================
# MOVIE SELECTION
# =========================================================

st.subheader("🔎 Find Similar Movies")

movie_list = sorted(
    movies["title"].dropna().unique()
)

selected_movie = st.selectbox(
    "Choose a movie:",
    movie_list
)


# =========================================================
# SELECTED MOVIE INFORMATION
# =========================================================

selected_data = movies[
    movies["title"] == selected_movie
].iloc[0]


with st.expander("🎥 Selected Movie Information"):

    col1, col2 = st.columns([1, 2])

    with col1:

        st.write("**Movie**")
        st.write(selected_movie)

        st.write("**Director**")
        st.write(
            selected_data["director"]
            if selected_data["director"]
            else "Not available"
        )

        st.write("**Genres**")

        genres = selected_data["genres"]

        if isinstance(genres, list):
            st.write(", ".join(genres))
        else:
            st.write(genres)

    with col2:

        st.write("**Overview**")

        overview = selected_data["overview"]

        if overview:
            st.write(overview)
        else:
            st.write("Overview not available.")


# =========================================================
# RECOMMENDATION BUTTON
# =========================================================

if st.button(
    "🎯 Recommend Movies",
    use_container_width=True,
    type="primary"
):

    recommendations = recommend(selected_movie)

    if recommendations:

        st.success(
            f"Top recommendations based on **{selected_movie}**"
        )

        st.subheader("🍿 Recommended Movies")

        for i, movie in enumerate(recommendations, 1):

            score_percentage = movie["score"] * 100

            with st.container(border=True):

                col1, col2 = st.columns([3, 1])

                with col1:

                    st.markdown(
                        f"### #{i} {movie['title']}"
                    )

                    genres = movie["genres"]

                    if isinstance(genres, list):
                        genres = ", ".join(genres)

                    st.write(
                        f"🎭 **Genres:** {genres}"
                    )

                    director = movie["director"]

                    if director:
                        st.write(
                            f"🎬 **Director:** {director}"
                        )

                    overview = movie["overview"]

                    if overview:
                        st.write(
                            f"📝 {overview}"
                        )

                with col2:

                    st.metric(
                        "Similarity",
                        f"{score_percentage:.1f}%"
                    )

                    progress_value = min(
                        max(float(movie["score"]), 0.0),
                        1.0
                    )

                    st.progress(progress_value)

    else:

        st.error(
            "Unable to generate recommendations."
        )


# =========================================================
# HOW IT WORKS
# =========================================================

st.divider()

st.subheader("🧠 How It Works")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.markdown("### 1️⃣ Data")
    st.write(
        "Movie metadata is collected from the TMDB dataset."
    )

with step2:
    st.markdown("### 2️⃣ TF-IDF")
    st.write(
        "Movie information is converted into numerical vectors."
    )

with step3:
    st.markdown("### 3️⃣ Similarity")
    st.write(
        "Cosine similarity compares movies based on their vectors."
    )

with step4:
    st.markdown("### 4️⃣ Recommend")
    st.write(
        "The five most similar movies are returned."
    )


# =========================================================
# ABOUT PROJECT
# =========================================================

st.divider()

st.subheader("ℹ️ About This Project")

st.write("""
This project implements a **Content-Based Movie Recommendation
System** using Machine Learning and Natural Language Processing.

Movie genres, keywords, overview, cast and director information
are combined to create a feature representation for each movie.

**TF-IDF Vectorization** converts the textual information into
numerical vectors. **Cosine Similarity** is then used to calculate
the similarity between movies and generate recommendations.
""")


# =========================================================
# TECHNOLOGIES
# =========================================================

st.subheader("🛠️ Technologies")

st.write(
    "Python • Pandas • NumPy • Scikit-learn • "
    "TF-IDF • Cosine Similarity • Streamlit"
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎬 Movie Recommendation System | "
    "Machine Learning Project"
)