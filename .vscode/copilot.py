from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Pretrained model and tokenizer를 불러오기
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 코드 생성 함수 정의
def generate_code(prompt, max_length=50, num_return_sequences=1):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output_sequences = model.generate(
        input_ids=input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        temperature=0.8,
    )

    generated_sequences = []
    for generated_sequence_id in output_sequences:
        generated_sequence = tokenizer.decode(generated_sequence_id)
        generated_sequence = generated_sequence[len(prompt) :]
        generated_sequences.append(generated_sequence.strip())

    return generated_sequences

# 코드 생성기 실행
prompt = "Write a Python function to calculate the factorial of the input number"

generated_code = generate_code(prompt)
print("Generated code:")
print(generated_code[0])

