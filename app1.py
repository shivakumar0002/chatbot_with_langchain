## Converstaional q&a

import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#streamlit UI 
st.set_page_config(page_title= "Your conversation AI chatbot about anything you want to know")
st.header("Lets chat!")

from dotenv import load_dotenv
load_dotenv()
import os
chat = ChatOpenAI(temperature=0.1)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a helpful asssistant")
    ]

## Function to load open ai model and get response 

def get_openai_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer= chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ",key ="input")
response=get_openai_response(input)

submit=st.button("ask the question")

## if ask button is called

if submit:
    st.subheader("Response")
    st.write(response)