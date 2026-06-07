import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.hackathon_screen import hackathon_screen
from src.screens.pay_screen import pay_screen
from src.screens.know_more_screen import know_more

def main():
    st.set_page_config(page_title="Get Set Learn", page_icon=":mortar_board:")

    if 'type' not in st.session_state:
        st.session_state['type'] = None

    match st.session_state['type']:
        case'knowmore':
            know_more()
        case'pay':
            pay_screen()
        case 'Explore':
            hackathon_screen()
        case None:
            home_screen()

main()