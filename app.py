import streamlit as st

from research_team.crew import run_research

st.set_page_config(page_title="Atlas · Research Studio", page_icon="✦", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#172520; --muted:#718078; --green:#1f7557; --lime:#d8f28a; --paper:#f5f7f2; }
.stApp { background:var(--paper); color:var(--ink); font-family:'DM Sans',sans-serif; }
[data-testid="stHeader"] { background:transparent; }
.block-container { max-width:1120px; padding-top:2.2rem; padding-bottom:4rem; }
.hero { padding:2.2rem 2.4rem; border-radius:24px; color:white; background:linear-gradient(118deg,#143d30 0%,#1c6248 62%,#43835a 100%); position:relative; overflow:hidden; }
.hero:after { content:'✳'; position:absolute; right:4%; top:-44%; font-size:260px; color:#ffffff12; }
.eyebrow { text-transform:uppercase; letter-spacing:.16em; font-size:.73rem; font-weight:700; color:var(--lime); }
.hero h1 { font:800 clamp(2.2rem,5vw,3.6rem)/1.06 'Manrope',sans-serif; margin:.65rem 0 .75rem; color:white; letter-spacing:-.05em; }
.hero p { color:#d9e8df; font-size:1.05rem; max-width:620px; margin:0; }
.pill { display:inline-block; border:1px solid #ffffff38; border-radius:99px; padding:.38rem .72rem; margin-top:1.3rem; font-size:.78rem; color:#edf6ef; }
.section-title { font:700 1.15rem 'Manrope',sans-serif; margin:.4rem 0 .25rem; }
.subtle { color:var(--muted); font-size:.92rem; }
.agent-card { background:#fff; border:1px solid #e5ebe3; border-radius:16px; padding:1rem 1.1rem; min-height:106px; }
.agent-num { font-size:.72rem; color:var(--green); font-weight:700; letter-spacing:.1em; }
.agent-name { font:700 1rem 'Manrope',sans-serif; margin:.32rem 0 .2rem; }
.agent-desc { color:var(--muted); font-size:.82rem; line-height:1.4; }
div.stButton > button[kind="primary"] { background:#1f7557; border:0; border-radius:12px; min-height:3rem; font-weight:700; }
div.stButton > button[kind="primary"]:hover { background:#185c44; border:0; }
div[data-testid="stTextArea"] textarea { border-radius:14px; border-color:#dce5dc; background:white; }
div[data-testid="stStatusWidget"] { border-radius:14px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">Atlas · Research Studio</div>
  <h1>Good research,<br>from a team that thinks.</h1>
  <p>Ask a question. Four focused AI agents search, verify, analyze, and shape the findings into a clear report.</p>
  <span class="pill">✦ Powered by CrewAI + Groq</span>
</div>
""", unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.35, 1], gap="large")
with left:
    st.markdown('<div class="section-title">What would you like to research?</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">Be specific for a more useful, source-backed report.</div>', unsafe_allow_html=True)
    question = st.text_area("Research question", placeholder="e.g. How are cities adapting to extreme heat, and which approaches have the strongest evidence?", height=125, label_visibility="collapsed")
    run = st.button("Start research  →", type="primary", use_container_width=True)
with right:
    st.markdown('<div class="section-title">Your research team</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">Each specialist has a job and web research tools.</div>', unsafe_allow_html=True)
    st.write("")
    cards = [
        ("01", "Researcher", "Finds current, relevant sources"),
        ("02", "Fact Checker", "Checks claims against evidence"),
        ("03", "Analyst", "Connects findings and caveats"),
        ("04", "Report Writer", "Creates a readable sourced brief"),
    ]
    cols = st.columns(2, gap="small")
    for i, (num, name, desc) in enumerate(cards):
        with cols[i % 2]:
            st.markdown(f'<div class="agent-card"><div class="agent-num">AGENT {num}</div><div class="agent-name">{name}</div><div class="agent-desc">{desc}</div></div>', unsafe_allow_html=True)

if run:
    if not question.strip():
        st.warning("Enter a research question to get started.")
    else:
        st.write("")
        try:
            result = run_research(question.strip())
            st.success("Research complete")
            st.markdown("## Your research brief")
            st.markdown(result)
        except Exception as exc:
            st.error(f"The research run could not finish: {exc}")
            st.caption("Check that GROQ_API_KEY and TAVILY_API_KEY are set in Streamlit Secrets.")

st.divider()
st.caption("Research is AI-generated. Follow the citations and verify important claims with the original sources.")
