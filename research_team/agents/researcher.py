from crewai import Agent

from research_team.tools.web_search import search_web


def make_researcher(llm: object) -> Agent:
    return Agent(
        role="Researcher",
        goal="Find current, relevant evidence and provide source URLs for the user's research question.",
        backstory="You are a careful web researcher. You search broadly, prefer primary and authoritative sources, and keep source links attached to each finding.",
        tools=[search_web],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )
