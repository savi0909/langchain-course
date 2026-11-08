# Eden Marco LangChain course

Initialized: 2026-11-08 (Asia/Calcutta).

## Confirmed identity

- User: Abhishek.
- Course: **LangChain & LangGraph AI Engineer: Agents, Agentic RAG & MCP**.
- Instructor: Eden Marco.
- Platform: Udemy.
- Source: https://www.udemy.com/course/langchain/ (public course page checked 2026-11-08).
- The user identified this course and requested project context and memory through Codex.

## Course scope

The public description covers Python-based LangChain applications, tool-calling agents,
agent loops, RAG and agentic retrieval, LangGraph workflows, MCP servers and clients,
and LangSmith tracing. These are course topics, not a record of completed study.

## Workspace purpose

Study mode: teach from first principles while learning Python, following
`LEARNING_PLAN.md` sequentially. Explain new syntax and check understanding one
small lesson at a time. This is a tutoring adaptation of the README path with
Python prerequisites added, not a verified transcript of Udemy's lecture sequence.

Keep course discussions, implementation context, notes, decisions and progress together
so future Codex sessions in this workspace can resume with relevant context.

## File map

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Instructions for Codex sessions in this workspace |
| `PROJECT_CONTEXT.md` | Stable course identity and workspace scope |
| `memory/STATE.md` | Current checkpoint, confirmed decisions and next step |
| `notes/` | Course notes, created when needed |
| `work/` | Scratch files and intermediate work |

## Gemini configuration and validation

Provider preference (2026-11-08): the user has a Google Gemini API key and no
OpenAI key. Use Gemini for course examples when implementation is requested.
No key values were requested or stored. `main.py` now uses ChatGoogleGenerativeAI
with `gemini-3.5-flash-lite` and loads `GOOGLE_API_KEY` through dotenv. The existing
Gemini dependency and lockfile changes were preserved; `uv sync --locked` passed.
Offline syntax, import, model construction and chain construction checks passed.
The user supplied successful Gemini output, confirming a working call in their
environment. The assistant has only performed offline checks. Display now uses
`response.text` to omit structured block metadata. When both key aliases are set,
the application retains `GOOGLE_API_KEY` and removes the redundant alias only
from its process environment, avoiding the SDK warning. Persistent key settings
are unchanged. Offline verification covered both key configurations and output formats.

Preferred exercise branch: `project/hello-world`, selected at the user's request
on 2026-11-08 (the user called it "Hello Test World"). Baseline commit: `2ea5ad8`.
These four master documents are maintained identically on local `main` and
`project/hello-world`: `AGENTS.md`, `PROJECT_CONTEXT.md`, `LEARNING_PLAN.md`, and
`memory/STATE.md`. Check the actual branch rather than treating this shared
document as evidence of checkout state. Synchronization is manual; no background
automation or push is implied. Source code remains specific to its project branch.
Its README is empty. `main.py` contains a person-summary chain using a prompt
template and ChatGoogleGenerativeAI; unused OpenAI and Ollama imports were removed.
`pyproject.toml` requires Python >=3.11 and declares LangChain >=0.3.27;
`.python-version` specifies 3.11. These are file declarations, not verified runtime
versions. Dependencies have been synchronized; the user has run the application
successfully. No live model call was made by the assistant.

`LLM_PROVIDER` is not used by this example. `langchain-openai` and
`langchain-ollama` are still listed in the Hello World manifest, but are not used
by the current source. Ollama is an optional local-model alternative; neither
integration is required for Gemini. Removal was explained but not performed.

## Course orientation and remaining unknowns

User instruction added 2026-11-08: safely check out the course repository's `main`
branch and review its README. Repository: `D:/AA-PYTHON/langchain-course`.
Verified on 2026-11-08: already on `main`, tracking `origin/main`, at commit
`0880469`. README reviewed from local disk. All project files now belong in this repository.

Current lecture, completed sections and exact installed package versions are
not recorded. A `.venv` exists and offline imports/construction checks passed.
Paid lecture contents and personal Udemy progress were not accessed.

## README review — 2026-11-08

- `main` contains the course index, license and static assets, rather than a runnable Python project.
- The README directs learners to project branches, starting with `project/hello-world`, or to external repositories for other applications. Local branches observed: `main` and `project/hello-world`.
- Branch-specific setup uses `uv sync` and `uv run python main.py`; follow the selected project's actual files before running commands.
- Prerequisites listed: Python 3.10+, basic Python/Git knowledge and an LLM provider or local model. These are README requirements, not verified local capabilities.
- The README mixes v1.0+ and v0.3+ LangChain references and inconsistent project counts; use the relevant project dependency files for version decisions.
- Untracked `.env` and `.idea/` entries were observed and preserved. `.env` contents were not read. Do not stage secrets or assume an existing environment is configured.

## How to resume

In a session using this workspace, say **Continue the LangChain course** and provide
the current lecture or exercise if it has not yet been recorded. Codex should read the
checkpoint, inspect relevant files and update memory as substantive work is completed.

The workspace instruction entry point follows the
[official AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Memory is maintained in local files; this setup does not alter account-wide saved memory.

## Canonical file location

All source code, context, learning plans, memory and notes must stay under
`D:/AA-PYTHON/langchain-course`. Context files were moved here from the generated
chat directory on 2026-11-08 at the user's request. If a future destination is
unclear, ask for the exact path before copying. No parallel memory copy is maintained
in the chat directory.
