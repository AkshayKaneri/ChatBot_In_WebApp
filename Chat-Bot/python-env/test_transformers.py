from transformers import pipeline

# Load a pre-trained text-generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
output = generator("Hello, how are you?", max_length=50, num_return_sequences=1)

print(output)