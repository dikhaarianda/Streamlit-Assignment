import streamlit as st
import pandas as pd

# Linechart dengan dataframe yang dibuat manual
st.header("Penjualan Per-Tahun")

df = pd.DataFrame({
  'year': ['2018', '2019', '2020', '2021', '2022'],
  'sales': [10000, 15000, 17000, 16000, 19000]
}, index=[1,2,3,4,5])

st.write('Tabel:')
st.dataframe(df, width=400)
st.markdown('#')

st.write('Linechart:')
st.line_chart(df, x='year')