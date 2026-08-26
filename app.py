from flask import Flask, jsonify, request, render_template
import joblib



app = Flask(__name__)

# Load our saved ML files
movies = joblib.load("model/movies.pkl")
similarity = joblib.load("model/similarity.pkl")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/movies")
def get_movies():
    return jsonify(movies["title"].tolist())

@app.route("/recommend", methods=["POST"])
def recommend_movie():

    data = request.get_json()
    movie = data["movie"]

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        recommendations.append(movies.iloc[i[0]]["title"])

    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True)