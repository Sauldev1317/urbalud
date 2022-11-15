import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt

st.title('Urbalud')
st.write("Proyecto que nos ayuda a determinar si un lugar es optimo para un nuevo centro de salud")
st.write(pd.DataFrame({
    'Ubicación': ['TLAJOMULCO', 'GUADALAJARA', 'ZAPOPAN', 'ZACATECAS'],
    'Población': [10000, 20000, 30000, 40000],
    'Centros medicos': [10, 20, 30, 40],
    'Agua potable': [0, 0, 0, 1],
    'Luz': [1, 1, 0, 1],
    'wifi': [1, 1, 1, 1]
}))



df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)