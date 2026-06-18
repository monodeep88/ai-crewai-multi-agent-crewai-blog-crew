import os


try:
    from crewai import Agent
    from crewai import Crew
    from crewai import Process
    from crewai import Task

    CREWAI_AVAILABLE = True
except Exception:
    Agent = None
    Crew = None
    Process = None
    Task = None
    CREWAI_AVAILABLE = False


def _fallback_crew(question: str, context: list[str], tools: list[dict[str, str]]) -> dict[str, object]:
    context_preview = " ".join(context[:2]) or "No retrieved context was available."
    tool_names = ", ".join(tool.get("name", "tool") for tool in tools[:3]) or "research checklist"
    return {
        "answer": (
            "CrewAI deterministic fallback output. "
            f"Researcher reviewed the available context: {context_preview} "
            f"Analyst connected the evidence to the question: {question}. "
            f"Reviewer checked gaps and suggested tools: {tool_names}."
        ),
        "steps": [
            {"step": "crewai_manager", "detail": "Scoped the user request and prepared the crew task list."},
            {"step": "crewai_researcher", "detail": "Reviewed retrieved context and extracted relevant evidence."},
            {"step": "crewai_analyst", "detail": "Compared evidence, question intent, and available domain tools."},
            {"step": "crewai_reviewer", "detail": "Challenged weak assumptions and prepared the final crew output."},
        ],
        "runtime": "deterministic-fallback",
    }


def build_crewai_crew() -> object | None:
    if not CREWAI_AVAILABLE:
        return None

    researcher = Agent(
        role="Researcher",
        goal="Find the most relevant evidence for the user's request.",
        backstory="A careful research agent that extracts useful facts from retrieved project documents.",
        allow_delegation=False,
        verbose=True,
    )
    analyst = Agent(
        role="Analyst",
        goal="Compare evidence, workflow rules, and tool outputs to produce a practical answer.",
        backstory="A structured analyst that turns research notes into clear recommendations.",
        allow_delegation=False,
        verbose=True,
    )
    reviewer = Agent(
        role="Reviewer",
        goal="Challenge weak claims and make the final answer safer and more complete.",
        backstory="A quality reviewer focused on missing evidence, unsupported assumptions, and next actions.",
        allow_delegation=False,
        verbose=True,
    )

    research_task = Task(
        description="Review the provided context and identify the facts that matter for: {question}",
        expected_output="Research notes with the most relevant facts and source limitations.",
        agent=researcher,
    )
    analysis_task = Task(
        description="Use the research notes and domain tools to answer: {question}",
        expected_output="A practical answer with reasoning and recommended next steps.",
        agent=analyst,
        context=[research_task],
    )
    review_task = Task(
        description="Review the answer for unsupported claims, gaps, and missing assumptions.",
        expected_output="Final answer with reviewer notes.",
        agent=reviewer,
        context=[analysis_task],
    )

    return Crew(
        agents=[researcher, analyst, reviewer],
        tasks=[research_task, analysis_task, review_task],
        process=Process.sequential,
        verbose=True,
    )


def run_crewai_crew(question: str, context: list[str], tools: list[dict[str, str]]) -> dict[str, object]:
    use_live_crewai = os.getenv("USE_CREWAI_RUNTIME", "").lower() in {"1", "true", "yes"}
    if not use_live_crewai:
        return _fallback_crew(question, context, tools)

    crew = build_crewai_crew()
    if crew is None:
        return _fallback_crew(question, context, tools)

    try:
        context_text = "\n\n".join(context[:4])
        tool_text = ", ".join(f"{tool.get('name')}: {tool.get('description')}" for tool in tools[:4])
        output = crew.kickoff(inputs={"question": question, "context": context_text, "tools": tool_text})
        return {
            "answer": str(output),
            "steps": [
                {"step": "crewai_runtime", "detail": "Executed CrewAI Agent, Task, Crew, and Process.sequential workflow."}
            ],
            "runtime": "crewai",
        }
    except Exception as exc:
        fallback = _fallback_crew(question, context, tools)
        fallback["steps"].insert(0, {"step": "crewai_runtime_fallback", "detail": f"CrewAI runtime unavailable: {exc}"})
        return fallback
