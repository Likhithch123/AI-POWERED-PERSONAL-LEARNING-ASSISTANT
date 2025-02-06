from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st #type: ignore

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt = ChatPromptTemplate.from_messages([('system','act as an, AI-POWERED PERSONALISED LEARNING ASSISTANT'),('human','{input_text}')])

def main():
    st.title('AI-Powered Personalized Learning Assistant')
    input_text = st.text_input('Input your goal and start learning anything you want.')
    if st.button('Response'):
        if input_text:
            chain = prompt|llm
            st.markdown(chain.invoke({'input_text': input_text}).content)


if __name__ == '__main__':
    main()

