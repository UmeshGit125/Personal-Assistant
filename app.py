import os
from dotenv import load_dotenv
import streamlit as st
import requests

# Load environment variables
load_dotenv()

URL = os.getenv("N8N_WEBHOOK_URL")

if not URL:
    st.error("Webhook URL not configured.")
    st.stop()



st.set_page_config(page_title="Personal Assistant", page_icon="🤝")

st.title("🤝 Your Personal Assistant")
st.subheader("What can your personal assistant do?")

st.markdown("""
1. Answer questions on various topics  
2. Arrange calendar events and meetings  
3. Read emails and send replies  
4. Manage tasks and to-do lists  
5. Take quick notes  
6. Track expenses and budgeting  
""")

st.subheader("💬 Chat with your assistant")

# 🔹 Store chat history safely
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 🔹 Chat input
user_message = st.chat_input("Type your message here...")

if user_message:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # 🔹 Show loading spinner while waiting
    with st.spinner("Thinking..."):

        try:
            response = requests.post(
                URL,
                json={"message": user_message},
                timeout=30
            )

            # Debug (optional — remove later)
            print("Status code:", response.status_code)
            print("Raw response:", response.text)

            # 🔴 Handle non-200 errors
            if response.status_code != 200:
                ai_response = f"⚠️ Server error ({response.status_code}): {response.text}"

            # 🔴 Handle empty response
            elif not response.text.strip():
                ai_response = "⚠️ Empty response from n8n."

            else:
                try:
                    data = response.json()

                    # If n8n returns list
                    if isinstance(data, list) and len(data) > 0:
                        ai_response = data[0].get("output", str(data[0]))

                    # If n8n returns dict
                    elif isinstance(data, dict):
                        ai_response = data.get("output", str(data))

                    else:
                        ai_response = f"⚠️ Unexpected response format:\n{data}"

                except Exception:
                    ai_response = f"⚠️ Invalid JSON returned:\n{response.text}"

        except requests.exceptions.Timeout:
            ai_response = "⚠️ Request timed out. Please try again."

        except requests.exceptions.ConnectionError:
            ai_response = "⚠️ Cannot connect to n8n. Is it running?"

        except Exception as e:
            ai_response = f"⚠️ Unexpected error:\n{str(e)}"

    # 🔹 Show AI message
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })