import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from transformers import pipeline

def summarize_product():
    llm = pipeline("text-generation", model="gpt2")
    result = llm("Summarize this product: Laptop Pro X, high-end performance.")
    print(result[0]["generated_text"])  # Print only the generated text

if __name__ == "__main__":
    summarize_product()
