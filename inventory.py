import streamlit as st
import pandas as pd
import chardet
from st_supabase_connection import SupabaseConnection, execute_query
import datetime as dt
import io

st_supabase_client = st.connection(
    "supabase", SupabaseConnection
)

st.title("Inventory Management")

# #1: Upload inventory data
st.subheader("1. Upload inventory data")

uploaded_file = st.file_uploader("Choose a CSV or XLSX file", type=['csv','xlsx'])
submit_button = st.button("Submit")

if uploaded_file is not None and submit_button:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Failed to read CSV file. Error: {e}")
            st.stop()  # Stop the script execution
    elif uploaded_file.name.endswith('.xlsx'):
        try:
            data = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Failed to read XLSX file. Error: {e}")
            st.stop()  # Stop the script execution
    else:
        st.error("Invalid file type. Please upload a CSV or XLSX file.")
        st.stop()  # Stop the script execution

    # Convert warranty_ends_on column to string format
    if 'warranty_ends_on' in data.columns:
        data['warranty_ends_on'] = data['warranty_ends_on'].dt.strftime('%Y-%m-%d')

    # Validate columns
    required_columns = ["branch_name", "loc", "machine_type", "model_name", "model_no", "serial_number", "specs", "user", "warranty_ends_on", "warranty_status"]
    if not all(col in data.columns for col in required_columns):
        st.error("File is missing required columns. Please upload a valid CSV or XLSX file.")
        st.stop()  # Stop the script execution
    else:
        # Insert data into Supabase database
        try:
            execute_query(st_supabase_client.table("inventory_management").insert(data.to_dict(orient='records')), ttl=0)
            st.success("Inventory data uploaded successfully!")
        except Exception as e:
            st.error(f"Failed to upload inventory data. Error: {e}")

# #2: Download inventory data
st.subheader("2. Download inventory data")

try:
    data = execute_query(st_supabase_client.table("inventory_management").select('*'), ttl=0).data
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False).encode()

    st.download_button(
        label="Download Inventory Data",
        data=csv,
        file_name="inventory_data.csv",
        mime="text/csv"
    )
except Exception as e:
    st.error(f"Failed to download inventory data. Error: {e}")