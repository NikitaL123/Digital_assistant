from imports import *
from connection import poluchit_otvet_ot_llm

def vydelit_zadachi(analizirovannyi_transkript: str) -> str:
    prompt = f"""
    Правила формирования задач:
    - Извлеки ВСЕ поставленные задачи
    - Для каждой укажи: кто исполнитель (роль или имя)
    - Если есть сроки - укажи
    - Формат: нумерованный список
    - Если время и дата не названы или не указаны, писать "Не указано"

    Транскрипт:
    {analizirovannyi_transkript}
    """
    return poluchit_otvet_ot_llm(prompt)