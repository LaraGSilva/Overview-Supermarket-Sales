import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout='wide')

# Abrindo o arquivo
try:
    script_dir = os.path.dirname(__file__)
    data_sup = os.path.join(script_dir, '../database/supermarket_sales.csv')
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(f'An exception occurred: {e}')
    
# Transformando os dados em um DataFrame
df = pd.read_csv(data_sup, sep=';', decimal=',')

# Capturando a data
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date', ascending=True)

# Filtros - Barra lateral
df['Month'] = df['Date'].apply(lambda x : str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox('Mês', df['Month'].unique())
cities = ['All Cities'] + list(df['City'].unique())
city = st.sidebar.selectbox('Cidade', cities)

if city == 'All Cities':
    df_filtered = df[df['Month'] == month]
else:
    df_filtered = df[(df['Month'] == month) & (df['City'] == city)]

# Estrutura do app
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# Faturamento total mensal
fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Faturamento total mensal')
fig_date.update_layout(title_x=0.5)  
col1.plotly_chart(fig_date)

# Faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x='Date', y='Product line', color='City', title='Faturamento por produto', orientation='h')
fig_prod.update_layout(title_x=0.5)  
col2.plotly_chart(fig_prod)

# Faturamento por filial
city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total', title='Faturamento por filial')
fig_city.update_layout(title_x=0.5)  
col3.plotly_chart(fig_city)

# Faturamento por tipo de pagamento
city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_kind = px.pie(df_filtered, values='Total', names='Payment', title='Faturamento por categoria de pagamento')
fig_kind.update_layout(title_x=0.5)  
col4.plotly_chart(fig_kind)

# Avaliacao
city_total = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(df_filtered, x='City', y='Rating', title='Avaliacao')
fig_rating.update_layout(title_x=0.5)  
col6.plotly_chart(fig_rating)

# Vendas por tipo de cliente
type_customer = df_filtered.groupby('Customer type')[['Total']].sum().reset_index()
fig_customer = px.pie(df_filtered, values='Total', names='Customer type', title='Faturamento por categoria de cliente', hole=0.5)
fig_customer.update_layout(title_x=0.5)  
col5.plotly_chart(fig_customer)
