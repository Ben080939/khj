import streamlit as st

st.header("open api key를 입력하세요.")
key = st.text_input("비밀보장", type="password")

if 'key' not in st.session_state:
    st.session_state.key = key

st.divider()

st.header("무엇이든 물어보세요.")

prompt1 = st.text_input("질문?")

@st.cache.data
if st.button("실행"):
   from openai import OpenAI
   client = OpenAI(api_key= key)
   response = client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt1},
     ]
   )
   st.markdown(response.choices[0].message.content)


