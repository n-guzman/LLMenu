from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st


load_dotenv(".env")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with open('llmenu/system_instruction.txt', "r") as file:
    file_content = file.read()
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=file_content)

st.title("Chat")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display chat messages from history on app rerun
for message in st.session_state.chat.history:
    with st.chat_message(message.role if message.role == 'user' else 'assistant'):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input():
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)