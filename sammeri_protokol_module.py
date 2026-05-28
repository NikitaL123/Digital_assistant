from imports import *
from connection import poluchit_otvet_ot_llm


def sformirovat_sammeri_i_protokol(analizirovannyi_transkript: str) -> Dict[str, str]:

    # Саммари
    instruction_sammeri = """
    Преобразуй заметки по встрече в саммари (краткое изложение основной информации, идей или содержания какого-либо источника.).
    Делай коротко, по делу, только ключевые моменты.
    Делай без ошибок (Обращай внимание на окончание предложений, делай окончания правильными!!!!!)
    """
    sammeri = poluchit_otvet_ot_llm(instruction_sammeri, analizirovannyi_transkript)

    # Протокол
    instruction_protokol = """
    Сформируй протокол встречи по стандарту:
    - Дата и время совещания (если не указано или не говориться пиши "Не указано")
    - Участники (с ролями)
    - Повестка дня
    - Основные обсуждения
    - Принятые решения
    - Следующие шаги
    - Пиши на русском!!!!
    """
    protokol = poluchit_otvet_ot_llm(instruction_protokol, analizirovannyi_transkript)

    return {"sammeri": sammeri, "protokol": protokol}