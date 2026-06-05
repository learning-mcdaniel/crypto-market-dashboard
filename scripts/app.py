import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide"
)

st.title("Crypto Market Dashboard")

conn = sqlite3.connect("data/crypto.db")

df = pd.read_sql("""
SELECT *
FROM crypto_prices
""", conn)

conn.close()

latest = (
    df.sort_values("load_timestamp")
      .groupby("coin")
      .tail(1)
)

col1, col2 = st.columns(2)

with col1:
    btc = latest[latest.coin=="bitcoin"].price.iloc[0]
    st.metric("Bitcoin", f"${btc:,.2f}")

with col2:
    eth = latest[latest.coin=="ethereum"].price.iloc[0]
    st.metric("Ethereum", f"${eth:,.2f}")

coin = st.selectbox(
    "Select Coin",
    df["coin"].unique()
)

filtered = df[df["coin"] == coin]

fig = px.line(
    filtered,
    x="load_timestamp",
    y="price",
    title=f"{coin.title()} Price History"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(filtered)
