import streamlit as st
import pandas as pd

# Загрузите ваш файл JSON с историей просмотров
# Здесь мы предполагаем, что вы уже скачали файл и назвали его "history.json"
history_df = pd.read_json("history.json")

# Создайте интерфейс с помощью Streamlit
st.title("История просмотров на YouTube")
st.dataframe(history_df)

# Добавьте ползунок для масштабирования сетки
scale_factor = st.slider("Масштаб", min_value=0.1, max_value=2.0, step=0.1, value=1.0)

# Отобразите историю просмотров в виде тайм-линии
# Здесь вы можете использовать библиотеки для работы с графиками, например, Plotly или Matplotlib
# Измените размер графика с учетом выбранного масштаба

# Запустите Streamlit приложение
if __name__ == "__main__":
    st.set_page_config(page_title="YouTube History Visualization", page_icon="📺")
    st.write("Запустите это приложение с помощью команды `streamlit run your_app.py`")
