from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "Climate change is a pressing global issue that requires immediate action.",
    "Renewable energy sources, such as solar and wind power, are essential for reducing carbon emissions.",
    "Greenhouse gases, like carbon dioxide and methane, contribute to global warming.",
    "The Paris Agreement is an international treaty aimed at addressing climate change.",
    "Sustainability and environmental conservation are crucial for the future of our planet."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

query = "climate change"
query_vector = vectorizer.transform([query])

from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

ranked_docs = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
print("Document rankings:")
for idx, score in ranked_docs:
    print(f"  Doc {idx + 1} (Score: {score:.4f}): {documents[idx]}")
