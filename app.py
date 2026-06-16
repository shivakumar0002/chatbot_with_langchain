# q&a chatbot

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI 
import streamlit as st
import os 


## Function to load OpenAI model and get response

def get_open_ai_response(question):
    if not question or not question.strip():
        return None
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPEN_API_KEY"),
        model="gpt-4o-mini",
        temperature=0.5,
    )
    return llm.invoke(question).content

## initalize our stremlit app

st.set_page_config(page_title="Q&A CHATBOT")

st.header("Ask me anything!")
input=st.text_input("Input: ",key ="input")
response=get_open_ai_response(input)

submit=st.button("Ask a question")

## if ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
