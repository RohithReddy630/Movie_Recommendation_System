# 🎬 Movie Recommendation System

A **Machine Learning based Content-Based Movie Recommendation System** built using Python, Pandas, Scikit-learn, TF-IDF, Cosine Similarity and Streamlit.

The application recommends movies similar to a movie selected by the user by analyzing movie genres, keywords, overview, cast and director information.

---

## 📌 Overview

The Movie Recommendation System uses a **Content-Based Filtering** approach.

Instead of depending on user ratings, the system analyzes the characteristics and content of each movie and recommends movies that are most similar to the selected movie.

For example, when the user selects **Avatar**, the system analyzes its movie information and recommends other movies with similar content.

### 🔹 Main Features

- 🎬 Movie selection through an interactive interface
- 🤖 Machine Learning based recommendation
- 🧠 Content-Based Filtering
- 📝 Natural Language Processing
- 📊 TF-IDF Vectorization
- 📐 Cosine Similarity
- ⭐ Top 5 similar movie recommendations
- 🌐 Streamlit web application
- 📁 TMDB 5000 movie dataset

---

## 🤖 Machine Learning

This project uses **Content-Based Filtering**, a Machine Learning recommendation technique.

The system recommends movies based on the similarity between their content.

### Features Used

The following movie features are used:

- Genres
- Keywords
- Overview
- Cast
- Director

These features are combined into a single text representation called **tags**.

---

## 🧠 Machine Learning Workflow

```text
TMDB Movie Dataset
        ↓
Data Cleaning
        ↓
Merge Movie & Credits Data
        ↓
Select Important Features
        ↓
Combine Features into Tags
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Calculate Movie Similarity
        ↓
Find Top 5 Similar Movies
```

---

## 🔍 How the Machine Learning Works

### 1. Data Collection

The project uses the TMDB 5000 Movie Dataset.

The dataset contains information such as:

- Movie title
- Genres
- Keywords
- Overview
- Cast
- Crew
- Director

---

### 2. Data Preprocessing

The movie and credits datasets are loaded using Pandas.

The two datasets are merged using the movie ID.

Unnecessary columns are removed and missing values are handled.

---

### 3. Feature Engineering

Important movie information is extracted from:

- Genres
- Keywords
- Overview
- Cast
- Director

These features are combined to create a single text column called:

```text
tags
```

Example:

```text
Action Adventure Science Fiction
space alien future technology
paraplegic marine planet
Sam Worthington Zoe Saldana
James Cameron
```

---

### 4. TF-IDF Vectorization

TF-IDF stands for:

**Term Frequency-Inverse Document Frequency**

TF-IDF converts the movie text into numerical vectors.

The project uses Scikit-learn's:

```python
TfidfVectorizer()
```

This allows the computer to represent movie descriptions mathematically.

The generated TF-IDF matrix contains numerical representations of the movie tags.

Example:

```text
TF-IDF Matrix Shape:

(4803, 5000)
```

This means the system represents the movie dataset using numerical text features.

---

### 5. Cosine Similarity

After converting the movie tags into numerical vectors, **Cosine Similarity** is used to calculate how similar movies are.

The similarity value indicates how closely two movies match based on their content.

```text
0 → Very different

1 → Highly similar
```

The system calculates similarity between the selected movie and all other movies.

---

### 6. Recommendation

The similarity scores are sorted from highest to lowest.

The system then selects the **Top 5 most similar movies**.

For example:

```text
Selected Movie: Avatar

Recommendations:

1. Aliens
2. Alien
3. Moonraker
4. Alien³
5. Silent Running
```

---

# 🧠 Machine Learning Techniques Used

| Technique | Purpose |
|---|---|
| Content-Based Filtering | Recommends movies based on movie content |
| Natural Language Processing | Processes movie text information |
| Feature Engineering | Combines important movie features |
| TF-IDF | Converts text into numerical vectors |
| Cosine Similarity | Calculates similarity between movies |

---

# 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **TF-IDF**
- **Cosine Similarity**
- **Natural Language Processing**
- **Git**
- **GitHub**

---

# 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

The dataset contains approximately 5,000 movies along with movie and credits information.

### Dataset Files

```text
data/
│
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv
```

The movie dataset contains information such as:

- Title
- Genres
- Keywords
- Overview
- Popularity
- Release date
- Vote average
- Vote count

The credits dataset contains:

- Cast
- Crew
- Director information

---

# 📁 Project Structure

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
```

---

# 🚀 How to Run

## Prerequisites

Make sure you have installed:

- Python 3.x
- Git
- VS Code (optional)

---

## Step 1: Open the Project

Open the project folder in VS Code.

Make sure your terminal is inside the project directory.

Example:

```text
C:\Users\rohit\Movie_Recommendation_System\Movie_Recommendation_System
```

---

## Step 2: Create a Virtual Environment

Run:

```bash
python -m venv venv
```

---

## Step 3: Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

## Step 4: Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

This installs the required Python libraries.

---

## Step 5: Run the Application

Run:

```bash
streamlit run app.py
```

---

## Step 6: Open the Application

Streamlit will display a local URL similar to:

```text
http://localhost:8501
```

Open this URL in your browser.

---

# 🎯 How to Use

### Step 1

Open the Streamlit application.

### Step 2

Select a movie from the **Select a movie** dropdown.

### Step 3

Click:

```text
Recommend Movies
```

### Step 4

The system analyzes the selected movie.

### Step 5

The Machine Learning model calculates similarity between the selected movie and other movies.

### Step 6

The application displays the **Top 5 similar movies**.

---

# 🎬 Example

Suppose the user selects:

```text
Avatar
```

The system analyzes:

```text
Genres
+
Keywords
+
Overview
+
Cast
+
Director
```

Then:

```text
Movie Features
      ↓
Tags
      ↓
TF-IDF
      ↓
Numerical Vectors
      ↓
Cosine Similarity
      ↓
Similarity Scores
      ↓
Top 5 Recommendations
```

Example output:

```text
Recommendations for: Avatar

1. Aliens
2. Alien
3. Moonraker
4. Alien³
5. Silent Running
```

---

# 📊 Example Machine Learning Output

The system generates a TF-IDF matrix:

```text
TF-IDF Matrix Shape: (4803, 5000)
```

The similarity matrix:

```text
Similarity Matrix Shape: (4803, 4803)
```

Example recommendation output:

```text
Recommendations for: Avatar

Aliens (similarity: 0.43)
Alien (similarity: 0.36)
Moonraker (similarity: 0.35)
Alien³ (similarity: 0.35)
Silent Running (similarity: 0.32)
```

---

# 🖥️ Application Workflow

```text
User
  ↓
Select Movie
  ↓
Streamlit Application
  ↓
Movie Features
  ↓
TF-IDF Vectorization
  ↓
Cosine Similarity
  ↓
Similarity Ranking
  ↓
Top 5 Movie Recommendations
```

---

# 💡 Why Content-Based Filtering?

Content-Based Filtering is useful because recommendations can be generated using the characteristics of the movies themselves.

The system does not require a large user-rating history.

For example:

```text
Movie A
   ↓
Movie Features
   ↓
Compare with Other Movies
   ↓
Calculate Similarity
   ↓
Recommend Similar Movies
```

---

# 📈 Advantages

- Simple and easy to understand
- Does not require user-rating history
- Provides personalized recommendations based on movie content
- Uses Machine Learning and NLP techniques
- Fast recommendation after similarity calculation
- Easy to extend with additional movie features

---

# ⚠️ Limitations

- Recommendations depend on available movie information
- Cannot easily recommend movies outside the available dataset
- Does not consider individual user preferences
- Similarity depends on the selected features
- Content-based systems can sometimes recommend movies that are too similar

---

# 🔮 Future Enhancements

The project can be further improved by adding:

- 🎞️ Movie posters
- ⭐ User ratings
- 👤 Personalized user recommendations
- 🔥 Popularity-based recommendations
- 🎭 Genre filtering
- 🔎 Movie search
- 🎬 Movie trailers
- 🌐 Online deployment
- 📱 Mobile-friendly interface
- 🤖 Hybrid Recommendation System
- 🧑‍💻 User login and profiles

---

# 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Python programming
- Data preprocessing
- Pandas DataFrames
- Feature engineering
- Natural Language Processing
- TF-IDF vectorization
- Cosine similarity
- Content-Based Recommendation
- Machine Learning workflow
- Streamlit application development
- Git and GitHub version control

---

# 👨‍💻 Author

**Rohith Reddy**

Computer Science Engineering  
Artificial Intelligence & Machine Learning

---

# 📜 License

This project is created for educational and academic purposes.