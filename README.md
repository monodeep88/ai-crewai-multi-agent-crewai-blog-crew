# CrewAI Blog Crew

## Project Overview

CrewAI Blog Crew is a complete full-stack AI project for **CrewAI multi-agent** at **Beginner** difficulty. It includes a FastAPI backend, a React frontend, sample documents, vector search with ChromaDB support, source citations, timeline logs, structured run storage, Docker files, and tests.

This project operates in the content creation and marketing domain, specifically targeting the automation of blog post writing. It leverages AI agents to perform research, strategize content, draft articles, and refine them, simulating a small editorial team. The goal is to produce ready-to-publish blog content efficiently.

Difficulty controls project complexity, architecture depth, AI model selection, and how advanced the generated codebase is.

- Architecture depth: minimal backend, simple folder structure, easy README, low-cost/free model
- Selected architecture: CrewAI Research Operations Crew
- Template path: templates/crewai-multi-agent/crewai-research-operations-crew
- Generated stack: FastAPI backend, React UI, local vector fallback, simple tests
- README style: beginner-friendly setup and clear expected output

## Tech Stack

- Backend: Python, FastAPI, Pydantic, SQLAlchemy
- AI/RAG: LangChain-ready prompt layer, ChromaDB vector storage, local deterministic fallback model
- Workflow: Agent pipeline with planner, retrieval, tool, reasoning, and final answer steps
- Frontend: React and Vite
- Database: SQLite by default, PostgreSQL through Docker Compose
- Testing: pytest
- Difficulty: Beginner

## Generation Method

This project was generated with a template-based architecture engine. AI is used only for the blueprint, domain customization, sample data, prompts, and documentation. The codebase is produced from tested FastAPI/React/Docker templates rather than raw LLM source output.

## Project Type Satisfaction Map

This generated project satisfies **CrewAI multi-agent** through the runtime path below. The implementation is not only a README claim: the files listed after the diagram are generated in the repository and validated before GitHub push.

```text
[User]
  |
  | question / task details / tone / constraints
  v
[React Frontend]
  |
  | POST /api/ask
  v
[FastAPI Backend]
  |
  +--> [Vector Store / Sample Docs]
  |        |
  |        +-- retrieved context / cited sources
  |
  v
[Researcher Agent]
  |
  v
[Analyst Agent]
  |
  v
[Reviewer Agent]
  |
  v
[Final Answer Builder]
  |
  | answer + sources + timeline steps
  v
[React Frontend]
  |
  v
[User sees final output + agent timeline]
```

Runtime proof points:

- `frontend/src/App.jsx` renders the user workspace, starter prompts, answer panel, cited sources, and timeline.
- `backend/app/main.py` exposes `POST /api/ask` and returns the final answer, sources, timeline steps, and project type.
- `backend/app/services/pipeline.py` orchestrates the project-type flow: Researcher Agent, Analyst Agent, Reviewer Agent.
- `backend/app/services/vector_store.py` loads sample documents and retrieves relevant cited context.
- `backend/app/domain.py` contains the generated topic-specific workflow steps, business rules, tools, persona, and starter questions.
- `backend/app/db.py` stores each run so the generated app behaves like a real workflow tool instead of a static prompt demo.
- `backend/tests/test_project_contract.py` validates the API contract and project-type behavior.

Type-specific behavior:

- Flow style: Crew manager -> role agents -> delegated tasks -> reviewer -> final crew output.
- Visible output: final answer, cited sources, timeline steps, and project type.
- Validation gate: pytest, frontend build, Docker Compose config, and Docker build before repository upload.

## Folder Structure

```text
ai-crewai-multi-agent-crewai-blog-crew/
  backend/
app/
  main.py
  config.py
  db.py
  schemas.py
  data/sample_docs/
  services/
text.py
vector_store.py
llm.py
tools.py
pipeline.py
tests/
  test_project_contract.py
requirements.txt
Dockerfile
  frontend/
src/
  App.jsx
  main.jsx
  styles.css
package.json
Dockerfile
  docker-compose.yml
  .env.example
  README.md
  ARCHITECTURE.md
  WHY_THIS_PROJECT.md
  DEPLOYMENT.md
  docs/screenshots/app-preview.svg
```

## Environment Variables

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
USE_CREWAI_RUNTIME=false
PINECONE_API_KEY=
PINECONE_INDEX_NAME=
DATABASE_URL=sqlite:///./app.db
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
VITE_API_URL=http://localhost:8000
```

The app runs without an OpenAI key by using a deterministic local answer model. Add `OPENAI_API_KEY` to use LangChain with OpenAI. For CrewAI projects, set `USE_CREWAI_RUNTIME=true` after installing dependencies to run the live CrewAI Agent/Task/Crew workflow; otherwise the app uses a deterministic CrewAI-shaped fallback.

For Pinecone projects, add `PINECONE_API_KEY` and `PINECONE_INDEX_NAME` to use a live Pinecone index. Without them, the repo still runs using local ChromaDB/local retrieval fallback.

## Installation

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
cd ../frontend
npm install
```

## Run Backend

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

## Run Frontend

```bash
cd frontend
npm run dev
```

## Run With Docker

```bash
docker compose up --build
```

## Example API Request

```bash
curl -X POST http://localhost:8000/api/ask ^
  -H "Content-Type: application/json" ^
  -d "{\"question\": \"What is the refund policy?\"}"
```

## Example User Question

```text
What should I do if a customer asks for a refund without an order id?
```

## Expected Output

The API returns:

- `answer`: a grounded answer generated from retrieved context
- `sources`: cited document chunks with similarity scores
- `steps`: planner, retriever, reasoning, tool-call, and final-answer timeline logs
- `project_type`: `CrewAI multi-agent`

## How The RAG/Agent Flow Works

Crew manager -> role agents -> delegated tasks -> reviewer -> final crew output.

## Project Planner Agent Workflow

User -> React Dashboard -> FastAPI -> Project Planner Agent -> Specialist Agents -> Generated Project -> Auto Testing -> GitHub Repository Creation -> Push Code -> Return GitHub URL

- **Architecture Agent**: Define app boundaries, data flow, runtime stack, and integration points. Outputs: The architecture is designed for a beginner-friendly approach, balancing a full-stack representation with focused complexity. The FastAPI backend is minimal, primarily acting as a wrapper for the CrewAI system. The React frontend provides a simple input form and display area, demonstrating how to interact with an AI service. Docker ensures environmental consistency and ease of deployment, a crucial skill for portfolios. The core complexity is concentrated within the CrewAI agent design and orchestration, making it easy to understand the multi-agent paradigm. This setup offers practical portfolio value by demonstrating skills in AI orchestration, API development, UI integration, and containerization..
- **Backend Agent**: Design FastAPI modules, service contracts, validation, and error handling. Outputs: Crew Orchestrator: Python module containing the CrewAI agents, tasks, and crew definition. Exposes a 'run_crew' function.; FastAPI Endpoints: API routes for 'trigger_blog_generation', 'get_crew_status', and 'get_blog_post'.; Result Storage: Simple mechanism (e.g., in-memory dictionary or basic file storage for a beginner project) to store generated blog posts and their status..
- **Frontend Agent**: Design React screens, state flow, controls, and user feedback states. Outputs: Topic Input Form: A text input field for users to provide the desired blog post topic.; Generate Button: Triggers the CrewAI process via the FastAPI backend.; Status Display: Shows the current stage of the blog generation process (e.g., 'Researching...', 'Drafting...', 'Editing...', 'Completed!').; Blog Post Viewer: Displays the final generated blog post in a readable format.; Error/Success Notifications: Provides feedback to the user on the operation status..
- **Database Agent**: Design persistence models, sample data, indexes, and audit records. Outputs: Run history; Source document metadata; Generated workflow audit records.
- **Testing Agent**: Define contract tests, smoke tests, and generated project validation. Outputs: Unit Tests (Python): Test individual agent tools (e.g., the search tool's functionality) and core utility functions.; Agent Task Tests: Verify that individual agent tasks produce expected outputs given specific inputs (mocked tool responses).; Integration Tests (Crew): Run the entire CrewAI workflow with predefined topics and assert that a blog post is generated, focusing on agent collaboration.; API Tests (FastAPI): Test FastAPI endpoints to ensure they correctly trigger the crew and return appropriate responses.; End-to-End Tests (Playwright/Cypress): Simulate user interaction from topic input to blog post display in the frontend..
- **DevOps Agent**: Define environment variables, Docker workflow, and repository packaging. Outputs: Docker-ready project; Environment sample file; GitHub repository upload.
- **Reviewer Agent**: Review the generated plan for completeness, security, and portfolio quality. Outputs: 1. **User Input:** User provides a blog post topic (e.g., 'The Benefits of Remote Work').; 2. **Research Phase:** The 'Research Analyst' agent uses web search tools to gather relevant information, statistics, and common talking points on the given topic.; 3. **Outline Generation:** The 'Content Strategist' agent takes the research findings and crafts a detailed blog post outline, including main sections, sub-sections, and key points to cover.; 4. **Drafting Phase:** The 'Blog Post Writer' agent uses the outline and research data to generate the first draft of the blog post, focusing on engaging content and clear explanations.; 5. **Review and Refine:** The 'Editor' agent reviews the draft for grammatical errors, clarity, coherence, tone consistency, and overall quality, suggesting improvements.; 6. **Final Output:** The refined blog post is presented to the user through the frontend..

## AI-Customized Domain Workflow

- 1. **User Input:** User provides a blog post topic (e.g., 'The Benefits of Remote Work').
- 2. **Research Phase:** The 'Research Analyst' agent uses web search tools to gather relevant information, statistics, and common talking points on the given topic.
- 3. **Outline Generation:** The 'Content Strategist' agent takes the research findings and crafts a detailed blog post outline, including main sections, sub-sections, and key points to cover.
- 4. **Drafting Phase:** The 'Blog Post Writer' agent uses the outline and research data to generate the first draft of the blog post, focusing on engaging content and clear explanations.
- 5. **Review and Refine:** The 'Editor' agent reviews the draft for grammatical errors, clarity, coherence, tone consistency, and overall quality, suggesting improvements.
- 6. **Final Output:** The refined blog post is presented to the user through the frontend.

## Business Rules

- All generated blog posts must be original and not plagiarized.
- Information must be factual and referenced where appropriate (implicitly handled by LLM synthesis from search results).
- The tone of the blog post should be consistent with the user's request (default to informative if not specified).
- Blog posts should ideally be between 500-1000 words (medium length) unless otherwise specified.
- Output must be in Markdown format for easy readability and integration.

1. The backend loads sample documents from `backend/app/data/sample_docs`.
2. Documents are split into chunks.
3. Chunks are embedded and stored in ChromaDB when available, with a local fallback for development.
4. User questions are matched against relevant chunks.
5. Agent-specific steps run: planner, retriever, tool call, reasoning, reviewer, or graph nodes.
6. The final answer is returned with source citations and a timeline.

## Testing

```bash
cd backend
pytest
```

## Validation Gates Before GitHub Push

The SaaS validates generated projects before creating and pushing the GitHub repository:

- `pytest`
- `npm install`
- `npm run build`
- `docker compose config`
- `docker compose build`

## Portfolio Proof Files

- `WHY_THIS_PROJECT.md`: explains why this repo satisfies the selected project type.
- `ARCHITECTURE.md`: documents the runtime flow, agents/nodes, and validation strategy.
- `DEPLOYMENT.md`: gives Render, Railway, Vercel, and Docker deployment options.
- `docs/screenshots/app-preview.svg`: generated UI preview image for README/profile use.

## Deployment

See `DEPLOYMENT.md` for Render, Railway, Vercel, and Docker deployment steps.
