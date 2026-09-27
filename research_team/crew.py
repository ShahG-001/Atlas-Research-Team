import streamlit as st
from crewai import Crew, Process

from research_team.agents.analyst import make_analyst
from research_team.agents.fact_checker import make_fact_checker
from research_team.agents.report_writer import make_report_writer
from research_team.agents.researcher import make_researcher
from research_team.llm import get_llm
from research_team.tasks import analysis_task, fact_check_task, research_task, writing_task


def _run_stage(agent, task, inputs: dict, status, label: str) -> str:
    status.update(label=f"Working now: {label}", state="running")
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff(inputs=inputs)
    status.write(f"✓ {label} complete")
    return str(result)


def run_research(question: str) -> str:
    llm = get_llm()
    researcher = make_researcher(llm)
    fact_checker = make_fact_checker(llm)
    analyst = make_analyst(llm)
    writer = make_report_writer(llm)

    with st.status("Preparing your research team…", expanded=True) as status:
        evidence = _run_stage(
            researcher, research_task(researcher, question), {"question": question}, status, "Researcher · searching the web"
        )
        verified = _run_stage(
            fact_checker, fact_check_task(fact_checker, question, evidence),
            {"question": question, "evidence": evidence}, status, "Fact Checker · verifying claims"
        )
        analysis = _run_stage(
            analyst, analysis_task(analyst, question, verified),
            {"question": question, "verified": verified}, status, "Analyst · synthesizing evidence"
        )
        report = _run_stage(
            writer, writing_task(writer, question, analysis),
            {"question": question, "analysis": analysis}, status, "Report Writer · drafting your brief"
        )
        status.update(label="Research complete", state="complete", expanded=False)
    return report
