import streamlit as st

from ui.header import render_header
from ui.sidebar import render_sidebar
from ui.chat import render_chat

st.set_page_config(
    page_title="FAPERN Insight",
    page_icon="🤖",
    layout="wide",
)

render_header()

config = render_sidebar()

render_chat(config)