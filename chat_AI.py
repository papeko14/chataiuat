import streamlit as st
import json
import os
# --- Page Configurations ---

st.set_page_config(page_title="n8n Chatbot App", layout="centered")
# --- Sidebar for Navigation ---
# สร้างเมนูทางด้านซ้าย (Sidebar)
#Data_tes = st.Page(page="testdata.py", title="Data", icon="📅")
chat_bot = st.Page(page="Chat_page.py", title="Chat_bot", icon="🤖")
chat_zone = st.Page(page="Chat_page_zone.py", title="Chat_bot_zone", icon="🤖")
graph = st.Page(page="Graph_data.py", title="Graph", icon="📊")
#test_data = st.Page(page="able_Data.py", title="Table Data", icon="📊")
pg = st.navigation(
        pages=[chat_bot,graph,chat_zone]
    )
pg.run()











