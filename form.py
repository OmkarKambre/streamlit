import streamlit as st
import os
from supabase import create_client, Client

st.title("Add Engineer to DB")

url = "https://udxcimusmbsraiwwgppa.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkeGNpbXVzbWJzcmFpd3dncHBhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk4MTc4NTIsImV4cCI6MjAzNTM5Mzg1Mn0.S1r-ynq7pKrUFqY68VVtbcH52p1hrJMOnqYoYT3_JCM"
supabase = create_client(url, key)

with st.form(key="form1"):
    name = st.text_input(label="Name*")
    pno = st.text_input(label="Phone Number*")
    email = st.text_input(label="Email ID*")
    field = st.toggle("Field Engineer")
    location = st.text_input(label="Location")
    domain_option = ['IT','CS']
    domain = st.selectbox(label="Domain", options=domain_option)
    submit = st.form_submit_button(label="Submit")

if submit:
    if not name or not pno or not email:
        st.warning("Please fill out the Name, Phone Number, and Email fields.")
    else:
        data = {
                "name": name,
                "pno": pno,
                "email": email,
                "location": location,
                "domain": domain,
                "toggle_field": field
            }
        response = supabase.table("basic_form").insert([data]).execute()

        if response:
            st.success("Data inserted successfully.")
        else:
            st.error("Failed to insert data. Please try again.")