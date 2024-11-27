from sentence_transformers import SentenceTransformer, util

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to evaluate coherence
def evaluate_coherence(text):
    sentences = text.split(". ")
    embeddings = model.encode(sentences, convert_to_tensor=True)
    coherence_score = util.pytorch_cos_sim(embeddings[:-1], embeddings[1:]).mean().item()
    return coherence_score

# Input text
text = "John went to the bank. He then went to the dealership. He needed a car."
score = evaluate_coherence(text)
print("Coherence Score:", round(score, 2))
