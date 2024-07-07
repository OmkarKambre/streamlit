import streamlit as st
import pandas as pd
import datetime as dt
import os
from st_supabase_connection import SupabaseConnection, execute_query

st_supabase_client = st.connection(
    name="conn",
    type=SupabaseConnection,
    ttl=None,
    url="https://udxcimusmbsraiwwgppa.supabase.co",
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkeGNpbXVzbWJzcmFpd3dncHBhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk4MTc4NTIsImV4cCI6MjAzNTM5Mzg1Mn0.S1r-ynq7pKrUFqY68VVtbcH52p1hrJMOnqYoYT3_JCM", 
)

    
st.header("Save AMC")
clientName = st.text_input("Client Name")
amcfms, type = st.columns(2)
amcfms = amcfms.selectbox("AMC/FMS", options=["AMC", "FMS", "AMC+FMS", "SFMS", "WIFI AMC"])
type = type.selectbox("Type", options=["Comprehensive", "Non Comprehensive", "Comprehensive + Non Comprehensive", "AMC", "FMS", "Renewal"])
note = st.text_area("Extra Specification")
totalAmt = st.text_input("Total Amount")
start = st.date_input("Start")
end = st.date_input("End")


billing =st.selectbox("Billing", options=["Yearly", "Half Yearly", "Quarterly", "Monthly"])
uploaded_file = st.file_uploader("Add Image", accept_multiple_files=False, type=['png', 'jpg', 'webp', 'jpeg'])

if billing == "Yearly":
    data2 = {
        "Subject":[(clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=5)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=4)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=3)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=2)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=1)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ "0 days" + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=5)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=4)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=3)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=2)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ str(pd.DateOffset(days=1)) + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ "0 days" + " "+ billing),
                   (clientName+" "+ amcfms + " "+ type+ " "+ "0 days" + " "+ billing)],
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
                      pd.to_datetime(end).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
                      pd.to_datetime(end).date()]
    }
    
elif billing == "Quarterly":
    
    data2 = {
        "Subject":[(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing)],
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),
        
        ],
    }
    
else:
    st.text(billing)
    data2 = {
        "Subject":[(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing), 
        
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),(clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),
        (clientName+" "+ amcfms + " "+ type+ " "+ billing),],
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)).date(),(pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)).date(),(pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)).date(),(pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)).date(),(pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)).date(),(pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)).date(),(pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)).date(),(pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)).date(),(pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)).date(),
        
        ],
    }

df2 = pd.DataFrame([data2])  

st.download_button(
   "Press to Download",
   df2.to_csv(index=False).encode('utf-8'),
   "file.csv",
   "text/csv",
   key='download-csv'
)

if st.button("Save"):


    if billing == "Yearly":
        images = []
        if uploaded_file is not None:
            filename = "images/"+str(dt.datetime.now())+uploaded_file.__getattribute__("name")
            st_supabase_client.upload("images", "local",uploaded_file , filename)
            images.append(filename)
            st.write(uploaded_file.__getattribute__("name").split('.')[-1])
        
        data = {
            "client_name":[clientName],
            "service":[amcfms],
            "type_service":[type],
            "total_amount":[totalAmt],
            "s_date":[start],
            "e_date":[end],
            "billing":[billing],
            "note":[note],
            "img_url" : [images]
        }
        execute_query(st_supabase_client.table("amc_form").insert(data),ttl=0,)
        df=pd.DataFrame(data)
        st.dataframe(df)


    elif billing == "Half Yearly":
        images = []
        if uploaded_file is not None:
            filename = "images/"+str(dt.datetime.now())+uploaded_file.__getattribute__("name")
            st_supabase_client.upload("images", "local",uploaded_file , filename)
            images.append(filename)
            st.write(uploaded_file.__getattribute__("name").split('.')[-1])
        
        data = {
            "client_name":[clientName],
            "service":[amcfms],
            "type_service":[type],
            "total_amount":[totalAmt],
            "s_date":[start],
            "e_date":[end],
            "billing":[billing],
            "P1 Start":[start],
            "P1 End":[(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date()],
            "P2 Start":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "P2 End":[end],
            "note":[note],
            "img_url" : [images]
        }
        execute_query(st_supabase_client.table("amc_form").insert(data),ttl=0,)
        df=pd.DataFrame(data)
        st.dataframe(df)


    elif billing == "Quarterly":
        images = []
        if uploaded_file is not None:
            filename = "images/"+str(dt.datetime.now())+uploaded_file.__getattribute__("name")
            st_supabase_client.upload("images", "local",uploaded_file , filename)
            images.append(filename)
            st.write(uploaded_file.__getattribute__("name").split('.')[-1])
        data = {
            "client_name":[clientName],
            "service":[amcfms],
            "type_service":[type],
            "total_amount":[totalAmt],
            "s_date":[start],
            "e_date":[end],
            "billing":[billing],
            "Q1 Start":[start],
            "Q1 End":[(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date()],
            "Q2 Start":[(pd.to_datetime(start)+pd.DateOffset(months=3)).date()],
            "Q2 End":[(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date()],
            "Q3 Start":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "Q3 End":[(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date()],
            "Q4 Start":[(pd.to_datetime(start)+pd.DateOffset(months=9)+pd.DateOffset(days=1)).date()],
            "Q4 End":[(pd.to_datetime(start)+pd.DateOffset(months=12)-pd.DateOffset(days=1)).date()],
            "note":[note],
            "img_url" : [images]
        }
        execute_query(st_supabase_client.table("amc_form").insert(data),ttl=0,)
        df=pd.DataFrame(data)
        st.dataframe(df)

        
    else:
        images = []
        if uploaded_file is not None:
            filename = "images/"+str(dt.datetime.now())+uploaded_file.__getattribute__("name")
            st_supabase_client.upload("images", "local",uploaded_file , filename)
            images.append(filename)
            st.write(uploaded_file.__getattribute__("name").split('.')[-1])
        data = {
            "client_name":[clientName],
            "service":[amcfms],
            "type_service":[type],
            "total_amount":[totalAmt],
            "s_date":[start],
            "e_date":[end],
            "billing":[billing],
            "M1":[start],
            "M2":[(pd.to_datetime(start)+pd.DateOffset(months=1)).date()],
            "M3":[(pd.to_datetime(start)+pd.DateOffset(months=2)).date()],
            "M4":[(pd.to_datetime(start)+pd.DateOffset(months=3)).date()],
            "M5":[(pd.to_datetime(start)+pd.DateOffset(months=4)).date()],
            "M6":[(pd.to_datetime(start)+pd.DateOffset(months=5)).date()],
            "M7":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "M8":[(pd.to_datetime(start)+pd.DateOffset(months=7)).date()],
            "M9":[(pd.to_datetime(start)+pd.DateOffset(months=8)).date()],
            "M10":[(pd.to_datetime(start)+pd.DateOffset(months=9)).date()],
            "M11":[(pd.to_datetime(start)+pd.DateOffset(months=10)).date()],
            "M12":[(pd.to_datetime(start)+pd.DateOffset(months=11)).date()],
            "note":[note],
            "img_url" : [images]
        }
        execute_query(st_supabase_client.table("amc_form").insert(data),ttl=0,)
        df=pd.DataFrame(data)
        st.dataframe(df)