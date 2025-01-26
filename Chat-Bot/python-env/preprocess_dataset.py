from transformers import GPT2Tokenizer
from datasets import load_dataset
# Load the dataset
model_path = "/Users/akshaykaneri/Coding/Projects/ChatBot_In_WebApp/Chat-Bot/python-env/dataset.jsonl"

dataset = load_dataset('json', data_files={'train': model_path})
print("Dataset loaded successfully:", dataset)
# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Add a padding token if not present
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Tokenize and prepare labels
def tokenize(batch):
    # Tokenize the prompt + completion as a single input sequence
    input_text = [f"{prompt} {completion}" for prompt, completion in zip(batch['prompt'], batch['completion'])]
    tokenized = tokenizer(input_text, truncation=True, padding='max_length', max_length=128)

    # Set input_ids as labels for causal language modeling
    tokenized['labels'] = tokenized['input_ids'].copy()
    return tokenized

tokenized_dataset = dataset['train'].map(tokenize, batched=True)
print("Tokenization completed:", tokenized_dataset)

print("Saving tokenized dataset...")
tokenized_dataset.save_to_disk('./tokenized_dataset')
print("Dataset tokenized and saved!")
