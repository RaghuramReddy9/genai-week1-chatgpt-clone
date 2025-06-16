import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  


st.set_page_config(page_title="ChatGPT Clone", page_icon="🤖")
st.title("🤖 ChatGPT Clone with Backend")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input field
user_input = st.text_input("💬 Type your message:")

# When user enters a message
if user_input:
    # 1. Save user message
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # 2. Format messages for the API
    messages = [
        {"role": msg["role"], "content": msg["text"]}
        for msg in st.session_state.chat_history
    ]

    # 3. Call OpenAI API
    with st.spinner("🤔 Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ai_reply = response.choices[0].message.content.strip()

        # 4. Save assistant reply
        st.session_state.chat_history.append({"role": "assistant", "text": ai_reply})

# Display conversation
st.markdown("---")
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"👤 **You:** {msg['text']}")
    else:
        st.markdown(f"🤖 **AI:** {msg['text']}")
