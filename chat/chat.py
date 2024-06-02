import streamlit as st
from openai import OpenAI
import time

st.header("open api key를 입력하세요.")
apikey = st.text_input("API Key", type="password")

client = OpenAI(api_key= apikey)

assistant = client.beta.assistants.create(
  name="assistant",
  description="당신은 유능한 비서입니다.",
  model="gpt-4o",
)

thread = client.beta.threads.create(
  messages=[
  ]
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
	new_message = client.beta.threads.messages.create(
	    thread_id = thread.id,
	    role="user",
	    content=prompt
	  )
	run = client.beta.threads.runs.create(
	  thread_id=thread.id,
	  assistant_id=assistant.id
	)
	
	while True:
	  run_check = client.beta.threads.runs.retrieve(
	    thread_id=thread.id,
	    run_id=run.id
	  )
	  run_check
	  if run_check.status not in ['queued','in_progress']:
	    break
	  else:
	    time.sleep(2)	
	thread_messages = client.beta.threads.messages.list(thread.id)
	for msg in thread_messages.data:
	   response = f"Echo: {msg.content[0].text.value}"
	   with st.chat_message("assistant"): 
	      st.markdown(response)
	st.session_state.messages.append({"role": "assistant", "content": response})

	








