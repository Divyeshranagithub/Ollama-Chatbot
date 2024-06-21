from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'Hello! I am a simple chatbot. How can I help you today?'),
        ('user', "Question:{question}"),
    ]
)

st.title('Ollama Chatbot')
input_t = st.text_input('Enter your question here:')

llm=Ollama(model='gemma:2b', base_url="http://ollama-container:11434", verbose=True)
output = StrOutputParser()

chain = prompt|llm|output

if st.button('Submit'):
    st.write(chain.invoke({'question':input_t}))
