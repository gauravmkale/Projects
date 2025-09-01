import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

movies = pd.read_csv("movies.csv")  # columns: title, summary, rating, actors, country

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

embeddings = model.encode(movies['summary'].tolist(), show_progress_bar=True)
np.save("movie_embeddings.npy", embeddings)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype="float32"))
faiss.write_index(index, "faiss_index.bin")

print("✅ FAISS index built and saved.")
