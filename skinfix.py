import streamlit as st
st.set_page_config(page_title='SkinFix', page_icon='🌸', layout='wide')

st.page_link("skinfix.py", label="HOME")
st.page_link("pages/ChatWithDoc.py", label="CHAT WITH SKIN DOC")
st.page_link("pages/ScanIngredients.py", label="SCAN YOUR PRODUCT INGREDIENTS" )
st.container()
# Set page title and background color
background_color = "#FFEBEB" 
## Set a soft color scheme
st.markdown(f"""
    <style>
        body {{
            color: #484848;
            background-color: {background_color};
        }}
        .st-bw {{
            background-color: {background_color};
            color: #484848;
        }}
        .st-at {{
            background-color: {background_color};
            color: #484848;
        }}
        .st-eq {{
            background-color: {background_color};
            color: #484848;
        }}
        .st-eu {{
            background-color: {background_color};
            color: #484848;
        }}
        .st-ez {{
            background-color: {background_color};
            color: #484848;
        }}
    </style>
""", unsafe_allow_html=True)
# Main title
st.title('SkinFix')

st.header("""Welcome to SkinFix!""")
st.write("""Are you ready to dive into the world of radiant skin? 🌟
At SkinFix, we believe that every skincare journey should be filled with confidence, joy, and a touch of magic! ✨ Whether you're a skincare newbie or a seasoned enthusiast, our app is your trusty companion on the path to healthy, glowing skin.""")

st.subheader("Why SkinFix?")
st.write("""Glad you asked! Here's the scoop: we're your one-stop destination for all things skincare. From analyzing product ingredients for toxicity to logging your skin concerns, we've got you covered every step of the way. No more guessing games or skincare woes – just pure skincare bliss!)""")



