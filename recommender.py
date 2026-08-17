import pandas as pd
import ast

# ---------------------------------------
# 1. Load the datasets
# ---------------------------------------

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

print("Movies dataset:", movies.shape)
print("Credits dataset:", credits.shape)


# ---------------------------------------
# 2. Merge the two datasets
# ---------------------------------------

movies = movies.merge(
    credits,
    left_on="id",
    right_on="movie_id"
)

print("Merged dataset:", movies.shape)


# ---------------------------------------
# 3. Select the columns we need
# ---------------------------------------

movies = movies[
    [
        "id",
        "title_x",
        "genres",
        "keywords",
        "overview",
        "cast",
        "crew"
    ]
]

# Rename title_x to title
movies.rename(columns={"title_x": "title"}, inplace=True)


# ---------------------------------------
# 4. Check for missing values
# ---------------------------------------

print("\nMissing values:")
print(movies.isnull().sum())
# ---------------------------------------
# 5. Convert JSON-like columns into lists
# ---------------------------------------

def convert_to_list(text):
    if isinstance(text, str):
        return [item["name"] for item in ast.literal_eval(text)]
    return []


# ---------------------------------------
# 6. Extract director from crew
# ---------------------------------------

def get_director(text):
    if isinstance(text, str):
        crew_list = ast.literal_eval(text)

        for person in crew_list:
            if person["job"] == "Director":
                return person["name"]

    return ""


# ---------------------------------------
# 7. Apply the functions
# ---------------------------------------

movies["genres"] = movies["genres"].apply(convert_to_list)
movies["keywords"] = movies["keywords"].apply(convert_to_list)
movies["cast"] = movies["cast"].apply(convert_to_list)
movies["director"] = movies["crew"].apply(get_director)


# ---------------------------------------
# 8. Display the cleaned information
# ---------------------------------------

print("\nCleaned movie information:")
print(
    movies[
        ["title", "genres", "keywords", "cast", "director"]
    ].head(3)
)
# ---------------------------------------
# 9. Handle missing overview values
# ---------------------------------------

movies["overview"] = movies["overview"].fillna("")


# ---------------------------------------
# 10. Combine all useful information
# ---------------------------------------

movies["tags"] = (
    movies["overview"]
    + " "
    + movies["genres"].apply(lambda x: " ".join(x))
    + " "
    + movies["keywords"].apply(lambda x: " ".join(x))
    + " "
    + movies["cast"].apply(lambda x: " ".join(x[:3]))
    + " "
    + movies["director"]
)


# ---------------------------------------
# 11. Convert tags to lowercase
# ---------------------------------------

movies["tags"] = movies["tags"].str.lower()


# ---------------------------------------
# 12. Display the final tags
# ---------------------------------------

print("\nMovie tags:")
print(movies[["title", "tags"]].head(3))
# ---------------------------------------
# 13. Convert text into numerical vectors
# ---------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["tags"])

print("\nTF-IDF matrix shape:")
print(tfidf_matrix.shape)
# ---------------------------------------
# 13. TF-IDF Vectorization
# ---------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["tags"])

print("\nTF-IDF matrix shape:")
print(tfidf_matrix.shape)


# ---------------------------------------
# 14. Calculate Cosine Similarity
# ---------------------------------------

similarity = cosine_similarity(tfidf_matrix)

print("\nSimilarity matrix shape:")
print(similarity.shape)


# ---------------------------------------
# 15. Create recommendation function
# ---------------------------------------

def recommend(movie_title):

    movie_title = movie_title.lower()

    matches = movies[
        movies["title"].str.lower() == movie_title
    ]

    if matches.empty:
        print("\nMovie not found.")
        return

    movie_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\nRecommendations for: {movies.iloc[movie_index]['title']}")

    for index, score in similarity_scores[1:6]:
        print(
            f"{movies.iloc[index]['title']} "
            f"(similarity: {score:.2f})"
        )


# ---------------------------------------
# 16. Test the recommendation system
# ---------------------------------------

recommend("Avatar")