from crewai import Agent

from research_team.tools.web_search import search_web


def make_analyst(llm: object) -> Agent:
    return Agent(
        role="Research Analyst",
        goal="Synthesize the verified evidence into findings, patterns, implications, and limitations.",
        backstory="You turn several sources into a balanced analysis. You distinguish strong evidence from tentative interpretation and retain citations.",
        tools=[search_web],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=4,
    )
