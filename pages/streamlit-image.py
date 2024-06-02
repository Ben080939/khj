import streamlit as st
from openai import OpenAI


st.header("무엇이든 그려보세요.")
prompti = st.text_input("명령")

if 'prompt' not in st.session_state: 
    st.session_state.prompt = prompti

@st.cache_data()
def draw(prompt):
    client = OpenAI(api_key= st.session_state.key)
    response = client.images.generate(model="dall-e-3",prompt=prompt)
    image_url = response.data[0].url
    image = f"![alt text]({image_url})"
    return image
  


if st.button("start"):
  img = draw(prompti)
  st.markdown(img)
