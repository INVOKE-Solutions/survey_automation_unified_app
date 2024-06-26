import streamlit as st
from PIL import Image

def page_style(title:str):
    '''
    Streamlit page configuration.

    Args:
        - None

    Return:
        - None
    '''
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

    # configure the default settings of the page.
    icon = Image.open('photos/invoke_icon.jpg')
    st.set_page_config(layout="wide",
                       page_title=title, 
                       page_icon=icon,
                       initial_sidebar_state="expanded")
    st.markdown(hide_st_style, unsafe_allow_html=True)
    image = Image.open('photos/invoke_logo.png')
    st.title(title)
    st.image(image)