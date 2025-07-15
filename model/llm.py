from huggingface_hub import login, InferenceClient

login(token='') #HF_TOKEN

model_id = "mistralai/Mistral-7B-Instruct-v0.2"
client = InferenceClient()

def llm(prompt):
    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return response.choices[0].message["content"]

if __name__=="__main__":
    print("llm is working..")
