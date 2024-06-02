import streamlit as st
from openai import OpenAI

if 'api_key' not in st.session_state:
    st.session_state['api_key'] = st.secrets["openai_api_key"]

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

# 입력 필드
st.session_state['prompt1'] = st.text_input("질문?", value=st.session_state['prompt1'])

if st.button("실행"):
    answer = ask(st.session_state['prompt1'], st.session_state['api_key'])
    st.markdown(answer)
