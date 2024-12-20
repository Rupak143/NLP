import spacy
nlp = spacy.load("en_core_web_sm")
sentences = [
    "Apple Inc. is headquartered in Cupertino, California, and its CEO, Tim Cook, often delivers keynote speeches.",
    "The Eiffel Tower in Paris, France, is a popular tourist attraction."
]

for sentence in sentences:
    doc = nlp(sentence)
    print(f"Entities in '{sentence}':")
    for ent in doc.ents:
        print(f"  - {ent.text}: {ent.label_}")
