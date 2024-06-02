import streamlit as st
from openai import OpenAI

apikey = st.text_input("API Key를 입력하세요", type="password")
client = OpenAI(api_key= apikey)

pp = st.text_input("질문을 입력하세요")

if st.button("실행"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pp},
        ]
    )
    answer = response.choices[0].message.content
    st.markdown(answer)
   
