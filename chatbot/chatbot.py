from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_ollama.llms import OllamaLLM

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OLLAMA_API_KEY"] = os.getenv("ollama_api_key")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates to the queries."),
        ("user" , "Question: {question}")
        
    ]
)

##streamlit app 
st.title('ChatBot with LangChain')
input_text = st.text_input('Enter your question here:')


llm = OllamaLLM(
    model="deepseek-r1:8b")

OutputParser = StrOutputParser()

chain = prompt | llm | OutputParser

if input_text:
    st.write(chain.invoke({'question':input_text}))