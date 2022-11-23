import streamlit as st 
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
import altair as alt
import folium
from st_on_hover_tabs import on_hover_tabs
import streamlit as st

from PIL import Image
image = Image.open('./resources/img/map.jpeg')
st.set_page_config(layout="wide")

# SIDEBAR
st.markdown('<style>' + open('./resources/styles/styles.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Demo', 'Money', 'Economy'], 
                         iconName=['dashboard', 'money', 'economy'], default_choice=0)

if tabs =='Demo':
    st.title('Urbalud')
    st.write("Proyecto que nos ayuda a determinar si un lugar es optimo para un nuevo centro de salud")
    gdl_location = [20.6595, -103.3494]
    m = n = o = folium.Map(location=gdl_location, zoom_start = 12)
    folium.Marker(
        gdl_location,
        popup="Parque Agua Azul",
        tooltip="Concha Acústica Agua Azul"
    ).add_to(m)

    # Map year 2020
    st.write("2020")
    st.image(image, caption='Sunrise by the mountains')
    



