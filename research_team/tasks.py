from crewai import Task


def research_task(agent, question: str) -> Task:
    return Task(
        description=(
            "Research this question using your web search tool: {question}\n"
            "Find at most 4 useful findings. Prefer primary/authoritative sources and recent material where relevant. "
            "For every finding, include the source title, URL, and what it supports. Do not make unsupported claims."
        ),
        expected_output="A concise evidence list with source titles, URLs, and relevant excerpts.",
        agent=agent,
    )


def fact_check_task(agent, question: str, evidence: str) -> Task:
    return Task(
        description=(
            "Question: {question}\n\nInitial research to check:\n{evidence}\n\n"
            "Use web search to verify the central claims against independent sources. Mark each claim supported, uncertain, or disputed. "
            "Keep URLs and explain any date or source-quality concerns."
        ),
        expected_output="Brief claim-by-claim verification, caveats, and cited URLs.",
        agent=agent,
    )


def analysis_task(agent, question: str, verified: str) -> Task:
    return Task(
        description=(
            "Question: {question}\n\nVerified research:\n{verified}\n\n"
            "Before writing, use your web search tool at least once to examine a key theme independently. "
            "Identify the strongest conclusions, recurring patterns, meaningful differences, and evidence gaps. "
            "Do not overstate causation or certainty. Keep source URLs beside the relevant findings."
        ),
        expected_output="A concise balanced synthesis with key findings, implications, limitations, and source links.",
        agent=agent,
    )


def writing_task(agent, question: str, analysis: str) -> Task:
    return Task(
        description=(
            "Research question: {question}\n\nAnalysis to turn into a report:\n{analysis}\n\n"
            "Use your web search tool at least once to check a source detail or corroborate a supplied citation. "
            "Write a concise report (about 400 words) in Markdown with: a direct answer, key findings, what remains uncertain, and Sources. "
            "Use clickable Markdown source links supplied in the analysis. Do not introduce facts that are not in the analysis."
        ),
        expected_output="A readable research brief with inline source links and a source list.",
        agent=agent,
    )
