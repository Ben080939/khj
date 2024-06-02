import streamlit as st
from openai import OpenAI
import time
import json

st.header("open api key를 입력하세요.")
apikey = st.text_input("API Key", type="password")

client = OpenAI(api_key= apikey)

tools = [
    {
        "type":"function",
        "function": {
            "name":"create_image_dalle",
            "description":"Dall-E를 이용해 이미지를 생성하고 이미지 파일 이름을 반환.",
            "parameters": {
                "type":"object",
                "properties": {
                    "prompt": {"type":"string", "description":"image generation prompt"}
                }
            }
        }
    }
]

assistant = client.beta.assistants.create(
    instructions = "당신은 미술 선생님입니다",
    model = "gpt-4-turbo",
    tools = tools
)
thread = client.beta.threads.create(
  messages=[
    {
        "role":"user",
        "content": "만약 사용자가 이미지 생성을 요청하면 해당 주제를 이용해 DALL-E 이미지를 생성해줘: 눈부신 아침의 백사장. 응답은 json만으로 해줘: {'filename':output_file_name}"
    }
  ]
)

def wait_run(client, run, thread):
  while True:
    run_check = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
    print(run_check.status)
    if run_check.status in ['queued','in_progress']:
      time.sleep(2)
    else:
      break
  return run_check

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
	run_check = wait_run(client, run, thread)
	
	if run_check.status == 'requires_action':
	  tool_calls = run_check.required_action.submit_tool_outputs.tool_calls
	  tool_outputs = []
	  for tool in tool_calls:
	    func_name = tool.function.name
	    kwargs = json.loads(tool.function.arguments)
	    output = locals()[func_name](**kwargs)
	    tool_outputs.append(
	        {
	            "tool_call_id":tool.id,
	            "output":str(output)
	        }
	    )
	  run = client.beta.threads.runs.submit_tool_outputs(
	    thread_id=thread.id,
	    run_id=run.id,
	    tool_outputs=tool_outputs
	  )
	  run_check = wait_run(client, run, thread)

	thread_messages = client.beta.threads.messages.list(thread.id)
	for msg in thread_messages.data:
	   response = f"Echo: {msg.content[0].text.value}"
	   with st.chat_message("assistant"): 
	      st.markdown(response)
	st.session_state.messages.append({"role": "assistant", "content": response})



if st.button("clear"):
	client.beta.threads.delete(thread.id)
	thread = client.beta.threads.create(
	  messages=[
	    {
	        "role":"user",
	        "content": "만약 사용자가 이미지 생성을 요청하면 해당 주제를 이용해 DALL-E 이미지를 생성해줘: 눈부신 아침의 백사장. 응답은 json만으로 해줘: {'filename':output_file_name}"
	    }
	  ]
	)

if st.button("대화창 나가기"):
	client.beta.threads.delete(thread.id)
	client.beta.assistants.delete(assistant.id)
	



	
