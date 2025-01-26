from transformers import GPT2Tokenizer, GPT2LMHeadModel
import os
import sys

model_path = "/Users/akshaykaneri/Coding/Projects/ChatBot_In_WebApp/Chat-Bot/python-env/fine_tuned_model"

# Load the fine-tuned model and tokenizer
fine_tuned_model_path = "/Users/akshaykaneri/Coding/Projects/ChatBot_In_WebApp/Chat-Bot/python-env/fine_tuned_model"
tokenizer = GPT2Tokenizer.from_pretrained(fine_tuned_model_path)
model = GPT2LMHeadModel.from_pretrained(fine_tuned_model_path)

# Add the padding token if not already present
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Test prompt
if len(sys.argv) < 2:
    print("Please provide a prompt as a command-line argument.")
    sys.exit(1)
prompt = sys.argv[1]

# Tokenize the input prompt
inputs = tokenizer(prompt, return_tensors="pt")

# Generate a response
outputs = model.generate(
    inputs['input_ids'], 
    max_length=50, 
    num_return_sequences=1, 
    pad_token_id=tokenizer.pad_token_id,
    temperature=0.7, 
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.5 
)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(f"Prompt: {prompt}")
print(response)