import streamlit as st
from openai import OpenAI

# API 키 입력 받기
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = st.text_input("API Key를 입력하세요", type="password")

# Prompt1을 세션 상태에 저장 (한 번만 설정되도록)
if 'prompt1' not in st.session_state:
    st.session_state['prompt1'] = ''

@st.cache_data
def ask(prompt, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat_completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

# API 키 입력 필드 및 질문 입력 필드
if st.session_state['api_key']:
    st.session_state['prompt1'] = st.text_input("질문?", value=st.session_state['prompt1'])

    if st.button("실행"):
        answer = ask(st.session_state['prompt1'], st.session_state['api_key'])
        st.markdown(answer)
else:
    st.warning("API Key를 입력하세요.")
