import streamlit as st
import numpy as np

st.title("Streamlit Tutorial App")
st.write("This is my new app")

button1 = st.button("Click Me")
if button1:
    st.write("Button Clicked")

like = st.checkbox("Do you like this app")