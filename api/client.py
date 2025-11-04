import requests
import streamlit as st 

def get_deepseek_response(input_text): 
    response = requests.post('http://localhost:8000/essay/invoke', json={'input':{'topic' : input_text}})
    data = response.json()
    return data['output']

def get_qwen_response(input_text): 
    response = requests.post('http://localhost:8000/poem/invoke', json={'input':{'topic': input_text}})
    
    return response.json()['output']


st.title('ChatBot with LangChain API')
input_text1 = st.text_input('Enter your essay topic here:')
input_text2 = st.text_input('Enter your poem topic here:')

if input_text1:
    st.write(get_deepseek_response(input_text1))
    
if input_text2:
    st.write(get_qwen_response(input_text2))