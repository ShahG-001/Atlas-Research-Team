# Atlas Research Studio

A modular Streamlit + CrewAI research app using Groq for the LLM and Tavily for web search. The four specialists run sequentially, and Streamlit shows the active stage while it runs.

## Required keys

- `GROQ_API_KEY`: create one in Groq Console.
- `TAVILY_API_KEY`: create one at Tavily. The app uses Tavily's web search API.

In Streamlit Community Cloud, add both keys under **App settings → Secrets**. Do not upload a secrets file.

## Files

- `app.py`: user interface
- `research_team/agents/`: one file per agent
- `research_team/tools/web_search.py`: shared web-search tool
- `research_team/llm.py`: Groq model setup
- `research_team/tasks.py`: one task per research stage
- `research_team/crew.py`: sequential orchestration and live stage status
- `requirements.txt`: deployment dependencies

## Deploy

Upload the contents of this folder to a GitHub repository. In Streamlit Community Cloud, create an app from that repository, set the main file to `app.py`, choose a current supported Python version (3.11 or 3.12), and add the two secrets above. The app installs packages from `requirements.txt`.
