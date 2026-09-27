import os

import streamlit as st
from crewai.tools import tool
from tavily import TavilyClient


@tool("Search the web with Tavily")
def search_web(query: str) -> str:
    """Search the web for trustworthy, relevant information and return source titles, URLs, and excerpts."""
    api_key = os.getenv("TAVILY_API_KEY") or st.secrets.get("TAVILY_API_KEY", "")
    if not api_key:
        raise RuntimeError("TAVILY_API_KEY is missing from Streamlit Secrets.")
    client = TavilyClient(api_key=api_key)
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=3,
        include_answer=False,
        include_raw_content=False,
    )
    results = response.get("results", [])
    if not results:
        return "No web results found. Try a more specific query."
    return "\n\n".join(
        f"Title: {item.get('title', 'Untitled')}\nURL: {item.get('url', '')}\nExcerpt: {item.get('content', '')}"
        for item in results
    )
