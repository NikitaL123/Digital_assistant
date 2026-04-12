from imports import *
from connection import poluchit_otvet_ot_llm


def sformirovat_sammeri_i_protokol(analizirovannyi_transkript: str) -> Dict[str, str]:

    # Саммари
    prompt_sammeri = f"""
    Преобразуй заметки по встрече в саммари (краткое изложение основной информации, идей или содержания какого-либо источника.).
    Делай коротко, по делу, только ключевые моменты.
    Делай без ошибок (Обращай внимание на окончание предложений, делай окончания правильными!!!!!)

    Транскрипт:
    {analizirovannyi_transkript}
    """
    sammeri = poluchit_otvet_ot_llm(prompt_sammeri)

    # Протокол
    prompt_protokol = f"""
    Сформируй протокол встречи по стандарту:
    - Дата и время совещания (если не указано или не говориться пиши "Не указано")
    - Участники (с ролями)
    - Повестка дня
    - Основные обсуждения
    - Принятые решения
    - Следующие шаги
    - Пиши на русском!!!!

    Транскрипт:
    {analizirovannyi_transkript}
    """
    protokol = poluchit_otvet_ot_llm(prompt_protokol)

    return {"sammeri": sammeri, "protokol": protokol}