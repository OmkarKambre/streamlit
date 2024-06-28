import streamlit as st

with st.form(key="form1"):
    name = st.text_input(label="Enter name")
    pno = st.text_input(label="Enter phone number")
    email = st.text_input(label="Enter email")
    interest = ["ML", "AI"]
    ml_interest = st.checkbox(label="ML", value=False)
    ai_interest = st.checkbox(label="AI", value=False)
    location = st.text_input(label="Enter location")
    domain_option = [
        'IT', 
        'CS'
        ]
    domain = st.selectbox(label="Domain", options=domain_option)
    submit = st.form_submit_button(label="Submit")

if submit:
    st.write(f"Name: {name}")
    st.write(f"Phone Number: {pno}")
    st.write(f"Email: {email}")
    st.write(f"Field of Interest: {ml_interest, ai_interest}")
    st.write(f"Location: {location}")
    st.write(f"Domain: {domain}")