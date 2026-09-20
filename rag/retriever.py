import json
import faiss
import numpy as np

from rag.embeddings import create_embeddings


DATA_PATH = "data/posts.json"


def clean_text(value):
    """Remove invalid Unicode surrogate characters."""
    if isinstance(value, str):
        return value.encode("utf-8", errors="replace").decode("utf-8")

    if isinstance(value, list):
        return [clean_text(item) for item in value]

    if isinstance(value, dict):
        return {key: clean_text(val) for key, val in value.items()}

    return value


def load_dataset():
    """Load and clean the LinkedIn post dataset."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return clean_text(data)


def build_vector_store():
    """Create FAISS index from the LinkedIn posts."""

    data = load_dataset()

    texts = [item["text"] for item in data]

    # Create embeddings
    embeddings = create_embeddings(texts)

    # FAISS index using cosine similarity.
    # Because embeddings are normalized, inner product = cosine similarity.
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)
    index.add(np.array(embeddings, dtype="float32"))

    return index, data


def retrieve_similar_posts(query, index, data, top_k=3):
    """Retrieve the most similar posts for a user query."""

    query_embedding = create_embeddings([query])

    scores, indices = index.search(
        np.array(query_embedding, dtype="float32"),
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):
        post = data[idx].copy()

        post["similarity"] = float(score)

        results.append(post)

    return results