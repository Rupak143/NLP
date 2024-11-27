import nltk
from nltk import word_tokenize, pos_tag
from nltk.tree import Tree

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Semantic lexicon
semantic_dict = {
    "bank": "A financial institution",
    "car dealership": "A place where cars are sold",
    "train": "A mode of transport running on tracks",
}

# Grammar for noun phrase extraction
grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}   # Determiner + adjectives (optional) + noun
"""

# Function to extract noun phrases and their meanings
def extract_noun_phrases_meanings(sentence):
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)  # POS tagging
    parser = nltk.RegexpParser(grammar)
    parse_tree = parser.parse(tagged_tokens)
    
    noun_phrases = []
    
    for subtree in parse_tree:
        if isinstance(subtree, Tree) and subtree.label() == "NP":
            phrase = " ".join(word for word, pos in subtree.leaves())
            meaning = semantic_dict.get(phrase.lower(), "Meaning not found")
            noun_phrases.append((phrase, meaning))
    
    return noun_phrases

# Input sentence
sentence = "John went to the bank and then to a car dealership."

# Run the function
output = extract_noun_phrases_meanings(sentence)

# Display results
print("Extracted Noun Phrases and Their Meanings:")
for phrase, meaning in output:
    print(f"{phrase}: {meaning}")
