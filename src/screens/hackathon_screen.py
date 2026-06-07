import streamlit as st
from src.components.register_dialog import register_dialog
from src.components.not_started_dialog import not_dialog
from src.ui.base_layout import style_base_layout
from src.components.no_brochure import no_brochure_dialog



def hackathon_screen():
    style_base_layout()
    if st.button("go back home"):
        st.session_state['type']=None
        st.rerun()
    st.header("Upcoming Hackathons/Events")
    st.header("Hackathon 1")
    st.video("https://youtu.be/QTPSSerVZsc?si=SEuWKXegK-nm9ebN")
    
    col1,col2 = st.columns(2)
    with col1:
        if st.button("register",key="btn1",width="stretch"):
            not_dialog()

    with col2:
        if st.button("download brochure",key="h1_broch",width="stretch"):
            no_brochure_dialog()

    st.header("Hackathon 2")
    st.video("https://youtu.be/uaccEYkY_PI?si=TxVEU9hqwrt6OEwH")
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Register!",key="btn2",width="stretch"):
            not_dialog()
    with col2:
        if st.button("download brochure",key="h2_broch",width="stretch"):
            no_brochure_dialog()

    
        