import psycopg2
import streamlit as st
from dotenv import load_dotenv
import os


@st.cache_resource
def db_connection():
    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

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
        return connection
    except Exception as e:
        print(f"Failed to connect: {e}")
        st.write(f"Failed to connect: {e}")

