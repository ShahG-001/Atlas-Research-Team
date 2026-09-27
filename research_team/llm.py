import os

import streamlit as st
from crewai import LLM


def get_llm() -> LLM:
    """Create a CrewAI LLM using Groq's LiteLLM provider interface."""
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is missing from Streamlit Secrets.")
    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0.2,
        max_tokens=1200,
        max_retries=3,
        timeout=90,
    )
