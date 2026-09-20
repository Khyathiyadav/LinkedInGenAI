from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():
    """Load the sentence-transformer embedding model."""
    return SentenceTransformer(MODEL_NAME)


def create_embeddings(texts):
    """Convert a list of texts into embedding vectors."""
    model = load_embedding_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings