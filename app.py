import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Dashboard Cartera', layout='wide')
st.title('Dashboard Ejecutivo Gestión de Cartera CXC')

uploaded_file = st.file_uploader('Sube Excel Cartera', type=['xlsx'])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
    # Implement full KPIs, charts, filters here based on spec
    st.success('Análisis listo - expande con Plotly para barras, donas, heatmaps etc.')