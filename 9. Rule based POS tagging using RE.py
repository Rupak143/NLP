import re

# Rule-based tagging
def rule_based_tagger(sentence):
    rules = [
        (r'.*ing$', 'VBG'),  # gerund
        (r'.*ed$', 'VBD'),  # past tense
        (r'.*es$', 'VBZ'),  # third person singular present
        (r'.*s$', 'NNS'),   # plural noun
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
        (r'.*', 'NN')       # default noun
    ]
    tokens = sentence.split()
    tags = []
    for token in tokens:
        for pattern, tag in rules:
            if re.match(pattern, token):
                tags.append((token, tag))
                break
    return tags

# Example usage
sentence = "She likes apples and oranges."
print(rule_based_tagger(sentence))
