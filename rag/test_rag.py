from rag.retriever import build_vector_store, retrieve_similar_posts


print("Building vector store...")

index, data = build_vector_store()

print(f"Loaded {len(data)} posts.")
print(f"Vector dimension: {index.d}")
print()


query = "My experience learning Python and becoming a better programmer"

results = retrieve_similar_posts(
    query,
    index,
    data,
    top_k=3
)


print("QUERY:")
print(query)
print("\n" + "=" * 60)

print("RETRIEVED POSTS")
print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\n--- Result {i} ---")
    print(f"Similarity: {result['similarity']:.4f}")
    print(f"Tone: {result['tone']}")
    print(f"Language: {result['language']}")
    print(f"Engagement: {result['engagement']}")
    print(f"Tags: {result['tags']}")
    print("\nPost:")
    print(result["text"])