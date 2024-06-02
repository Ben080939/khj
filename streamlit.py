import streamlit as st

st.header("open api key를 입력하세요.")

apikey = st.text_input("API Key",key="api", type="password")

if 'akey' not in st.session_state:
    st.session_state.akey = 'apikey'
	
st.divider() 

st.header("무엇이든 물어보세요.")

@st.cache_data
def ask(prompt):
   from openai import OpenAI
   client = OpenAI(api_key= apikey)
   response = client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt1},
     ]
   )
   answer = st.markdown(response.choices[0].message.content)
   return answer
	
	

prompt1 = st.text_input("질문?")

if st.button("실행"):
	ask(prompt1)
   



