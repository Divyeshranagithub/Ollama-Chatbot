# 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
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

st.title('Langchain ollama chatbot')
input_t = st.text_input('Enter your question here:')

llm=Ollama(model='gemma:2b') 
output = StrOutputParser()

chain = prompt|llm|output

if st.button('Submit'):
    st.write(chain.invoke({'question':input_t}))