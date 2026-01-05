import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Datos vehiculares')

hist_check = st.checkbox('Construir histograma')

if hist_check:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disper_check = st.checkbox('Construir gráfico de dispersión')

if disper_check:
    st.write(
        'Creación de gráfico de dispersión para conocer el precio en función del tipo de vehículo')
    fig = px.scatter(data, x='price', y='type')
    st.plotly_chart(fig, use_container_width=True)
