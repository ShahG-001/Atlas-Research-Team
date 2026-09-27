from crewai import Agent

from research_team.tools.web_search import search_web


def make_fact_checker(llm: object) -> Agent:
    return Agent(
        role="Fact Checker",
        goal="Check important research claims against independent web sources and flag uncertainty or disagreement.",
        backstory="You are skeptical and precise. Verify claims rather than repeating them, look for dates and source quality, and never invent citations.",
        tools=[search_web],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )
