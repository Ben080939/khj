import streamlit as st

st.header("무엇이든 그려보세요.")
prompt2 = st.text_input("명령")

if st.button("start"):
  from openai import OpenAI
  client = OpenAI(api_key= apikey)
  response = client.images.generate(model="dall-e-3",prompt=prompt2)
  image_url = response.data[0].url
  st.markdown(f"![alt text]({image_url})")
