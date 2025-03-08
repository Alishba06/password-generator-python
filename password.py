
import streamlit as st
import random
import string

def generate_password(length , use_digits , use_special ):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits # Add number (0-9) if selected

    if use_special:
        characters += string.punctuation # Add sepical characters (! , @ , # , $ , % , & , *) if selected

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password length" , min_value=4 , max_value=32 , value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Speical Characters")

if st.button("Generator Password"):
    password = generate_password(length , use_digits , use_special)
    st.write(f"Generated Password: {password}")

st.write("-----------------------------------------")

st.write("Build with 🖤by [Alishba](https://github.com/Alishba06)")