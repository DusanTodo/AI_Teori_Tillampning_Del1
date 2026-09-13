import streamlit as st # standard namnet som pd för pandas
import pandas as pd
import joblib

model = joblib.load('bilpris_modell.pkl')  # läser in den redan sparade tränade modellen

st.title("Bilprisprediktor: Toyota & BMW")  # skriver in rubrik i vår stremlit web app

brand = st.selectbox("Märke", ["Toyota", "BMW"])  # drop down meny
year = st.number_input("Årsmodell", min_value=2000, max_value=2023, value=2015)  # st.number_input sifferfält år/mätarställning mm det som var på x variabeln
engine_size = st.number_input("Motorstorlek (liter)", min_value=1.0, max_value=5.0, value=2.0)
mileage = st.number_input("Mätarställning (mil)", min_value=0, max_value=300000, value=100000)
doors = st.number_input("Antal dörrar", min_value=2, max_value=5, value=4)
owner_count = st.number_input("Antal tidigare ägare", min_value=1, max_value=5, value=1)
fuel_type = st.selectbox("Drivmedel", ["Diesel", "Electric", "Hybrid", "Petrol"])
transmission = st.selectbox("Växellåda", ["Automatic", "Manual", "Semi-Automatic"])

if st.button("Beräkna pris"):  # koden under körs bara när anmvändaren klikcar på knappen
    input_data = pd.DataFrame({  # bygger en tabell/dataframe med exakt samma kolumner
        'Year': [year],
        'Engine_Size': [engine_size],
        'Mileage': [mileage],
        'Doors': [doors],
        'Owner_Count': [owner_count],
        'Brand_Toyota': [brand == 'Toyota'],
        'Fuel_Type_Electric': [fuel_type == 'Electric'],
        'Fuel_Type_Hybrid': [fuel_type == 'Hybrid'],
        'Fuel_Type_Petrol': [fuel_type == 'Petrol'],
        'Transmission_Manual': [transmission == 'Manual'],
        'Transmission_Semi-Automatic': [transmission == 'Semi-Automatic'],
    })

    predicted_price = model.predict(input_data)[0]  # skikcar in raden till den sparade linear regression modell och plockar predictionen
    st.success(f"Predikterat pris: {predicted_price:,.0f} kr") # visar resultat i en grön ruta
