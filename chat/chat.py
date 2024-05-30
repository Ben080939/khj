import streamlit as st

st.header("open api key를 입력하세요.")
apikey = st.text_input("API Key", type="password")

from openai import OpenAI

client = OpenAI(api_key= apikey)

assistant = client.beta.assistants.create(
  name="assistant",
  description="당신은 유능한 비서입니다.",
  model="gpt-4o",
)

thread = client.beta.threads.create(
  messages=[ ]
)

st.header("무엇이든 물어보세요.")

if "messages" not in st.session_state:
	st.session_state.messages = []

for msg in st.session_state.messages:
	with st.chat_message(msg["role"]):
		st.markdown(msg["content"])

if prompt := st.chat_input("What is up?"):
	st.chat_message("user").markdown(prompt)
	st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
