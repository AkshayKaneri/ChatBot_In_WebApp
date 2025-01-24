from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the fine-tuned model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_model")
model = GPT2LMHeadModel.from_pretrained("./fine_tuned_model")

# Add the padding token if not already present
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Test prompt
prompt = "What is AI?"

# Tokenize the input prompt
inputs = tokenizer(prompt, return_tensors="pt")

# Generate a response
outputs = model.generate(
    inputs['input_ids'], 
    max_length=50, 
    num_return_sequences=1, 
    pad_token_id=tokenizer.pad_token_id
)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Prompt: {prompt}")
print(f"Response: {response}")