"""
Rishky Piano — Streamlit Web App
Interactive piano playable with your MacBook keyboard.
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Rishky Piano",
    page_icon="🎹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome for an immersive feel
st.markdown("""
<style>
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { background: #0b0b14; }
</style>
""", unsafe_allow_html=True)

# Load and embed the piano HTML
piano_html = Path(__file__).parent / "piano.html"
html_content = piano_html.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=900, scrolling=False)
