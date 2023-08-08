# llm_model.py
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    # tokenizer = "TMP"
    # model = "ttt"
    return tokenizer, model

def generate_text(tokenizer, model, prompt_text, max_lenght = 50):
    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    # string1 = "hello_world"
    return generated_text
    # return string1
