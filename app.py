import streamlit as st

st.title("Analog screening — v0")
lat = st.number_input("Latitude", -90.0, 90.0, 41.3)
lon = st.number_input("Longitude", -180.0, 180.0, 69.2)
st.write(f"You picked {lat}, {lon}")