import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("My Web Aplication")
st.subheader("List of my labs:")

list = ['lab1', 'lab2', 'lab3', 'lab4', 'lab5', 'lab6', 'lab7']
s = ''
for i in list:
    s += "- " + i + "\n"
st.markdown(s)