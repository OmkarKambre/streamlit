from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from supabase import create_client, Client

st.title("Add Engineer to DB")

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
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