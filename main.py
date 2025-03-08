from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api.formatters import TextFormatter

import streamlit as st
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

system_prompt = """You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
with heading. Please provide the summary of the text given here:  """
st.header("Youtube Video Summarizer")

url = st.text_input("Enter the URL of the youtube video: ")
    
extra = st.text_input("enter extra instructions here")
system_prompt = system_prompt + extra

    def get_transcript(url):
        video_id = url.split("/")[3]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        final = formatter.format_transcript(transcript)
        st.write("transcript loaded")
        return final

    def get_summary(final):
        prompt = system_prompt + final
        llm = ChatMistralAI(model_name="mistral-large-latest")
        result = llm.invoke(prompt)
        ans = result
        return ans.content

st.write(get_summary(get_transcript(url)))


