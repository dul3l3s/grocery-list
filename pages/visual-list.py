import streamlit as st

st.title("Grocery List")

st.write("### Select quantity")
col1, col2, col3 = st.columns(3, vertical_alignment="bottom")

#Column 1
col1.image('images/lettuce.png', width=100)
item1_qty = col1.number_input('Quantity', min_value=0, key="item1")
sub_btn1 = col1.button('Add to list', key='btn1')

#Column 2
col2.image('images/carrots.png', width=100)
item2_qty = col2.number_input('Quantity', min_value=0, key="item2")
sub_btn2 = col2.button('Add to list', key='btn2')

#Column 3
col3.image('images/tomato.png', width=100)
item3_qty = col3.number_input('Quantity', min_value=0, key="item3")
sub_btn3 = col3.button('Add to list', key='btn3')