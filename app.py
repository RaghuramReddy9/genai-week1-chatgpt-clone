import streamlit as st

st.set_page_config(page_title="ChatGPT Clone 💬")
st.title("ChatGPT Clone")

user_input = st.text_input("You:", "")
if user_input:
    st.write("🤖 Bot: (response coming soon)")
