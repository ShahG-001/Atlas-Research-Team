from crewai import Agent

from research_team.tools.web_search import search_web


def make_report_writer(llm: object) -> Agent:
    return Agent(
        role="Research Report Writer",
        goal="Write a clear, concise, well-structured report that preserves source links and caveats.",
        backstory="You are an editor of evidence-based research briefs. You use the supplied verified findings, cite sources as Markdown links, and do not add unsupported facts.",
        tools=[search_web],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
