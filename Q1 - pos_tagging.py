import nltk
from nltk import pos_tag, word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

texts = ["The sun is shining brightly", "I love reading interesting books"]

for text in texts:
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    print(f"POS tags for '{text}': {pos_tags}")
