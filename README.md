# 🎬 Movie Recommender System

A **content-based movie recommendation system** built using **Python, Machine Learning, Flask, HTML, CSS, and JavaScript**.

The application allows users to search for a movie and get the **top 5 movies recommended based on similarity in movie content**.

---

## 🚀 Features

* 🔍 Search for movies from the dataset
* 🎬 Get the top 5 similar movies
* 🤖 Content-based movie recommendation
* ⚡ Flask backend for serving recommendations
* 💻 Web-based user interface
* 📊 Uses movie genres, keywords, cast, crew, and overview
* 💾 Precomputed similarity matrix for faster recommendations

---

## 🧠 How It Works

This project uses a **content-based recommendation system**.

Information from each movie is combined into a single `tags` column containing:

* Movie overview
* Genres
* Keywords
* Top 3 cast members
* Director

The text is processed using **Porter Stemming** and converted into numerical vectors using **CountVectorizer**.

Finally, **Cosine Similarity** is used to calculate the similarity between movies.

### Recommendation Pipeline

```text
Movie Dataset
      ↓
Data Cleaning
      ↓
Create Movie Tags
      ↓
Text Preprocessing
      ↓
Porter Stemming
      ↓
CountVectorizer
      ↓
Movie Vectors
      ↓
Cosine Similarity
      ↓
Top 5 Similar Movies
```

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* CountVectorizer
* Cosine Similarity

### Backend

* Flask
* Python
* Joblib

### Frontend

* HTML
* CSS
* JavaScript

### Dataset

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

---

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── model.py
├── requirements.txt
├── .gitignore
├── .gitattributes
├── README.md
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/garvit1226/movie-recommender-system.git
```

### 2. Open the Project

```bash
cd movie-recommender-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

---

## 🔬 Recommendation Algorithm

The recommendation system uses **Cosine Similarity**.

When a user selects a movie:

1. The selected movie is located in the dataset.
2. Its similarity scores are retrieved.
3. Movies are sorted according to their similarity score.
4. The selected movie itself is excluded.
5. The top 5 most similar movies are returned.

---

## 💾 Model Files

The computationally expensive processing is performed beforehand and saved using **Joblib**.

```text
model/
├── movies.pkl
└── similarity.pkl
```

The Flask application loads these saved files instead of recalculating the similarity matrix every time the server starts.

```python
movies = joblib.load("model/movies.pkl")
similarity = joblib.load("model/similarity.pkl")
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset** and **TMDB 5000 Credits Dataset**.

The recommendation system uses information such as:

* Movie title
* Overview
* Genres
* Keywords
* Cast
* Director

---

## 🔮 Future Improvements

* 🎞️ Add movie posters and additional movie information
* 👤 Add user-based recommendations
* ⭐ Add rating-based recommendations
* 🔀 Build a hybrid recommendation system


---

## 👨‍💻 Author

**Garbhit**

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
