import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("PASSWORD")

# Power BI report embed URL
POWERBI_EMBED_URL = os.getenv("POWERBI_EMBED_URL")

st.title("Secure Power BI Dashboard Viewer")

# Password input field
password = st.text_input("Enter password to access the dashboard:", type="password")

# Check password
if st.button("Submit"):
    if PASSWORD and password == PASSWORD:
        st.success("Access granted! Viewing the dashboard below.")
        
        # Embed Power BI dashboard in an iframe
        st.markdown(
            f"""
            <iframe 
                src="{POWERBI_EMBED_URL}" 
                width="100%" 
                height="400" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Access denied! Incorrect password.")
