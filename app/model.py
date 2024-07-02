from transformers import pipeline
import re

# Load the model and tokenizer
model = pipeline('text-generation', model='gpt2')

def generate_quote(problem):
    # Provide a more structured and specific prompt to guide the model
    prompt = (
        f"Problem: {problem}\n"
        "Give a philosophical quote addressing this problem:\n"
    )
    response = model(prompt, max_length=200, num_return_sequences=1, pad_token_id=50256)
    quote = response[0]['generated_text']
    
    # Remove the prompt part from the generated text
    if "Give a philosophical quote addressing this problem:" in quote:
        quote = quote.split("Give a philosophical quote addressing this problem:")[1].strip()

    # Post-process the quote to remove any incomplete sentences and unwanted text
    quote = re.split(r'\.|\n', quote)[0].strip() + '.'

    # Ensure the quote is meaningful and not just a random statement
    if len(quote.split()) < 5:  # Check if the quote is too short to be meaningful
        return "No suitable quote found, please try again with a different problem."
    
    return quote
