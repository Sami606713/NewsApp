import streamlit as st
# import pandas as pd
# import requests
from utils import get_data,get_title,get_description,get_image,get_content,get_url
import webbrowser as wb

# Set the title
st.title("My News App⏳")

# Get the data
response=get_data()

# Set the index in session state
if 'index' not in st.session_state:
    st.session_state.index = 0


main_container=st.container(border=True)
def update_news(index):
    # main_container=st.container(border=True)
    main_container.empty()
    with main_container:
        with st.container(border=True):
            with st.columns(1)[0]:
                image= get_image(response,index)
                try:
                    st.write("Image")
                    st.image(image)
                except:
                    st.write("Image not found")
                
        
        with st.container(border=True):
            with st.columns(1)[0]: 
                title=get_title(response,index)
                st.write(f"title:  {title}")
        
        # Description
        with st.container(border=True):
            with st.columns(1)[0]:
                desc=get_description(response,index)
                st.write(f"description: {desc}")
        
        # Content
        with st.container(border=True):
            with st.columns(1)[0]:
                cont=get_content(response,index)
                st.write(f"content: {cont}")
                if(st.button("Read More")):
                    url=get_url(response,index)
                    wb.open_new_tab(url=url)


update_news(st.session_state.index)
with main_container:
    btn1,btn2=st.columns(2)
    with btn1:
        if(st.button("prev")):
            st.session_state.index -= 1

    with btn2:
        if(st.button("Next")):
            st.session_state.index+=1
    