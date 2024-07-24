import streamlit as st
import inventory
import database_streamlit

def main():
    page_names = ["Inventory", "Database"]
    page_functions = [inventory.main, database_streamlit.main]

    selected_page = st.selectbox("Select a page", page_names)

    if selected_page == page_names[0]:
        page_functions[0]()
    elif selected_page == page_names[1]:
        page_functions[1]()

if __name__ == "__main__":
    main()