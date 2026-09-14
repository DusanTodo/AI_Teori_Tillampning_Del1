import streamlit as st
import numpy as np
import joblib
from PIL import Image
from streamlit_drawable_canvas import st_canvas

model = joblib.load('mnist_modell.pkl')

st.title("Sifferigenkänning: rita eller ladda upp en siffra")

st.subheader("Rita en siffra (0-9)")
canvas_result = st_canvas(
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None and st.button("Gissa ritad siffra"):
    img = Image.fromarray(canvas_result.image_data.astype("uint8")).convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img)  # redan vit siffra på svart bakgrund, precis som MNIST

    st.image(img_array, caption="Bilden som skickas till modellen (28x28, gråskala)", width=150)

    img_flat = img_array.reshape(1, -1) / 255.0
    prediction = model.predict(img_flat)[0]

    st.success(f"Modellen gissar: {prediction}")

st.subheader("Eller ladda upp en bild")
uploaded_file = st.file_uploader("Ladda upp en bild av en handskriven siffra (0-9)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img)
    img_array = 255 - img_array

    st.image(img_array, caption="Bilden som skickas till modellen (28x28, gråskala)", width=150)

    img_flat = img_array.reshape(1, -1) / 255.0
    prediction = model.predict(img_flat)[0]

    st.success(f"Modellen gissar: {prediction}")
