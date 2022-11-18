import streamlit as st 
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
import altair as alt
import folium
from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")


# SIDEBAR
st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
                         iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='Dashboard':
    st.title("Navigation Bar")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Money':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Economy':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))
    

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

# barChart
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


# Map GDL
m = n = o = folium.Map(location=[20.6595, -103.3494], zoom_start = 12)
folium.Marker(
    [20.6595, -103.3494],
    popup="Liberty Bell",
    tooltip="Liberty Bell"
).add_to(m)

st_data_map1 = st_folium(m, width = 725, key = 1)
st_data_map2 = st_folium(n, width = 725, key = 2)
st_data_map3 = st_folium(o, width = 725, key = 3)

""" - Mapa con filtros de año 2010/2020/2030
- Los agebs estarán de colores diferentes según su cluster  
- Sidebar con descripción de cada cluster (atributos ) y gráficas que indiquen estadística descriptiva sobre los datos de la misma base
 - Al dar click a un ageb surge un popup que da los datos del ageb (cluster al que pertenece, descripción del cluster, datos del AGEB) """