# Step-by-step learning plan

Created: 2026-11-08. Mode: first-principles instruction with Python taught alongside the course.

## Basis and sequence

The user requested sequential study and is also learning Python. This plan adds a
Python prerequisite stage to the README's explicit Learning Path, then teaches
additional Python concepts as each project needs them. It is a tutoring adaptation,
not a claim to reproduce the complete Udemy lecture order. The README's project
table and Learning Path differ; use its Learning Path for now and reconcile with
the current Udemy lecture when supplied.

Source reviewed locally: `D:/AA-PYTHON/langchain-course/README.md`, main at `0880469`.

| Step | Focus | Python and underlying ideas | Checkpoint |
| --- | --- | --- | --- |
| 0 | Python foundations | Running a program; values, names, strings, numbers; expressions; print; lists and dictionaries; conditions, loops and functions | Explain and write a small function that transforms input into output |
| 1 | Environment and Hello World Chain | Interpreter, project dependencies, virtual environments, imports, environment variables; API request/response; prompt, model and result | Trace a simple model call and explain each line, including new syntax |
| 2 | Code Interpreter | Function arguments, return values, type hints, basic classes, exceptions; tool schemas and the agent tool loop; boundaries around executing generated code | Explain how a requested tool becomes a Python function call and its result returns to the model |
| 3 | Ice Breaker / search application | Modules, structured data, JSON, HTTP, validation and structured outputs | Trace external data from retrieval through model output |
| 4 | Documentation Helper | Files, text processing and collections; chunks, embeddings, similarity, retrieval and RAG | Explain indexing separately from answering a question, and trace a retrieved passage |
| 5 | Blog Analyzer | Multi-step transformations, intermediate results, failure handling and debugging | Explain each processing stage and diagnose a failed stage |
| 6 | Agentic RAG | State, nodes, edges, routing, loops and stopping conditions; LangGraph; retrieval decisions and correction | Trace a graph execution and explain why it chooses its next step |
| 7 | Further course topics | Reflection, Reflexion, MCP and other topics as their actual lectures are reached | Add a small example and an explanation of each new mechanism |

Steps 1–6 preserve the README's named Learning Path order. Step 0 is added Python
preparation; step 7 groups additional topics for later reconciliation. The README
also links a Modern Search Agent; confirm the current lecture before selecting its
repository or treating it as the Ice Breaker implementation.

## Lesson rhythm

Provider throughout this plan: **Google Gemini**, using `ChatGoogleGenerativeAI`
from `langchain-google-genai`. Start with `gemini-3.5-flash-lite` and
`GOOGLE_API_KEY` in local `.env`; an OpenAI key is unnecessary. Teach dotenv,
imports, model construction, prompt composition, `invoke`, and `response.text`
incrementally. `LLM_PROVIDER` is not currently used. OpenAI and Ollama are optional
alternatives, not prerequisites. The user has already demonstrated a successful
Gemini call; this does not establish understanding of the Python or chain.

1. State one concrete goal and why it matters.
2. Explain the mechanism from familiar concepts; define each new term.
3. Walk through a small example and explain unfamiliar Python syntax.
4. Ask one prediction, short exercise or explanation in the user's own words.
5. Review the response and resolve confusion before advancing.
6. Record the checkpoint and next step in `memory/STATE.md`.

Keep lessons short. Do not front-load all of Python or large completed applications.
Introduce advanced syntax only when needed. Existing programming knowledge is
unknown; adapt after the learner's first responses.

## Current lesson

Step 0, lesson 1: a Python program executes instructions; values can be bound to
names; assignment evaluates the right-hand side before binding the left-hand name.
Demonstrate with a number and `print`, then ask for a prediction. No code execution
or mastery is claimed until observed.

## Repository practice

Preferred exercise branch: `project/hello-world`, chosen on 2026-11-08. Its source is available
for study, but Python foundations remain the current lesson until the user is
ready to advance. Review `main.py` incrementally when introducing Hello World;
the branch README is empty. The branch requires Python >=3.11, which takes
precedence over the course index's general Python 3.10+ prerequisite.

Orientation on `main` and README review are complete. Inspect the appropriate project
branch and dependencies when beginning a project. Preserve untracked `.env` and
`.idea/`; never display secrets. Avoid dependency installation and paid model calls
until they serve the current lesson. No desktop automation is needed.

This plan and the other three master context files must have identical committed
contents on local `main` and `project/hello-world`. Synchronize future documentation
updates deliberately; source code and dependency manifests remain branch-specific.
