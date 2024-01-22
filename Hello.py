import streamlit as st
import openai
import pyperclip

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.title("Educo")
# st.write("""Chat with gpt-4.""")
# st.sidebar.success("Select an item above")


openai.api_key = ""

def on_copy_click(text):
    st.session_state.copied.append(text)
    pyperclip.copy(text)

# Set a model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo" # gpt-3.5-turbo

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # st.session_state.messages.append({"role": "user", "content": vault_prompt})

if "copied" not in st.session_state:
    st.session_state.copied = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

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
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # BUTTON
    # st.button("[copy]", on_click=on_copy_click, args=(full_response,))