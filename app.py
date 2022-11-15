import streamlit as st 
import pandas as pandas

st.write("FIRST APP")

df = pd.read_csv("")
st.line_chart(df)