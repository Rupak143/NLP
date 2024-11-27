import random
from collections import defaultdict
# Build bigram model
def build_bigram_model(corpus):
    bigram_model = defaultdict(lambda: defaultdict(int))
    tokens = corpus.split()
    for i in range(len(tokens) - 1):
        bigram_model[tokens[i]][tokens[i + 1]] += 1
    return bigram_model
# Convert counts to probabilities
def calculate_probabilities(bigram_model):
    for word, next_words in bigram_model.items():
        total = sum(next_words.values())
        for next_word in next_words:
            bigram_model[word][next_word] /= total
    return bigram_model
# Generate text using the bigram model
def generate_text(bigram_model, start_word, num_words=10):
    text = [start_word]
    current_word = start_word
    for _ in range(num_words - 1):
        next_word_candidates = bigram_model[current_word]
        if not next_word_candidates:
            break
        current_word = random.choices(
            list(next_word_candidates.keys()),
            weights=list(next_word_candidates.values())
        )[0]
        text.append(current_word)
    return " ".join(text)
# Example usage
corpus = "The cat sat on the mat. The cat saw a rat. The rat sat on the mat."
bigram_model = build_bigram_model(corpus)
bigram_model = calculate_probabilities(bigram_model)
print(generate_text(bigram_model, "The", num_words=10))
