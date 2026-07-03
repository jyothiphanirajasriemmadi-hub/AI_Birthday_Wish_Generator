import streamlit as st
from prompts import birthday_prompt
from utils import generate_wish

st.title("🎂 AI Birthday Wish Generator")
name=st.text_input("Recipient Name")
relationship=st.selectbox("Relationship",["Friend","Family","Colleague"])
age=st.number_input("Age",1,120,25)
tone=st.selectbox("Tone",["Funny","Emotional","Formal","Inspirational","Casual"])
language=st.selectbox("Language",["English","Telugu","Hindi"])
if st.button("Generate"):
    if name:
        st.write(generate_wish(birthday_prompt(name,relationship,age,tone,language)))
    else:
        st.warning("Enter a name")
