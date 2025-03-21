import streamlit as st
import pandas as pd
from functions.db import db_connection

item_arr = [
       '-Required-',
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

connection = db_connection()

# Item entry form
with st.form("list_entry", clear_on_submit=True):
    st.write("Enter item")
    item_type = st.selectbox('Select item type', item_arr, placeholder='Required')
    item_desc = st.text_input("Item description:", placeholder='Required')
    item_qty = st.number_input("Select quantity:", min_value=0)

    st.form_submit_button('Submit')

# This is outside the form
st.write(item_qty)
st.write(item_type)
st.write(item_desc)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

if item_qty > 0 and item_desc != '' and item_type !='':
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

# Delete a record
with st.form("del_entry", clear_on_submit=True):
    del_id = st.number_input('Entry deletion ID', min_value=0)
    st.form_submit_button(f'Delete entry {del_id}')
st.write(del_id)
try:
    cursor.execute(
        f"delete from grocery_list where id = {del_id}"
    )
except Exception as e:
    st.write(f"error deleting: {e}")

print("Results:", rows)
for r in rows:
    print(f"{r}")

# Commit changes
connection.commit()

# Close the cursor and connection
# cursor.close()
# connection.close()
# print("Connection closed.")
