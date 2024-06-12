import streamlit as st
from openai import OpenAI

apikey = st.text_input("api key를 입력하세요", type="password") 

st.header("음식 메뉴 추천")
prompti = st.text_input("키워드")


response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
r = response.choices[0].message.content
st.markdown(r)

@st.cache_data()
def draw(prompt):
    client = OpenAI(api_key=apikey)
    response = client.images.generate(model="dall-e-3",prompt= prompt)
    image_url = response.data[0].url
    image = f"![alt text]({image_url})"
    return image
    
if st.button("start"):
  img = draw(r)
  st.markdown(img)
