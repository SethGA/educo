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

# def on_copy_click(text):
#     st.session_state.copied.append(text)
#     pyperclip.copy(text)

Set a model
if "openai_model" not in st.session_state:
   st.session_state["openai_model"] = "gpt-3.5-turbo"

Initialize chat history
    
# with open("plaid.txt", "r") as file:
#     # Read the contents of the file into a string
#     file_contents = file.read()
    
file_contents = """{
  "added": [
    {
      "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
      "account_owner": null,
      "amount": 72.1,
      "iso_currency_code": "USD",
      "unofficial_currency_code": null,
      "category": [
        "Shops",
        "Supermarkets and Groceries"
      ],
      "category_id": "19046000",
      "check_number": null,
      "counterparties": [
        {
          "name": "Walmart",
          "type": "merchant",
          "logo_url": "https://plaid-merchant-logos.plaid.com/walmart_1100.png",
          "website": "walmart.com",
          "entity_id": "O5W5j4dN9OR3E6ypQmjdkWZZRoXEzVMz2ByWM",
          "confidence_level": "VERY_HIGH"
        }
      ],
      "date": "2023-09-24",
      "datetime": "2023-09-24T11:01:01Z",
      "authorized_date": "2023-09-22",
      "authorized_datetime": "2023-09-22T10:34:50Z",
      "location": {
        "address": "13425 Community Rd",
        "city": "Poway",
        "region": "CA",
        "postal_code": "92064",
        "country": "US",
        "lat": 32.959068,
        "lon": -117.037666,
        "store_number": "1700"
      },
      "name": "PURCHASE WM SUPERCENTER #1700",
      "merchant_name": "Walmart",
      "merchant_entity_id": "O5W5j4dN9OR3E6ypQmjdkWZZRoXEzVMz2ByWM",
      "logo_url": "https://plaid-merchant-logos.plaid.com/walmart_1100.png",
      "website": "walmart.com",
      "payment_meta": {
        "by_order_of": null,
        "payee": null,
        "payer": null,
        "payment_method": null,
        "payment_processor": null,
        "ppd_id": null,
        "reason": null,
        "reference_number": null
      },
      "payment_channel": "in store",
      "pending": false,
      "pending_transaction_id": "no86Eox18VHMvaOVL7gPUM9ap3aR1LsAVZ5nc",
      "personal_finance_category": {
        "primary": "GENERAL_MERCHANDISE",
        "detailed": "GENERAL_MERCHANDISE_SUPERSTORES",
        "confidence_level": "VERY_HIGH"
      },
      "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_GENERAL_MERCHANDISE.png",
      "transaction_id": "lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje",
      "transaction_code": null,
      "transaction_type": "place"
    }
  ],
  "modified": [
    {
      "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
      "account_owner": null,
      "amount": 28.34,
      "iso_currency_code": "USD",
      "unofficial_currency_code": null,
      "category": [
        "Food and Drink",
        "Restaurants",
        "Fast Food"
      ],
      "category_id": "13005032",
      "check_number": null,
      "counterparties": [
        {
          "name": "DoorDash",
          "type": "marketplace",
          "logo_url": "https://plaid-counterparty-logos.plaid.com/doordash_1.png",
          "website": "doordash.com",
          "entity_id": "YNRJg5o2djJLv52nBA1Yn1KpL858egYVo4dpm",
          "confidence_level": "HIGH"
        },
        {
          "name": "Burger King",
          "type": "merchant",
          "logo_url": "https://plaid-merchant-logos.plaid.com/burger_king_155.png",
          "website": "burgerking.com",
          "entity_id": "mVrw538wamwdm22mK8jqpp7qd5br0eeV9o4a1",
          "confidence_level": "VERY_HIGH"
        }
      ],
      "date": "2023-09-28",
      "datetime": "2023-09-28T15:10:09Z",
      "authorized_date": "2023-09-27",
      "authorized_datetime": "2023-09-27T08:01:58Z",
      "location": {
        "address": null,
        "city": null,
        "region": null,
        "postal_code": null,
        "country": null,
        "lat": null,
        "lon": null,
        "store_number": null
      },
      "name": "Dd Doordash Burgerkin",
      "merchant_name": "Burger King",
      "merchant_entity_id": "mVrw538wamwdm22mK8jqpp7qd5br0eeV9o4a1",
      "logo_url": "https://plaid-merchant-logos.plaid.com/burger_king_155.png",
      "website": "burgerking.com",
      "payment_meta": {
        "by_order_of": null,
        "payee": null,
        "payer": null,
        "payment_method": null,
        "payment_processor": null,
        "ppd_id": null,
        "reason": null,
        "reference_number": null
      },
      "payment_channel": "online",
      "pending": true,
      "pending_transaction_id": null,
      "personal_finance_category": {
        "primary": "FOOD_AND_DRINK",
        "detailed": "FOOD_AND_DRINK_FAST_FOOD",
        "confidence_level": "VERY_HIGH"
      },
      "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_FOOD_AND_DRINK.png",
      "transaction_id": "yhnUVvtcGGcCKU0bcz8PDQr5ZUxUXebUvbKC0",
      "transaction_code": null,
      "transaction_type": "digital"
    }
  ],
  "removed": [
    {
      "transaction_id": "CmdQTNgems8BT1B7ibkoUXVPyAeehT3Tmzk0l"
    }
  ],
  "next_cursor": "tVUUL15lYQN5rBnfDIc1I8xudpGdIlw9nsgeXWvhOfkECvUeR663i3Dt1uf/94S8ASkitgLcIiOSqNwzzp+bh89kirazha5vuZHBb2ZA5NtCDkkV",
  "has_more": false,
  "request_id": "Wvhy9PZHQLV8njG"
}
"""

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
    stream=True,
  )
  full_response += response.choices[0].message['content']  # Extract the 'content' property
  placeholder.markdown(full_response + "▌")
  placeholder.markdown(full_response)
  st.session_state.messages.append({"role": "assistant", "content": full_response})
  
    # BUTTON
    # st.button("[copy]", on_click=on_copy_click, args=(full_response,))
