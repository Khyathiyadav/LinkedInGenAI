from rag.retriever import build_vector_store, retrieve_similar_posts
from agents.generator import generate_post


print("Building RAG system...")

index, data = build_vector_store()

print(f"Loaded {len(data)} posts.\n")


# User requirements
topic = "My experience learning Python"
tone = "Professional"
audience = "Students and aspiring developers"
language = "English"
length = "Medium"


# Create retrieval query
query = f"""
Topic: {topic}
Tone: {tone}
Audience: {audience}
Language: {language}
"""


# Retrieve relevant examples
retrieved_posts = retrieve_similar_posts(
    query,
    index,
    data,
    top_k=3
)


print("Retrieved reference posts:")
for i, post in enumerate(retrieved_posts, start=1):
    print(f"{i}. {post['text'][:100]}...")


# Generate final post
print("\nGenerating post...")

post = generate_post(
    topic=topic,
    tone=tone,
    audience=audience,
    language=language,
    length=length,
    retrieved_posts=retrieved_posts
)


print("\n" + "=" * 60)
print("GENERATED LINKEDIN POST")
print("=" * 60)
print(post)