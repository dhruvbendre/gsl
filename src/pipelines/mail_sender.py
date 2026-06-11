import os
import smtplib
import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.email import EmailTools

def trigger_agno_groq_email(recipient_email, fullname, teamname):
    # 1. Set the CORRECT environment variable name BEFORE anything else initializes
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    elif "API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["API_KEY"]

    # Initialize EmailTools to use its internal connection setup
    email_tools = EmailTools(
        sender_email=st.secrets["email"]["sender_email"],
        sender_passkey=st.secrets["email"]["sender_password"], 
        sender_name="GetSetLearn Team",
        receiver_email=recipient_email
    )

    # FIX: Define a clean, explicit wrapper function. 
    # Agno reads these exact parameter names and type hints to build a flawless schema for Groq.
    def send_confirmation_email(subject: str, body: str) -> str:
        """Sends a confirmation email to the user with a specified subject and body text."""
        try:
            # Safely invoke the underlying tool method directly
            return email_tools.email_user(subject=subject, body=body)
        except Exception as error:
            return f"Failed to send email: {str(error)}"

    # 2. Build the Groq-powered Agent
    hackathon_agent = Agent(
        model=Groq(id="qwen/qwen3-32b"),
        # Use our clean wrapper function 'send_confirmation_email' instead of the raw tool instance
        tools=[send_confirmation_email, DuckDuckGoTools()], 
        description=(
            "You are the official operations coordinator agent for the STEM Hackathon GetSetLearn. "
            "Your job is to send beautifully formatted confirmation emails to newly registered teams."
        ),
        instructions=[
            "Use clear headings, clean spacing, and bullet points to layout the information.",
            "Explicitly include the recipient's Full Name and Team Name inside the email text.",
            "Outline key hackathon parameters: it is for kids/students only, late submissions are invalid, and mischief leads to disqualification.",
            "Use DuckDuckGoTools only if you need to double-check general STEM hackathon engagement guidelines, otherwise prioritize sending.",
            # Point the agent to use our custom wrapper name
            "Immediately execute the send_confirmation_email tool function to transmit the message to the user."
        ]
    )

    # 3. Construct the clean instruction prompt command
    prompt = f"""
    Send the registration confirmation email right now.
    
    Email Target Details:
    - Team Leader Name: {fullname}
    - Registered Team Name: {teamname}
    
    Make the subject line precisely: '🎉 Registration Confirmed: STEM Hackathon GetSetLearn!'
    """

    try:
        # Run the agent workflow loop
        hackathon_agent.run(prompt, show_tool_calls=True)
        return True
    except Exception as e:
        print(f"Agno-Groq Agent error: {e}")
        return False