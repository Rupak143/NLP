import re
# Transformation-based tagging
def transformation_based_tagger(sentence):
    # Initial tagging (default NN for simplicity)
    tokens = sentence.split()
    tags = [(token, "NN") for token in tokens]

    # Transformation rules
    transformations = [
        (r'^The$', 'DT'),   # 'The' -> Determiner
        (r'^is$', 'VBZ'),   # 'is' -> Verb
        (r'^a$', 'DT'),     # 'a' -> Determiner
        (r'^great$', 'JJ')  # 'great' -> Adjective
    ]

    for i, (token, tag) in enumerate(tags):
        for pattern, new_tag in transformations:
            if re.match(pattern, token):
                tags[i] = (token, new_tag)
                break
    return tags

# Example usage
sentence = "The cat is a great pet."
print(transformation_based_tagger(sentence))
