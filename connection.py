from imports import *

llm_client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def poluchit_otvet_ot_llm(prompt: str) -> str:
    response = llm_client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": "Ты полезный цифровой ассистент . Всегда отвечай только на русском, точно и по делу, четко ясно и понятно."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,      # чтобы было точнее ( но работает это как-то 50/50)
        max_tokens=20000
    )
    return response.choices[0].message.content.strip()