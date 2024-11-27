import openai

# Set your OpenAI API key
openai.api_key = "your-api-key"

# Generate text
prompt = "Write a short story about a brave cat."
response = openai.Completion.create(
    engine="text-davinci-003", prompt=prompt, max_tokens=100
)
print(response.choices[0].text.strip())
