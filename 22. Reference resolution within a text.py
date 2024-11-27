from allennlp.predictors.predictor import Predictor

# Load AllenNLP coreference model
predictor = Predictor.from_path(
    "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz"
)

# Function for reference resolution
def resolve_references(text):
    result = predictor.predict(document=text)
    resolved_text = text
    for cluster in result["clusters"]:
        main_reference = result["document"][cluster[0][0]:cluster[0][1] + 1]
        for mention in cluster[1:]:
            mention_text = result["document"][mention[0]:mention[1] + 1]
            resolved_text = resolved_text.replace(" ".join(mention_text), " ".join(main_reference))
    return resolved_text

# Input text
text = "John went to the bank. He then went to the car dealership."
resolved = resolve_references(text)
print("Resolved Text:", resolved)
