import streamlit as st
import pandas as pd
from st_supabase_connection import SupabaseConnection, execute_query

st_supabase_client = st.connection("supabase", SupabaseConnection)

def fetch_amc_ids():
    try:
        query = st_supabase_client.table("amc_form").select("amc_id", "client_name")
        result = execute_query(query, ttl=0).data
        amc_ids = [(row['amc_id'], f"{row['client_name']} - {row['amc_id']}") for row in result]
        return amc_ids
    except Exception as e:
        st.error(f"Failed to fetch AMC IDs. Error: {e}")
        return []

def fetch_amc_data(selected_amc_id):
    try:
        amc_id = selected_amc_id.split(' - ')[1]  
        query = st_supabase_client.table("amc_form").select('*').eq('amc_id', amc_id)
        result = execute_query(query, ttl=0).data
        return pd.DataFrame(result)
    except Exception as e:
        st.error(f"Failed to fetch AMC data. Error: {e}")
        return pd.DataFrame()

def fetch_inventory_data(selected_amc_id):
    try:
        amc_id = selected_amc_id.split(' - ')[1]  
        query = st_supabase_client.table("inventory_management").select('*').eq('amc_id', amc_id)
        result = execute_query(query, ttl=0).data
        return pd.DataFrame(result)
    except Exception as e:
        st.error(f"Failed to fetch inventory data. Error: {e}")
        return pd.DataFrame()

st.title("Inventory Management")

amc_ids = fetch_amc_ids()
if not amc_ids:
    st.error("Failed to fetch AMC IDs.")
else:
    options = [option[1] for option in amc_ids]
    keys = [option[0] for option in amc_ids]
    selected_amc_id = st.selectbox("Select Client", options, index=None, key=keys)  

    if selected_amc_id:
        amc_data = fetch_amc_data(selected_amc_id)
        st.subheader(f"AMC Data for AMC ID: {selected_amc_id}")
        st.write(amc_data)

        inventory_data = fetch_inventory_data(selected_amc_id)
        st.subheader(f"Inventory Data for AMC ID: {selected_amc_id}")
        st.write(inventory_data)

    st.subheader("Upload inventory data")

    uploaded_file = st.file_uploader("Choose a CSV or XLSX file", type=['csv', 'xlsx'])
    submit_button = st.button("Upload")

    if submit_button:
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    data = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('.xlsx'):
                    data = pd.read_excel(uploaded_file)
                else:
                    st.error("Invalid file type. Please upload a CSV or XLSX file.")
                    st.stop()

                if 'warranty_ends_on' in data.columns:
                    data['warranty_ends_on'] = pd.to_datetime(data['warranty_ends_on']).dt.strftime('%Y-%m-%d')

                st.subheader("Uploaded Data:")
                st.write(data)

                try:
                    if 'amc_id' not in data.columns:
                        data['amc_id'] = selected_amc_id.split(' - ')[1]  
                    execute_query(st_supabase_client.table("inventory_management").insert(data.to_dict(orient='records')), ttl=0)
                    st.success("Inventory data uploaded successfully!")

                    # Fetch inventory data again after uploading
                    inventory_data = fetch_inventory_data(selected_amc_id)
                    st.subheader(f"Inventory Data for AMC ID: {selected_amc_id}")
                    st.write(inventory_data)

                except Exception as e:
                    st.error(f"Failed to upload inventory data. Error: {e}")

            except Exception as e:
                st.error(f"Failed to process file upload. Error: {e}")

        else:
            st.warning("Please choose a file to upload.")

    st.subheader("Download inventory data")

    try:
        query = st_supabase_client.table("inventory_management").select('*')
        result = execute_query(query, ttl=0).data
        df = pd.DataFrame(result)
        csv = df.to_csv(index=False).encode()

        st.download_button(
            label="Download Inventory Data",
            data=csv,
            file_name="inventory_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Failed to download inventory data. Error: {e}")