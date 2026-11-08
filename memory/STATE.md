# Course memory

Last updated: 2026-11-08 (Asia/Calcutta).

## Current checkpoint

- Context and file-based memory initialized for Eden Marco's Udemy LangChain course.
- Current lecture / section: unknown.
- Completed course work: not reported.
- Code repository: `D:/AA-PYTHON/langchain-course` (user-provided).
- Preferred exercise branch: `project/hello-world`, selected by the user on 2026-11-08; baseline commit `2ea5ad8`. `main` remains the course index. This shared memory describes both branches; inspect Git for the actual checkout state.
- README: `main` course index previously reviewed at `0880469`; Hello World branch README is empty.
- Hello World source: `main.py` contains a person-summary chain using ChatGoogleGenerativeAI with `gemini-3.5-flash-lite`. Unused OpenAI/Ollama imports were removed. User supplied successful Gemini output; assistant checks were offline only.
- Project declarations: Python >=3.11; `.python-version` is 3.11; dependency lower bound LangChain >=0.3.27. Installed versions remain unverified.
- Local branches observed: `main`, `project/hello-world`.
- Environment: `.venv` synchronized with `uv sync --locked`; imports and model/chain construction passed offline checks. Exact installed versions are not recorded. `.env` remains ignored; `.idea/` is untracked. No key values are stored here.
- Blockers: none for context setup; lecture information is needed to identify where to resume study.
- Study mode: first principles, Python learner, sequential lessons with a small example and one understanding check before advancing.
- Provider preference: Google Gemini; user already has a Gemini API key and no OpenAI key. User subsequently authorized the source update. Uses `GOOGLE_API_KEY` loaded through dotenv; no secret values read or stored in this task.
- Configuration: `LLM_PROVIDER` is not read. `response.text` prints readable text. If both key aliases exist, Hello World removes `GEMINI_API_KEY` only from its own process when `GOOGLE_API_KEY` is nonempty. `.env` has a `GOOGLE_API_KEY` entry; persistent environment settings are unchanged.
- Dependencies: OpenAI/Ollama integrations are still declared but unused; removal has not been performed.
- Master documentation: keep these four files identical on local `main` and `project/hello-world`: `AGENTS.md`, `PROJECT_CONTEXT.md`, `LEARNING_PLAN.md`, `memory/STATE.md`. Synchronization is manual, with no background job or automatic push.
- Plan: `LEARNING_PLAN.md`; Python foundations added before the README Learning Path.
- Current tutoring step: 0, lesson 1 (program execution, values, assignment and print); introduced, understanding not yet assessed.
- Next step: review the learner's prediction for the assignment example, then adjust the Python starting level.

## Confirmed decisions

| Date | Decision | Basis |
| --- | --- | --- |
| 2026-11-08 | Use the course repository for the Eden Marco course linked in project context. | User request |
| 2026-11-08 | Check out `main` safely and review the course repository README before implementation. | User's additional note |
| 2026-11-08 | Use `D:/AA-PYTHON/langchain-course`; `main` orientation and README review completed. | User-provided path and local inspection |
| 2026-11-08 | Keep durable context in `PROJECT_CONTEXT.md`, with a resumable checkpoint here and a root `AGENTS.md` entry point. | Setup implementation |

## Open questions

- Which lecture or section is the user currently studying?
- Prior programming experience beyond learning Python is unknown.

## Session history

- 2026-11-08: User requested identical master context on `main` and `project/hello-world`, emphasizing Gemini instead of OpenAI. Updated all four master files to describe Gemini, current output/key handling, optional integrations and shared branch policy. Documentation is synchronized independently of the uncommitted Hello World source/dependency changes.

- 2026-11-08: User reported a successful Gemini run with a duplicate-key warning and raw content blocks. Changed `print(response.content)` to `print(response.text)`. After dotenv loading, the program drops the redundant `GEMINI_API_KEY` alias from its own process when `GOOGLE_API_KEY` is nonempty, preserving SDK precedence and Gemini-only fallback without changing the user's persistent environment or `.env`. Offline checks passed for both-key selection, Gemini-only fallback, string responses and structured text blocks. No live API request made for this fix. An initial check cleared Windows system environment variables and failed SSL initialization; preserving those variables corrected the test harness.

- 2026-11-08: Updated the Hello World source to Gemini at the user's request. Preserved pre-existing Gemini manifest/lockfile changes. `uv sync --locked`, offline Python syntax/import/model/chain construction, and `git diff --check` passed. Used a dummy key for constructor verification; no API calls or live credential checks. Changes remain uncommitted.

- 2026-11-08: Interpreted "Hello Test World" as the existing `project/hello-world` branch and switched safely. Preserved all context files and existing local files. Reviewed the empty branch README, Python version declaration, dependency manifest and source without reading secrets or executing the app. Saved context and plan as a local branch commit; no push requested.

- 2026-11-08: User requested first-principles teaching while learning Python and following a step-by-step plan. Saved the tutoring plan and study mode. Begin Python foundations before Hello World, preserving the README's explicit Learning Path project order.

- 2026-11-08: User supplied `D:/AA-PYTHON/langchain-course`. Confirmed it was already on `main` and reviewed README at `0880469`. Recorded project-branch workflow, mixed version references and preserved untracked files. No branch switch, dependency installation or code execution was necessary.

- 2026-11-08: Saved the user's `main` checkout and README review instruction. Verified that this workspace has no Git repository or README. Repository identification was pending at that point; subsequently resolved below in the repository records.

- 2026-11-08: Verified course identity from its public Udemy page. Created project instructions, context and memory. No lecture completion or runtime setup is implied.

## Future checkpoint updates

Record the exact lecture, relevant file paths, observed results, verified understanding
or unresolved confusion, and the next concrete step. Do not mark a topic mastered just
because it was explained, or mark an exercise complete without evidence.

## File ownership and location — 2026-11-08

- Canonical project root: `D:/AA-PYTHON/langchain-course`.
- Moved `AGENTS.md`, `PROJECT_CONTEXT.md`, `LEARNING_PLAN.md` and `memory/STATE.md` into the project root structure; removed their original copies through verified file moves.
- User instruction: create project source code, memory and context files only inside this project folder. Ask clearly for the exact destination if a future copy location is ambiguous.
- Tutoring remains at Step 0, lesson 1; no answer to the prediction exercise has been supplied.
