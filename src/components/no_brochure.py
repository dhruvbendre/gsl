import streamlit as st
import segno
import io
from src.database.db import create_registrations
from src.screens.pay_screen import pay_screen
from src.ui.base_layout import style_base_layout

@st.dialog("Ooops!")
def no_brochure_dialog():
    style_base_layout()
    st.header("brochure is not available yet")