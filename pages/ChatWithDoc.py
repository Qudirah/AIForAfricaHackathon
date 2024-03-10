import streamlit as st
from openai import OpenAI

def get_completions_from_messages(user_input,model="gpt-3.5-turbo"):
    messages = [{"role":"system","content":"""Your name is Skin Doc, a Nigerian skincare expert who likes to flirt subtly. You work in a company called SkinFix \ 
                 You first say hi to the user, complement them and then ask what you can do for them\
                 If a user tells you about their skin issues, you make light jokes and then comfort them. Then you tell them three main ingredients to look out for in products and recommend for them a simple skincare routine(Always include a sunscreen within every routine).\
                 Incase the user have no issues with their skin, Compliment them and remind them you are here to listen and advice them about anything skincare.\
                 You help with issues such as formulating skincare routines based on the condition they have told you, You recommend skincare products if they ask, You give good advice and keep the atmosphere light with jokes\
                 """},
            {"role":"user","content":"Hey Doc! My name is qudirah and I suffer from hyperpigmentation and dull skin. I don't know what to do"},
            {"role":"assistant","content":"Hello beautiful qudirah. To tackle hyperpigmentation and dull skin, look for products containing Vitamin C, Niacinamide, and Retinol. A good routine for you would be to cleanse every morning, use a niacinamide infused toner after, follow by a vitamin c or retinol based serum and of course, never forget a sunscreen!"},
            {"role":"user","content":"What does government means? Can you teach me about something other than skincare?"},
            {"role":"assistant","content":"I am only an expert in the skincare field. "},
            {"role":"user","content":"What are some affordable skincare you can recommend?"},
            {"role":"assistant","content":"You can check brands like facefacts for affordable skincare"},
            {"role":"user","content":user_input}]
    client = OpenAI()
    chat_completion = client.chat.completions.create(
    model=model,
    messages=messages
)
    return chat_completion.choices[0].message.content.replace('\n',' ')
st.container()
st.subheader("Hello! Chat with Skin Doc live to talk about your concerns!")

# Initialize session state variables
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input and interaction with assistant
if prompt := st.chat_input("How may Skin Doc Help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user input
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response using get_completions_from_messages
    with st.chat_message("assistant"):
        assistant_response = get_completions_from_messages(prompt, model=st.session_state["openai_model"])
        st.markdown(assistant_response)

    # Save the assistant's response to session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
