import streamlit as st
from utils import get_data,get_title,get_description,get_image,get_content,get_url
import webbrowser as wb

# Set the title
st.title("📰 My News App ⏳")

# Get the data
response=get_data()

# Set the index in session state
if 'index' not in st.session_state:
    st.session_state.index = 0

main_container=st.container(border=True)
def update_news(index):
    # main_container.empty()
    with main_container:
        with st.container(border=True):
            with st.columns(1)[0]:
                image= get_image(response,index)
                try:
                    st.image(image,caption="News Image")
                except:
                    st.write("Image not found")
                
        
        with st.container(border=True):
            with st.columns(1)[0]: 
                title=get_title(response,index)
                st.markdown(f"# {title}")
                st.write(f"{title}")
        
        # Description
        with st.container(border=True):
            with st.columns(1)[0]:
                desc=get_description(response,index)
                st.markdown(f"### {desc}")
        
        # Content
        with st.container(border=True):
            with st.columns(1)[0]:
                cont=get_content(response,index)
                st.markdown(f"#### {cont}")
                if(st.button("Read More")):
                    url=get_url(response,index)
                    wb.open_new_tab(url=url)

        with main_container:
            btn1,btn2=st.columns(2)
            with btn1:
                if(st.button("Prev")):
                    st.session_state.index -= 1

            with btn2:
                if(st.button("Next")):
                    st.session_state.index+=1
        


# Call the update news function
update_news(st.session_state.index)

    
