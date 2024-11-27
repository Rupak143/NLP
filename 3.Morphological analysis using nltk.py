import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# Download resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
# Sample text
text = "Cats are running faster than the dogs."
# Tokenization and POS tagging
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [(word, lemmatizer.lemmatize(word)) for word in tokens]
print("Tokens with POS tags:", pos_tags)
print("Lemmatized words:", lemmatized)
