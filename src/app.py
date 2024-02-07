import streamlit as st
import pandas as pd
import requests
from utils import get_data,get_title,get_description,get_image

# Set the title
st.title("My News App")

# Get the data
response=get_data()

with st.container(border=True):
    with st.container(border=True):
        with st.columns(1)[0]:
            image= get_image(response,2)
            st.write("Image")
            st.image(image)
    
    with st.container(border=True):
        with st.columns(1)[0]: 
            title=get_title(response,2)
            st.write(f"title:  {title}")
    
    with st.container(border=True):
        with st.columns(1)[0]:
            desc=get_description(response,2)
            st.write(f"description: {desc}")

# Setup the layout