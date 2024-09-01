"""
Case Técnico:

O case consiste em uma base no excel anexada à este e-mail ('Forecast Value'), contendo dados de valores(coluna 'Value') atribuídos à certos países (coluna 'Country'), e esses valores variam no tempo (coluna 'Month/Year'). Os valores registrados são de Fevereiro-2022 à Dezembro-2023 (para cada país). 

A nível de negócio, esses valores tratam-se de percentuais de atingimento metas de venda. Por exemplo:
O registro acima indica que a meta para Colombia e Equador, em Fevereiro de 2022 era de 58%.

O objetivo do case consiste basicamente em: a partir do registro de valores que se tem, de Fev-2022 à Dez-2023, prever qual seria o valor de Jan-2024, para cada país.

Para fazer essa previsão, você pode utilizar qualquer técnica e método que for mais confortável para você. A solução deverá ser feita em python e formato de notebook .ipynb ou .py (tanto faz se for por vscode, azure ai studio, google colab, jupyter ou qualquer outra plataforma)
"""

### Import packages ###
# importar formato de data
from datetime import datetime
# Aplicação Web
import streamlit as st
# Requisição para o servidor do BC
import requests, json
# manipulação de dataframes disponíveis
import pandas as pd 
# Visualização Gráfica para análises
import plotly.express as px 
import plotly.graph_objects as go

### Configurações Prévias 
st.set_page_config(layout='wide')


st.title("Forcast Analyst") 
st.markdown(
    """
    Esse é o relatório sobre as principais moedas disponiblizadas pelo **Banco Central do Brasil**.   
    """
)
st.expander('expander', expanded=False)
# Configurar a barra lateral 
with st.sidebar:
    
    PATH = r"/home/usuario/Forex/Forecast Value.xlsx"
    df = pd.read_excel(PATH)
    if st.sidebar.checkbox("Mostrar tabela?"):
        st.header("Raw Data")
        df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"], format='%Y-%m-%d %H:%M:%S.%f')
        df = df.set_index(df["dataHoraCotacao"])
        data = df["cotacaoCompra"].resample('1d').ohlc()
        data.dropna(inplace=True)
        st.dataframe(data)

st.cache_data()

df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"], format='%Y-%m-%d %H:%M:%S.%f')
df = df.set_index(df["dataHoraCotacao"])
data = df["cotacaoCompra"].resample('1d').ohlc()
data.dropna(inplace=True)
fig1 =  go.Figure(data=[go.Candlestick(x=data.index,
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])
fig1.update_layout(title = f'Analise de {moeda} — {moedas[moeda]}')
st.plotly_chart(fig1, use_container_width=True)

# Import the model
# model = MyModel()
# model.load_state_dict(torch.load('model.pt'))