import streamlit as st
import pandas as pd
import numpy as np

# Bar-chart
np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2018', '2019', '2020', '2021', '2022'],
  'Produk1': np.random.randint(100, 1000, 5),
  'Produk2': np.random.randint(100, 1000, 5),
  'Produk3': np.random.randint(100, 1000, 5)
  })

st.write('Show bar-chart:')
st.bar_chart(df.set_index('Tahun'))