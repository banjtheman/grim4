import streamlit as st
import utils

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Grimoire</h1>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align: center;'>The magical tool for generating ideas and prompts for writing</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p align='center'><img src='https://raw.githubusercontent.com/banjtheman/grimoire/master/grim/assets/spellbook.png'/></p>",
    unsafe_allow_html=True,
)


# Read from a list of prompts
prompts = utils.load_json("prompts.json")

# Create a list of categories from the prompts that the user can choose
categories = list(set([prompt["category"] for prompt in prompts]))

st.markdown(
    "<h3 style='text-align: center;'>From the dropdown menu, choose the category of prompts that you want to view. Then copy a prompt to <a href='https://chat.openai.com'>ChatGPT</a>, and get results</h3>",
    unsafe_allow_html=True,
)

category = st.selectbox(
    "Select a category:",
    categories,
    help="Select a category: From the dropdown menu, choose the category of prompts that you want to view.",
)

# When the category is selected, display a grid view of each of the prompts
selected_prompts = [prompt for prompt in prompts if prompt["category"] == category]
st.markdown("### Prompts")


col1, col2, col3 = st.columns(3)


for index, prompt in enumerate(selected_prompts):

    if index % 3 == 0:
        utils.display_prompt(col1, prompt)
    elif index % 3 == 1:
        utils.display_prompt(col2, prompt)
    else:
        utils.display_prompt(col3, prompt)

# TODO api is too convulated, needing chronium and session keys atm
# Have a button that will send an API call to ChatGPT with the prompt the user input
# if st.button("Send to ChatGPT"):
#     # Have a spinner wait while waiting for the API to return
#     with st.spinner("Generating response..."):
#         # Send the API call to ChatGPT
#         response = utils.send_to_chatgpt(edited_prompt)
#     # Display the response from the API
#     st.write(response)
