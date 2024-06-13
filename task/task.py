import streamlit as st
from openai import OpenAI

def draw(prompt):
    response = client.images.generate(model="dall-e-3",prompt= prompt)
    image_url = response.data[0].url
    image = f"![alt text]({image_url})"
    return image

apikey = st.text_input("api key를 입력하세요", type="password") 

client = OpenAI(api_key=apikey)

st.header("음식 메뉴 추천")
prompti = st.text_input("키워드")

if st.button("start"):
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'{prompti}와 관련된 음식 한가지를 추천해줘'},
      ]
    )
    r = response.choices[0].message.content
    st.markdown(r)
    img = draw(r)
    st.markdown(img)

if st.button("맛집 추천"):
    assistant = client.beta.assistants.create(
      instructions="당신은 유능한 비서입니다.",
      model="gpt-4-turbo-preview",
      tools=[{"type": "file_search"}],
      tool_resources={
          "file_search":{
              "vector_store_ids": [vector_store.id]
          }
      }
    )
    
    thread = client.beta.threads.create(
      messages=[
        {
          "role": "user",
          "content": f'{r}을 하는 식당을 첨부된 파일에서 추천해줘',
          #"attachments": [{"file_id": message_file.id, "tools":[{"type":"file_search"}}]
        }
      ]
    )
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    thread_messages = client.beta.threads.messages.list(thread.id, run_id=run.id)
    
    for msg in thread_messages.data:
      st.markdown(f"{msg.role}: {msg.content[0].text.value}")





    

