import os

import streamlit as st
from crewai import LLM


def get_llm() -> LLM:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except (FileNotFoundError, KeyError):
            raise RuntimeError(
                "Add GEMINI_API_KEY to your Streamlit Cloud Secrets."
            )

    return LLM(
        model="model="gemini/gemini-2.5-flash",
        api_key=api_key,
        max_output_tokens=1200,
    )
