import streamlit as st
import openai

# 페이지 설정
st.set_page_config(page_title="GPT-3.5 Turbo Chatbot", page_icon="🤖")

# API Key를 세션 상태에 저장
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

# API Key 입력 받기
st.session_state.api_key = st.text_input("Enter your OpenAI API key:", type="password", value=st.session_state.api_key)

# 입력된 API Key로 OpenAI 클라이언트 설정
if st.session_state.api_key:
    openai.api_key = st.session_state.api_key

# 질문 입력 받기
question = st.text_input("Ask a question:")

# @st.cache_data를 이용해 입력이 변하지 않으면 rerun 시 저장된 결과 반환
@st.cache_data(ttl=60*5)  # 캐시 유효 기간을 5분으로 설정
def get_response_from_gpt3(question, api_key):
    openai.api_key = api_key  # 함수 내에서 API 키 설정
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# 질문이 입력된 경우 응답 가져오기
if question and st.session_state.api_key:
    try:
        response = get_response_from_gpt3(question, st.session_state.api_key)
        st.write("### Response from GPT-3.5 Turbo:")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.write("Please enter your OpenAI API key and ask a question.")
