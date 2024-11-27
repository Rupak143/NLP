from transformers import pipeline

# Load dialog act classifier pipeline
classifier = pipeline("text-classification", model="bhadresh-savani/dialog-acts-classification")

# Input dialog
dialog = [
    "Hi, can you help me check my account balance?",
    "Sure, please provide your account number.",
    "It's 12345.",
    "Your balance is $1000.",
]

# Predict dialog acts
results = [(utterance, classifier(utterance)[0]["label"]) for utterance in dialog]
for utterance, act in results:
    print(f"{utterance}: {act}")
