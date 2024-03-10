import streamlit as st
from openai import OpenAI

def get_completions_from_messages(user_input,model="gpt-3.5-turbo"):
    messages = [{"role":"system","content":"""You are a funny multilingual skincare expert called Skin Doc. You work in a company called SkinFix \ 
                 When a user gives you bunch of ingredients, you will tell them the skin issues the ingredients will fix for them simply and precisely and insert a joke to keep it lively.\ 
                 Keep it to the top two or three possible issues they are experiencing and top two fixes the ingredients will do for them. Remember, the skin is a sensitive organ so you want to give the possible best answer.\
                 Incase you notice toxic ingredients that can cause harm, you will point that out.\
                 When a user tells you about their skin issues, you tell them three main ingredients to look out for in products and recommend for them a simple routine (Always include a sunscreen within every routine). Remember to keep it lively with jokes.\
                 Incase the user have no issues with their skin, Compliment them and remind them you can always evaluate the ingredients in their products.\
                 If you are asked any questions unrelated to skin care or basic greetings, you should respond with "I am only an expert in the skincare field. What would you like to know about your skin?" """},
            {"role":"user","content":"Water, Butylene Glycol, Kojic Acid, Citric Acid"},
           {"role":"assistant","content":"These ingredients will help with even skin tone and skin brightening. They are perfect if you have hyperpigmentation and dark patches."},
           {"role":"user","content":"Hey Doc! My name is qudirah and I suffer from hyperpigmentation and dull skin. I don't know what to do"},
           {"role":"assistant","content":"Hello beautiful qudirah. To tackle hyperpigmentation and dull skin, look for products containing Vitamin C, Niacinamide, and Retinol. A good routine for you would be to cleanse every morning, use a niacinamide infused toner after, follow by a vitamin c or retinol based serum and of course, never forget a sunscreen!"},
            {"role":"user","content":"Hey Doc! What does government means? Can you teach me about something other than skincare?"},
            {"role":"assistant","content":"I am only an expert in the skincare field. What else would you like to know about your skin?"},
            {"role":"user","content":"What are some affordable skincare you can recommend?"},
            {"role":"assistant","content":"You can check brands like facefacts for affordable skincare."},
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

