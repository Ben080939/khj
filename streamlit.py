import streamlit as st
import openai
import os

apikey = st.text_input("API Key를 입력하세요", type="password")

@st.cache_data()
def ask(prompt):
    client = OpenAI(api_key=apikey)
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
    answer = ask(prompt1)
    st.markdown(answer)
   
