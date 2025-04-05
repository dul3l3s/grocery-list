import streamlit as st
from functions.db_ops import enter_item, display_list, truncate_list
from functions.supa_db import *

query = "SELECT item_type, item_desc, item_qty from grocery_list;"

def main():
    st.write("Enter item:")
    enter_item()
    st.write("Current list:")
    truncate_list()
    display_list(query)
    #supa()


main()