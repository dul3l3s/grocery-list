import streamlit as st
from functions.selectbox import sorted_list
from functions.db import db_connection

def enter_item():
    item_arr = sorted_list()
    connection = db_connection()
    cursor = connection.cursor()

    with st.form("list_entry", clear_on_submit=True):
        left, middle, right, r2 = st.columns(4, vertical_alignment="bottom", gap="medium")
        item_type = left.selectbox("Category", item_arr)
        item_desc = middle.text_input("Description", placeholder="-Required-")
        item_qty = right.number_input("Quantity", min_value=0)
        submit_btn = r2.form_submit_button('Submit')

        if submit_btn:
            # Insert into example
            cursor.execute(
                "insert into grocery_list (item_qty, item_type, item_desc) values (%s, %s, %s)",
                (item_qty, item_type, item_desc)
            )
            # Commit changes
            connection.commit()

    form = left, middle, right, r2

    return form
