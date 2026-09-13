import streamlit as st
import pandas as pd
import joblib

model = joblib.load('diamant_modell.pkl')  # läser in den redan sparade tränade modellen

st.title("Diamantprisprediktor")

carat = st.number_input("Carat", min_value=0.2, max_value=5.0, value=0.5)
depth = st.number_input("Depth (%)", min_value=40.0, max_value=80.0, value=61.5)
table = st.number_input("Table (%)", min_value=40.0, max_value=100.0, value=57.0)
x = st.number_input("Längd, x (mm)", min_value=0.0, max_value=11.0, value=5.0)
y = st.number_input("Bredd, y (mm)", min_value=0.0, max_value=59.0, value=5.0)
z = st.number_input("Höjd, z (mm)", min_value=0.0, max_value=32.0, value=3.0)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

if st.button("Beräkna pris"):  # koden under körs bara när användaren klickar på knappen
    input_data = pd.DataFrame({  # bygger en rad med exakt samma kolumner som modellen tränades på
        'carat': [carat],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z],
        'cut_Good': [cut == 'Good'],
        'cut_Ideal': [cut == 'Ideal'],
        'cut_Premium': [cut == 'Premium'],
        'cut_Very Good': [cut == 'Very Good'],
        'color_E': [color == 'E'],
        'color_F': [color == 'F'],
        'color_G': [color == 'G'],
        'color_H': [color == 'H'],
        'color_I': [color == 'I'],
        'color_J': [color == 'J'],
        'clarity_IF': [clarity == 'IF'],
        'clarity_SI1': [clarity == 'SI1'],
        'clarity_SI2': [clarity == 'SI2'],
        'clarity_VS1': [clarity == 'VS1'],
        'clarity_VS2': [clarity == 'VS2'],
        'clarity_VVS1': [clarity == 'VVS1'],
        'clarity_VVS2': [clarity == 'VVS2'],
    })

    predicted_price = model.predict(input_data)[0]  # skickar in raden till den sparade modellen och plockar predictionen
    st.success(f"Predikterat pris: {predicted_price:,.0f} $")
