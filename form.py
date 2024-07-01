import streamlit as st
from supabase import create_client, Client
import re

st.title("Add Engineer to DB")

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
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
        if not re.match(r"^[a-zA-Z ]+$", name):
            st.warning("Invalid name format. Please enter a name that only contains alphabets and spaces.")
        elif not pno.isdigit() or len(pno)!= 10 or not pno.startswith(("7", "8", "9")):
            st.warning("Invalid phone number. Phone number should be 10 digits, start with 7, 8, or 9, and only contain numbers.")
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            st.warning("Invalid email format. Please enter a valid email address.")
        elif not re.match(r"^[a-zA-Z ]+$", location):
            st.warning("Invalid location format. Please enter a name that only contains alphabets and spaces.")
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