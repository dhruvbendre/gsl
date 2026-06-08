import streamlit as st
import segno
import io
from src.database.db import create_registrations
from src.screens.pay_screen import pay_screen
from src.database.db import get_team_mem

@st.dialog("Register for hackathon")
def register_dialog():
    col1,col2 = st.columns(2)
    with col1:
        fullname = st.text_input("Team Leaders Name*",placeholder="DhruvBendre")
    with col2:
        email = st.text_input("Gmail*",placeholder="abcd@gmail.com")

    col3,col4 = st.columns(2)
    with col3:
        mobile = st.text_input("TeamLeads Mobile*",placeholder="8655251261")
    with col4:
        schoolname = st.text_input("School Name*",placeholder="your school")

    col5,col6 = st.columns(2)
    with col5:
        teamname = st.text_input("Team Name*",placeholder="Tech Titans")
    with col6:
        teamsize = st.text_input("Team Size(Max 4)*")

    col7,col8 = st.columns(2)
    with col7:
        city = st.text_input("City*")
    with col8:
        pincode = st.text_input("Pincode*")

    col9,col10 = st.columns(2)
    with col9:
        member1 = st.text_input("Member 2")
    with col10:
        member2 = st.text_input("Member 3")

    member3 = st.text_input("Member 4",width="stretch")

    if st.button("Proceed further", use_container_width=True):
        with st.spinner("Let's get you registered..."):
            if fullname and email and mobile and schoolname and teamname and teamsize and city and pincode:
                try:
                    # 1. Save data into registrations table
                    new_reg_data = create_registrations(fullname, email, mobile, schoolname, teamname, teamsize, city, pincode)
                
                    # 2. Verify row generation success and grab the unique ID key
                    if new_reg_data and len(new_reg_data) > 0:
                        reg_id = new_reg_data[0]['id']
                        st.session_state.current_reg_id = reg_id
                        
                        # 3. Save team fields directly to table 2 linked with the reg_id
                        get_team_mem(reg_id, fullname, member1, member2, member3)
                        
                        st.toast("Registration & Team Saved!")
                        st.session_state.type = "pay"
                        st.rerun()
                    else:
                        st.error("Failed to generate a registration record.")
                        
                except Exception as e:
        # Extract the detailed message if it's a Supabase/PostgREST error, otherwise use standard string
                    error_msg = getattr(e, 'message', str(e)).lower()
                    
                    # User-friendly error mapping
                    if "email" in error_msg and ("unique" in error_msg or "already exists" in error_msg):
                        st.error("✉️ This email address is already registered. Please use a different one.")

                    elif "teamname" in error_msg or "team_name" in error_msg and ("unique" in error_msg or "already exists" in error_msg):
                        st.error("👥 This team name is already taken. Please choose a unique name for your team.")

                    elif "team_size" in error_msg or "limit" in error_msg:
                        st.error("🚫 Team size limit exceeded. Teams cannot have more than 4 members.")

                    elif "email_format" in error_msg or "invalid input syntax for type email" in error_msg:
                        st.error("✉️ Please enter a valid email address.")
                        
                    else:
                        # Fallback for unexpected errors (still keeping it clean for the user)
                        st.error("⚠️ Something went wrong while saving your details. Please double-check your inputs.")
                        # Optional: Log the real error to your terminal for debugging
                        print(f"DEBUG DB ERROR: {e}")
                        
            else:
                st.error("Please fill all the fields marked with an asterisk (*)")
            
                
                    
                
                    


                