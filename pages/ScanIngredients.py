import streamlit as st
import pytesseract
from PIL import Image,ImageFilter
import numpy as np
from openai import OpenAI

def format_picture(picture):
    picture = Image.open(picture)
    picture = picture.convert("L")
    picture = picture.filter(ImageFilter.UnsharpMask(radius=10, percent=100, threshold=1))
    picture = picture.point(lambda p: p > 85 and 255)
    picture = np.array(picture)
    text = pytesseract.image_to_string(picture)
    return text

def get_completions_from_messages(user_input, model="gpt-4"):
    messages = [{"role":"system","content":"""You are a sassy skincare expert. \ When a user gives you bunch of ingredients, you will tell them the skin issues the ingredients will fix simply and precisely and insert a joke to keep it lively.\ 
             Keep it to the top two or three possible issues they are experiencing and top two fixes the ingredients will do for them. Remember, the skin is a sensitive organ so you want to give the possible best answer.\ Incase you notice toxic ingredients that can cause harm, you will point that out."""},
            {"role":"user","content":"Water, Butylene Glycol, Kojic Acid, Citric Acid"},
            {"role":"assistant","content":"These ingredients will help with even skin tone and skin brightening and so is minding your business. Drink water for clear skin and mind your business."},
            {"role":"user","content":"Dimethiccesy, Cety! AlcoRol, Glycerin, Parki (Shea) Butter, Tiglycende, Aloe BarbadensisMais (Apple) Fruit Extract, Anthemis,Flosmarinus OfficinalisExtract,Oryze Seti 1 Extract, Cateanyi Ethyihexanoate,Geiearyl PhospheaiySitycery| Stearate, Carbomer, BHT,Fragranc’,, Kanitian Gum, Tetrasodium Glutamate Diacetate. 'Phenoxyetharel, Ethyihexyiglycerin, Caprylyl Glycol, HexyleneGlycol, Cironellol, Limonene, Amyl Cinnamal, Geraniol, Hexy!Cinnvarnal, Hydroxycitronellal, Linalool, Sodium Hydroxide,Hydroquionine,Phthalates,Toluene"},
            {"role":"assistant","content":"These are lovely ingredients but be wary of Toluene and Hydroquinone. They are toxic products just like your ex!"},
            {"role":"user","content":user_input}]
    client = OpenAI()
    chat_completion = client.chat.completions.create(
    model = model,
    messages=messages
)
    return chat_completion.choices[0].message.content.replace('\n',' ')

# Set page title and background color
st.set_page_config(page_title='SkinFix', page_icon='🌸', layout='wide')
st.container()
background_color = "#FFEBEB" 

st.subheader("Skin Doc Here! Let me take a look at the Product Ingredients")
st.write("Kindly select a method to upload an image containing the product ingredients")
upload_option = st.radio("Select an option", ["Upload a Picture", "Take a Picture to scan", "Manually Enter the Product Ingredients"])

if upload_option == "Upload a Picture":
    picture = st.file_uploader('Upload a picture of your ingredients to scan', accept_multiple_files=False)

    if picture is not None:
        text = format_picture(picture)

        if len(text.lower().replace('\n', ' ')) > 0:
            text = st.text_area(label='Please edit to be sure we have the right ingredients.', value=text)
            submit = st.button('Submit')

            if submit:
                text = text.lower().replace('\n', ' ')
                st.warning(get_completions_from_messages(user_input=text))
        else:
            st.warning('Ingredients not detected. Please try again.')

elif upload_option == "Take a Picture to scan":
    picture = st.camera_input("Take the picture of ingredients section on the product ")

    if picture is not None:
        text = format_picture(picture)
        text = text.lower().replace('\n', ' ')

        if len(text.lower().replace('\n', ' ')) > 0:
            text = st.text_area(label='Please edit to be sure we have the right ingredients.', value=text)
            submit = st.button('Submit')

            if submit:
                text = text.lower().replace('\n', ' ')
                st.warning(get_completions_from_messages(user_input=text))
        else:
            st.warning('Ingredients not detected. Please try again.')
else:
    text = st.text_area(label='Please Manually fill in the ingredients')
    text = text.lower().replace('\n', ' ')
    submit = st.button('Submit')
    if submit:
        text = text.lower().replace('\n', ' ')
        st.warning(get_completions_from_messages(user_input=text))