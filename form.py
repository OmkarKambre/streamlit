import streamlit as st
st.image('inmac.png')
st.title("Add Engineer to DB")

with st.form(key="form1"):
    name = st.text_input(label="Name*")
    pno = st.text_input(label="Phone Number*")
    email = st.text_input(label="Email ID*")
    field = st.toggle("Field Engineer")
    location = st.text_input(label="Location")
    domain_option = [
        'IT', 
        'CS'
        ]
    domain = st.selectbox(label="Domain", options=domain_option)
    submit = st.form_submit_button(label="Submit")

if submit:
    if not name or not pno or not email:
        st.warning("Please fill out the Name, Phone Number, and Email fields.")
    else:
        st.write(f"Name: {name}")
        st.write(f"Phone Number: {pno}")
        st.write(f"Email: {email}")
        st.write(f"Field of Interest: {field}")
        st.write(f"Location: {location}")
        st.write(f"Domain: {domain}")