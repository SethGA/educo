import streamlit as st
import openai
from openai import OpenAI
import random
# import pyperclip

st.set_page_config(
  page_title="Hello",
  page_icon="👋",
  layout="wide",
  initial_sidebar_state="expanded",
  menu_items={
      'Get Help': 'https://www.example.com/help',
      'Report a Bug': 'https://www.example.com/bug',
      'About': '# This is a header\nThis is an about page'
  }
)

st.title("Educo")
st.subheader("Welcome to Educo, your personal financial assistant")

st.markdown("""
---
""")

st.markdown("""
<style>
body {
    color: #ff0000;
    background-color: #000000;
}
</style>
    """, unsafe_allow_html=True)

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    'Please select an option',
     ['Home', 'View Account Balance', 'Transfer Funds', 'Pay Bills', 'Settings'])

if option == 'Home':
    st.sidebar.markdown("Welcome back to your online banking portal. Navigate using the menu to manage your account.")
elif option == 'View Account Balance':
    st.sidebar.markdown("Here you can view the current balance for all your accounts.")
elif option == 'Transfer Funds':
    st.sidebar.markdown("Transfer funds between your accounts or to another bank account.")
elif option == 'Pay Bills':
    st.sidebar.markdown("Manage your bill payments. Set up new payees, schedule payments, and view past transactions.")
elif option == 'Settings':
    st.sidebar.markdown("Manage your account settings. Update personal information, change your password, and more.")



OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# MODEL
if "openai_model" not in st.session_state:
   st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
    


if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "user", "content": file_contents})

if "copied" not in st.session_state:
    st.session_state.copied = []

# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # user
    with st.chat_message("user"):
        st.markdown(prompt)
        # st.session_state.messages.append({"role": "user", "content": vault_prompt})

    # assistant
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
           #stream=True,
        )
        full_response += str(response.choices[0].message)
        placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # BUTTON
    # st.button("[copy]", on_click=on_copy_click, args=(full_response,))
