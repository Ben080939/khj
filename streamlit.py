import streamlit as st

st.header("open api key를 입력하세요.")

apikey = st.text_input("API Key",key="api", type="password")

if 'aws_key' not in st.session_state:
    st.session_state = ['aws_key'] = 'apikey'
	
    or
    
    st.session_state.aws_key = 'apikey'
st.divider() 

st.header("무엇이든 물어보세요.")

prompt1 = st.text_input("질문?")

if st.button("실행"):
   from openai import OpenAI
   client = OpenAI(api_key= apikey)
   response = client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt1},
     ]
   )
   st.markdown(response.choices[0].message.content)



