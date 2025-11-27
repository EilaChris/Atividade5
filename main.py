import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv('vacinacao_corrigido.csv')

df['Date_reported']=pd.to_datetime(df['Date_reported'])

fig1=px.line(df, x='date', y='total_vaccinations', color='location', title='Números total de Vacinados')
fig1.update_layout(xaxis_title='Data',yaxis_title='Número total de Vacinados')
fig1.show()

df_brasil_india_usa = df.query('location == "INDIA" or location== "BRAZIL"or location=="UNITED STATES" ')
fig4=px.pie(df_brasil_india_usa, values='people_fully_vaccinated', names='location', title='Pessoas totalmente Vacinadas no Brasil, India e USA')
fig4.show()

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)

st.set_page_config(page_title="DashCovid",layout="wide")
