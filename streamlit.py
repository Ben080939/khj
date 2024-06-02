import streamlit as st
import openai

api_key = st.text_input("API Key를 입력하세요", type="password")

@st.cache_data()
def ask(prompt):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]

prompt1 = st.text_input("질문을 입력하세요")

if st.button("실행"):
    if api_key:
        answer = ask(prompt1)
        st.markdown(answer)
    else:
        st.error("API Key를 입력하세요.")
