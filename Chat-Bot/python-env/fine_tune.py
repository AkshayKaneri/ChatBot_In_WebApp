from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_from_disk

# Load tokenized dataset
dataset = load_from_disk('./tokenized_dataset')

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define training arguments
training_args = TrainingArguments(
    output_dir="./fine_tuned_model",  # Save the model here
    num_train_epochs=3,              # Number of training epochs
    per_device_train_batch_size=2,   # Batch size per device
    save_steps=10,                   # Save the model every 10 steps
    save_total_limit=2,              # Keep only the last 2 checkpoints
    logging_dir="./logs",            # Log directory
    logging_steps=5,                 # Log every 5 steps
    report_to="none",                # Disable reporting to external tools
    bf16=True                        # Enable mixed precision (fp16)
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Train the model
trainer.train()

# Save the final fine-tuned model
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")
print("Fine-tuning complete. Model saved to ./fine_tuned_model")