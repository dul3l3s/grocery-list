import streamlit as st
import pandas as pd
from functions.db import db_connection
from functions.enter_item import enter_item

def main():
    st.write("Enter item:")
    enter_item()

main()