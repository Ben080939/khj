import streamlit as st
import os
import openai
from openai import OpenAI

apikey = st.text_input("API Key를 입력하세요", type="password")

@st.cache_data()
def ask(pp):
    client = OpenAI(api_key = apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pp},
        ]
    )
    return response.completion.choices[0].message.content

pp = st.text_input("질문을 입력하세요")

if st.button("실행"):
    client = OpenAI(api_key =apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pp},
        ]
    )
    answer = completions.choices[0].message.content
    st.markdown(answer)
   
