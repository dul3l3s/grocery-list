import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("url")
key = os.environ.get("key")

if not url or not key:
    raise ValueError("Supabase URL and key must be set in environment variables")

supabase: Client = create_client(url, key)

def supa():
    try:
        # Fetch data from Supabase
        response = supabase.table("grocery_list").select("*").execute()
        st.write(response)

        return response
    except Exception as e:
        print(f"An unexpected error occurred: {e}")