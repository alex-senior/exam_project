import streamlit as st

st.set_page_config(
    page_title="Web Aplication",
    page_icon="👋",
)

st.title("Мій веб-додаток")
st.subheader("Список моїх лабораторних робіт:")

#st.button("Відеозапис")

@st.dialog("Опис")
def descr(filepath):
    st.write(open(filepath, 'r', encoding='utf-8').read())
    st.link_button('View', 'WEB/labs/lab1/lab1.py')

lb1 = st.button('Лабораторна робота №1')
if lb1:
    descr('WEB/labs/lab1/README.md')
lb2 = st.button('Лабораторна робота №2')
if lb2:
    descr('WEB/labs/lab2/README.md')
lb3 = st.button('Лабораторна робота №3')
if lb3:
    descr('WEB/labs/lab3/README.md')
lb4 = st.button('Лабораторна робота №4')
if lb4:
    descr('WEB/labs/lab4/README.md')
lb5 = st.button('Лабораторна робота №5')
if lb5:
    descr('WEB/labs/lab5/README.md')
lb6 = st.button('Лабораторна робота №6')
if lb6:
    descr('WEB/labs/lab6/README.md')
lb7 = st.button('Лабораторна робота №7')
if lb7:
    descr('WEB/labs/lab7/README.md')