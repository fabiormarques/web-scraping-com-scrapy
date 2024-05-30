import streamlit as st
import pandas as pd
import sqlite3


conn = sqlite3.connect("data/quotes.db")
df = pd.read_sql_query("select * from mercadolivre_itens", conn)
conn.close()

st.title("Pesquisa de Mercado - Tênis Esportivos Mercado Livre")

st.subheader("KPIs principais do sistema")

col1, col2, col3 = st.columns(3)

col1.metric(label="Total de itens", value=df.shape[0])

unique_brands = df["brand"].nunique()
col2.metric(label="Marcas Únicas", value=unique_brands)

average_new_price = df["new_price"].mean()
col3.metric(label="Preço Médio Novo R$",value=f"{average_new_price:.2f}")

st.subheader("Marcas encontradas até a 10ª  página")
col1, col2 = st.columns([4,2])

top_10_pages_brands = df["brand"].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

st.subheader("Preço médio por marca")
col1, col2 = st.columns([4,2])
average_price_brand = df.groupby("brand")["new_price"].mean().sort_values(ascending=False)
col1.bar_chart(average_price_brand)
col2.write(average_price_brand)

st.subheader("Satisfação por marca")
col1, col2 = st.columns([4,2])
df_non_zero_reviews = df[df["reviews_rating_number"] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby("brand")["reviews_rating_number"].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)
