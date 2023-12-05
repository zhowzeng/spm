import numpy as np
import pandas as pd
import streamlit as st

st.title("Stock Pattern Matcher")


st.sidebar.title("Configuration")
ticker_symbol = st.sidebar.selectbox("Ticker Symbol", ("2330.TW", "2890.TW"))
lookback = st.sidebar.selectbox("Lookback Size", (5, 10, 20, 60), 3)
horizon = st.sidebar.selectbox("Horizon Size", (5, 10, 20), 2)
n_neighbors = st.sidebar.slider("Number Of Neighbors", 1, 20, 5, 1)


data = pd.DataFrame(
    np.random.randn(n_neighbors, lookback),
    columns=(i + 1 for i in range(lookback)),
    index=(f"stock {i}" for i in range(n_neighbors)),
).T


st.line_chart(
    data,
    color=["#ffaa00"] * n_neighbors,
)

st.dataframe(data)
