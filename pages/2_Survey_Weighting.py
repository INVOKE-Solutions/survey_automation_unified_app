from module.utils.ui_components import page_style
from module.utils.security import check_password
import streamlit as st

if check_password():
    page_style(title="Survey Weighting")
    st.markdown(
        f"""
        I'll continue tomorrow.
        """
    )