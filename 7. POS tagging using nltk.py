import nltk
from nltk import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# POS tagging with NLTK
def pos_tagging(text):
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    return tags

# Example usage
text = "Time flies like an arrow."
print(pos_tagging(text))
