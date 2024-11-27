from transformers import MarianMTModel, MarianTokenizer

# Load the translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function for translation
def translate_to_french(text):
    tokens = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Translate text
text = "Hello, how are you?"
translation = translate_to_french(text)
print("French Translation:", translation)
