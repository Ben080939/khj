import streamlit as st
from openai import OpenAI

apikey = st.text_input("api key를 입력하세요", type="password") 


st.session_state



if 'key' not in st.session_state: 
    st.session_state['key'] = apikey

@st.cache_data()
def ask(pp):
    client = OpenAI(api_key= st.session_state.key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pp},
        ]
    )
    return response.choices[0].message.content
    
    
pp = st.text_input("질문을 입력하세요")

if st.button("실행"):
    answer = ask(pp)
    st.markdown(answer)
   
