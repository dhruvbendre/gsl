import streamlit as st
from src.database.config import supabase
import bcrypt
from supabase import PostgrestAPIError


print("db.py loaded")

def create_registrations(fullname,email,mobile,schoolname,teamname,teamsize,city,pincode):
    data = {"team_name":teamname,"team_leader_name":fullname,"team_leader_email":email,"school_name":schoolname,"team_leader_phone":mobile,"team_size":teamsize,"pincode":pincode,"City":city}
    response = supabase.table('registrations').insert(data).execute()
    return response.data

def get_registrations(reg_id=None):
    if not reg_id:
        return None
    try:
        response = supabase.table("registrations").select("*").eq("id", reg_id).single().execute()
        return response.data
    except PostgrestAPIError as e:
        st.error(f"Database error: {e.message}")
        return None
    except Exception:
        return None
    
def get_team_mem(regid,fullname,member1,member2,member3):
    data = {"registration_id":regid,"team_leader_name":fullname,"member2":member1,"member3":member2,"member4":member3}
    response = supabase.table("members").insert(data).execute()
    return response.data