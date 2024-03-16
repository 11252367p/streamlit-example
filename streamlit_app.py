

import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Загрузите превью видео с YouTube (замените URL на свой)
youtube_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

# Получите превьюшки видео с помощью YouTube API
response = requests.get(f"https://img.youtube.com/vi/{youtube_url.split('=')[1]}/maxresdefault.jpg")
thumbnail_bytes = BytesIO(response.content)
thumbnail_image = Image.open(thumbnail_bytes)

# Создайте интерфейс с помощью Streamlit
st.title("Превью видео с YouTube")
st.image(thumbnail_image, use_column_width=True)

# Добавьте ползунок для изменения масштаба картинок превьюшек
scale_factor = st.slider("Масштаб", min_value=0.1, max_value=2.0, step=0.1, value=1.0)

# Измените размер превьюшек с учетом масштаба
new_width = int(thumbnail_image.width * scale_factor)
new_height = int(thumbnail_image.height * scale_factor)
thumbnail_image_resized = thumbnail_image.resize((new_width, new_height))

# Отобразите превьюшки видео на тайм-линии
st.image(thumbnail_image_resized, use_column_width=True)

# Запустите Streamlit приложение
if __name__ == "__main__":
    st.set_page_config(page_title="YouTube Preview Timeline", page_icon="🎥")
    st.write("Запустите это приложение с помощью команды `streamlit run your_app.py`")



