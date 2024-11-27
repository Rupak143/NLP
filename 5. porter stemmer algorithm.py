from nltk.stem import PorterStemmer

# Create a Porter Stemmer
stemmer = PorterStemmer()

# List of words
words = ["running", "flies", "happiness", "arguing", "cats"]

# Apply stemming
stems = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stems)
