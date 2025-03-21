import streamlit as st
import pandas as pd
from functions.selectbox import sorted_list
from functions.db import db_connection

# Reusable db connection
connection = db_connection()
cursor = connection.cursor()

def enter_item():
    item_arr = sorted_list()

    with st.form("list_entry", clear_on_submit=True):
        left, middle, right, r2 = st.columns(4, vertical_alignment="bottom", gap="medium")
        item_type = left.selectbox("Category", item_arr)
        item_desc = middle.text_input("Description", placeholder="-Required-")
        item_qty = right.number_input("Quantity", min_value=0)
        submit_btn = r2.form_submit_button('Submit')

        if submit_btn and item_type != "-Required-" and item_desc != "" and item_qty != 0:
            # Insert into example
            cursor.execute(
                "insert into grocery_list (item_qty, item_type, item_desc) values (%s, %s, %s)",
                (item_qty, item_type, item_desc)
            )
            # Commit changes
            connection.commit()


def display_list():
    # Example Select query
    cursor.execute("SELECT * from grocery_list;")
    rows = cursor.fetchall()

    # Place database table into a pandas dataframe
    df = pd.DataFrame(rows)

    # Display the dataframe with streamlit
    st.dataframe(df, use_container_width=True)


def truncate_list():
    del_btn = st.button("Delete list?", key='del_btn')
    if del_btn:
        cursor.execute("Truncate grocery_list")
        # Commit changes
        connection.commit()
