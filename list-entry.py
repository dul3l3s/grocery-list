import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

item_arr = [
       '',
       'Hardlines',
       'Produce',
       'Meat',
       'Deli',
       'Dairy',
       'Pets',
       'Cleaning',
       'Beverages',
       'Frozen',
       'Fridge',
       'Dry',
       'Snacks',
       'Health'
   ]
item_arr.sort()

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")

    # Item entry form
    with st.form("list_entry", clear_on_submit=True):
        st.write("Enter item")
        item_type = st.selectbox('Select item type', item_arr)
        item_desc = st.text_input("Item description:")
        item_qty = st.number_input("Select quantity:", min_value=0)

        st.form_submit_button('Submit')

    # This is outside the form
    st.write(item_qty)
    st.write(item_type)
    st.write(item_desc)

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Insert into example
    cursor.execute(
        "insert into grocery_list (item_qty, item_type, item_desc) values (%s, %s, %s)",
        (item_qty, item_type, item_desc)
    )

    # Example query
    cursor.execute("SELECT * from grocery_list;")
    rows = cursor.fetchall()

    # Place database table into a pandas dataframe
    df = pd.DataFrame(rows)

    # Display the dataframe with streamlit
    st.dataframe(df, use_container_width=True)

    print("Results:", rows)
    for r in rows:
        print(f"{r}")

    # Commit changes
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
    st.write(f"Failed to connect: {e}")
