from imports import *
from whisper_module import poluchit_transkript
from analysis_module import opredelit_roli_i_analiz
from sammeri_protokol_module import sformirovat_sammeri_i_protokol
from zadachi_module import vydelit_zadachi

st.title("Цифровой ассистент") # Большая жирная надпись (типа лого)

uploaded_file = st.file_uploader("Загрузи запись", # Тоже надпись жирная но меньше, так же кнопка с областью и огр с форматами
                                 type=["mp3", "wav", "m4a", "ogg"])

if uploaded_file is not None:
    os.makedirs("temp_audio", exist_ok=True)
    audio_path = os.path.join("temp_audio", uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Обработать запись", type="primary", use_container_width=True): # Большая кнопка которая начинает едйствие

        # Это Транскрипт
        with st.spinner("Транскрибируем аудио..."): # with st.spinner это вот этот значок с загрузкой
            transkript_vstrechi = poluchit_transkript(audio_path)
        st.subheader("1. Транскрипт")
        st.write(transkript_vstrechi)

        # Это Роли
        with st.spinner("Определяем роли..."): # with st.spinner это вот этот значок с загрузкой
            analiz = opredelit_roli_i_analiz(transkript_vstrechi)
        st.subheader("2. Роли участников")
        st.markdown(analiz)

        # Это и Саммари и протокол
        with st.spinner("Делаем саммари и протокол..."): # with st.spinner это вот этот значок с загрузкой
            results = sformirovat_sammeri_i_protokol(analiz)
        st.subheader("3. Саммари")
        st.write(results["sammeri"])
        st.subheader("Протокол встречи")
        st.write(results["protokol"])

        # Это Задачи
        with st.spinner("Выделяем задачи..."): # with st.spinner это вот этот значок с загрузкой
            zadachi = vydelit_zadachi(analiz)
        st.subheader("4. Задачи")
        st.write(zadachi)

        st.success("Готово")

        #А это чистка
        if os.path.exists(audio_path):
            os.remove(audio_path)