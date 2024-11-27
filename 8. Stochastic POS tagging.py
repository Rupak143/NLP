from collections import defaultdict

# Training data
train_data = [
    ("Time", "NN"), ("flies", "VBZ"), ("like", "IN"),
    ("an", "DT"), ("arrow", "NN")
]

# Build a simple tag probability model
def train_model(data):
    word_tag_freq = defaultdict(lambda: defaultdict(int))
    for word, tag in data:
        word_tag_freq[word][tag] += 1
    # Convert counts to probabilities
    model = {}
    for word, tag_freq in word_tag_freq.items():
        total = sum(tag_freq.values())
        model[word] = {tag: count / total for tag, count in tag_freq.items()}
    return model

# Tagging function
def stochastic_pos_tagging(model, sentence):
    tokens = sentence.split()
    tags = []
    for token in tokens:
        if token in model:
            tags.append(max(model[token], key=model[token].get))
        else:
            tags.append("NN")  # Default tag
    return list(zip(tokens, tags))

# Example usage
model = train_model(train_data)
sentence = "Time flies like an arrow"
print(stochastic_pos_tagging(model, sentence))
