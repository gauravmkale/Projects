from flask import Flask, request, jsonify
import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load dataset
movies = pd.read_csv("movies.csv")  # title, summary, rating, actors, country

# Load embeddings model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load FAISS index
index = faiss.read_index("faiss_index.bin")

# Pre-computed embeddings
embeddings = np.load("movie_embeddings.npy")

@app.route("/recommend", methods=["GET"])
def recommend():
    query = request.args.get("title")
    if query is None:
        return jsonify({"error": "No movie title provided"}), 400

    movie_row = movies[movies['title'].str.lower() == query.lower()]
    if movie_row.empty:
        return jsonify({"error": "Movie not found"}), 404

    movie_idx = movie_row.index[0]
    movie_vector = embeddings[movie_idx].reshape(1, -1)

    D, I = index.search(movie_vector, 6)

    results = []
    for idx in I[0][1:6]:
        movie = movies.iloc[idx]
        results.append({
            "title": movie['title'],
            "rating": movie['rating'],
            "actors": movie['actors'],
            "summary": movie['summary'],
            "country": movie['country']
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
