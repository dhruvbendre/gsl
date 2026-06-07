import streamlit as st
from src.screens.hackathon_screen import hackathon_screen
from src.ui.base_layout import style_base_layout
from src.ui.home_layout import home_header
from src.components.register_dialog import register_dialog
from src.screens.know_more_screen import know_more
from src.pipelines.RAG import EmbeddingManager,VectorStoreManager,RAGRetriever,load_all_pdfs,split_docs
from langchain_groq import ChatGroq

def home_screen():
    home_header()
    st.subheader("Get Set Learn",text_alignment="center")
    st.video("https://youtu.be/QTPSSerVZsc?si=tOKK4BglVKpj57EG")
    col1,col2,col3 = st.columns(3)
    with col1:
        if st.button("Register !",key="btn1",width="stretch"):
            register_dialog()

    with col2:
        with open("C:/Users/Dhruv Bendre/OneDrive/Desktop/Get Set Learn Hackathon/STEM_Hackathon_Brochure.pdf", "rb") as file:
            st.download_button(
                label="Brochure",
                data=file,
                file_name="STEM_Hackathon_Brochure.pdf", 
                mime="application/pdf",                 
                key="h1_broch",
                use_container_width=True                
            )
    with col3:
        if st.button("Know More",width="stretch"):
            st.session_state.type = "knowmore"
            st.rerun()
            




    st.header("All About The Event",text_alignment="center")
    st.write("The Get Set Learn STEM Hackathon is a platform for school students to turn ideas into innovative solutions. Participants will tackle real-world challenges, collaborate with peers, and apply STEM concepts to create impactful projects.")
    st.markdown("""
        <div class="card-container">
            <div class="info-card">
                <div class="card-title">What is STEM?</div>
                <div class="card-body">
                    A STEM Hackathon is an exciting challenge where teams build real-world inventions using Science, Technology, Engineering, and Math!
                </div>
            </div>
            <div class="info-card">
                <div class="card-title">Learn & Grow</div>
                <div class="card-body">
                    Kids team up to tackle awesome puzzles, code cool programs, and showcase their creative ideas within a 24-72 hour timeline.
                </div>
            </div>
            <div class="info-card">
                <div class="card-title">Awesome Prizes</div>
                <div class="card-body">
                    Show off your innovation to judges, win cool medals, and take home fantastic tech gadgets for your hard work!
                </div>
            </div>
           <div class="info-card">
    <div class="card-title">Mentors</div>
    <div class="card-body">
        <strong>50+ Industry Experts</strong><br>
        Guidance from AI, Robotics, Coding, Design, and STEM professionals throughout the hackathon.
    </div>
    </div>

    <div class="info-card">
        <div class="card-title">Event Days</div>
        <div class="card-body">
            <strong>23–24 June 2026</strong><br>
            2 days of innovation, workshops, mentoring sessions, project building, and final presentations.
        </div>
    </div>

    <div class="info-card">
        <div class="card-title">Hurry Up!</div>
        <div class="card-body">
            <strong>Registration Closes 10 June</strong><br>
            Limited seats available. Secure your team's spot before applications close.
        </div>
    </div>
    """, unsafe_allow_html=True)


    if st.button("Explore more"):
        st.session_state['type']='Explore'
        st.rerun()
        

