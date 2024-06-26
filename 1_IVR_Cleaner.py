import streamlit as st
from utils.ui_components import page_style
from utils.security import check_password

if check_password():
    page_style(title="IVR Data Cleaning")
    st.markdown(
        f"""
        Fahmi's IVR Data Cleaner.
        """
    )
