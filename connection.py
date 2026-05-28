from imports import *

llm_client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def poluchit_otvet_ot_llm(instruction: str, user_data: str = "") -> str:
    # Инструкции и пользовательские данные разделены на разные сообщения  и это защищает от зловредных запросов в файле, даже если в транскрипте есть
    # что-то типа "игнорируй все инструкции", модель получает это как данные, а не команду.
    messages = [
        {
            "role": "system",
            "content": "Ты полезный цифровой ассистент. Всегда отвечай только на русском, точно и по делу, четко ясно и понятно."
        },
        {
            "role": "user",
            "content": instruction
        }
    ]
    if user_data:
        messages.append({
            "role": "user",
            "content": f"Данные для анализа:\n{user_data}"
        })

    response = llm_client.chat.completions.create(
        model="llama3",
        messages=messages,
        temperature=0.5, # чтобы было точнее ( но работает это как-то 50/50)
        max_tokens=20000
    )
    return response.choices[0].message.content.strip()