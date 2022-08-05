import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.write("""
# App para predecir precio de inmuebles
""")

uploaded_file = st.sidebar.file_uploader("Upload input CSV file", type=["csv"])

if uploaded_file is not None:
    
    input_df = pd.DataFrame(data)

else:

    def input_features():

        days_on_site = st.sidebar.slider('Dias en el sitio', 0,150, 1)

        amenities = st.sidebar.slider('Número de amenidades', 0,20, 1)

        age_in_years = st.sidebar.slider('Antiguedad del inmueble en años', 0,500, 1)

        bathrooms = st.sidebar.slider('Número de baños', 0,10, 1)

        cellars = st.sidebar.slider('Número de sotanos', 0,20, 1)

        num_floors = st.sidebar.slider('Número de pisos', 0,50, 1)
        
        monthly_fee_transformed = st.sidebar.slider('Cuota mensual de mantenimiento', 0,5000, 1)

        apartments_per_floor = st.sidebar.slider('Número de Departamentos por piso', 0,20, 1)

        parking_lots = st.sidebar.slider('Número de estacionamientos', 0,200, 1)

        floor_situated = st.sidebar.slider('Piso donde se encuentra', 0,30, 1)

        num_bedrooms = st.sidebar.slider('Número de habitaciones', 0,20, 1)

        m2 = st.sidebar.slider('M2', 0,300, 1)

        lat = st.sidebar.slider('Latitud', -200,200, 1)

        lon = st.sidebar.slider('Longitud', -200,200,1)
        
       

        data = {'days_on_site':[days_on_site],
               'amenities': [amenities],
                'age_in_years': [age_in_years],
                'bathrooms': [bathrooms],
                'cellars': [cellars],
                'num_floors': [num_floors],
                'monthly_fee_transformed': [monthly_fee_transformed],
                'apartments_per_floor': [apartments_per_floor],
                'parking_lots': [parking_lots],
                'floor_situated': [floor_situated],
                'num_bedrooms': [num_bedrooms],
                'm2': [m2],
                'lat': [lat],
                'lon': [lon]
               }

        features = pd.DataFrame(data)

        return features

    input_df = input_features()
    
#load model from current directory
model = pickle.load(open('modelo', 'rb'))


# Crear objeto de predicción
prediction = model.predict(input_df)

# etiquetas
label = np.array(['Precio m2 Cuadrado'])

# diseño
st.subheader('Resultado')
st.write(prediction/input_df['m2'])

