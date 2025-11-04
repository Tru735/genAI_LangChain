from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key")
os.environ["OLLAMA_API_KEY"] = os.getenv("ollama_api_key")

app = FastAPI(
    title = "LangChain Ollama ChatBot API",
    description = "An API for a ChatBot using LangChain and Ollama",
    version="1.0.0"
)

add_routes(
    app,
    OllamaLLM(model="deepseek-r1:8b"),
    path="/deepseek-chatbot"
)

dpsModel = OllamaLLM(model="deepseek-r1:8b")
qwenModel = OllamaLLM(model="qwen3:4b")

prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} in English in about 100 words.")

prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic} in English in about 50 words.")

add_routes(
    app,
    prompt1 | dpsModel,
    path="/essay"
)

add_routes(
    app,
    prompt2 | qwenModel,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    