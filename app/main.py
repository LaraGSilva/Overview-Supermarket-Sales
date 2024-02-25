import streamlit as  st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout='wide')

# Opening the file 
try:
    script_dir = os.path.dirname(__file__)
    data_sup = os.path.join(script_dir,'../database/supermarket_sales.csv')
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(f'A  excpetion  ocurred {e}')
    
# Transforming the data to dataframe structure 
df = pd.read_csv(data_sup, sep=';', decimal=',')

# Catching date
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date', ascending=True)

# Left side bar
df['Month'] = df['Date'].apply(lambda x : str(x.year) + '-'+str(x.month))
month = st.sidebar.selectbox('Mês', df['Month'].unique())
df_filtred = df[df['Month'] == month]

# Structure app
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Faturamento total mensal
fig_date = px.bar(df_filtred,x='Date', y='Total',color='City', title='Faturamento total mensal')
col1.plotly_chart(fig_date)

# Faturamento por tipo de produto
fig_prod = px.bar(df_filtred,x='Date', y='Product line',color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_prod)

# Faturamento por filial
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total', title='Faturamento por filial')
col3.plotly_chart(fig_city)

# Faturamento por tipo de pagamento
city_total = df_filtred.groupby('City')[['Total']].sum().reset_index()
fig_kind= px.pie(df_filtred, values='Total', names='payments', title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_kind)

# Avaliacao
city_total = df_filtred.groupby('City')[['Rating']].mean().reset_index()
fig_rating= px.bar(df_filtred,x='City',y='Rating', title='Avaliacao')
col5.plotly_chart(fig_rating)