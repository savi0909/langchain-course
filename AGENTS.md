# LangChain course workspace

This workspace supports Abhishek's study of Eden Marco's Udemy course at
https://www.udemy.com/course/langchain/.
The local course repository is `D:/AA-PYTHON/langchain-course`.
Preferred exercise branch: `project/hello-world` (selected by the user on 2026-11-08).
`main` is the course index; use `project/hello-world` for Hello World study. Inspect the actual branch before acting; do not switch branches automatically on startup.

## Start of each session

1. Read `PROJECT_CONTEXT.md` for course identity and scope.
2. Read `memory/STATE.md` for the current checkpoint, decisions and questions.
3. Inspect relevant local files before assuming code, dependencies or progress exist.
4. At course orientation, check the working tree in `D:/AA-PYTHON/langchain-course`, safely use `main`, and review its README. It was already on `main` when reviewed on 2026-11-08. Runnable examples live on project branches or in separate repositories. For subsequent exercises, use the branch appropriate to the user's task; do not reset an active exercise to `main` automatically. Preserve uncommitted changes; never force a checkout or discard work.

## Working approach

- Study mode chosen 2026-11-08: teach from first principles while the user also learns Python. Follow `LEARNING_PLAN.md` sequentially, one small lesson at a time. Explain new syntax and motivation, demonstrate a small example, then invite one prediction or exercise. Check understanding before advancing; do not infer mastery from an explanation alone.

- Help with course concepts, exercises, debugging and implementation in the context of the user's current request.
- Use Google Gemini for this user's examples, through `langchain-google-genai` / `ChatGoogleGenerativeAI`. Current Hello World model: `gemini-3.5-flash-lite`. Load `GOOGLE_API_KEY` from local `.env`; no OpenAI key is required. `LLM_PROVIDER` is not read by the example. Print `response.text` for readable output. OpenAI/Ollama packages are optional and are still declared until explicitly removed.
- Follow the lecture or supplied material when available. Distinguish course examples from optional extensions and current library changes.
- Do not infer completed lectures, proficiency, enrollment, repository URLs or installed versions.
- Verify version-sensitive API guidance against installed dependencies and official framework documentation when needed.
- Keep explanations tied to the current concept; preserve any study mode explicitly chosen by the user.
- This setup provides context and memory only. Create code and install dependencies when the user requests implementation or environment setup.

## Persistent memory

- At meaningful stopping points, update `memory/STATE.md` with confirmed progress, relevant files, decisions, unresolved questions and one concrete next step.
- Record the date and basis for important facts. Label proposals and unknowns explicitly.
- Keep the current checkpoint concise; retain useful historical decisions beneath it.
- Save reusable course notes under `notes/` as they are produced. Use `work/` for temporary files.
- Never store API keys, passwords, tokens or raw private transcripts in memory; record only variable names or safe setup instructions.
- These files provide workspace-local continuity; do not claim account-wide saved memory has changed.
- Maintain identical master copies of `AGENTS.md`, `PROJECT_CONTEXT.md`, `LEARNING_PLAN.md` and `memory/STATE.md` on local `main` and `project/hello-world`, as requested on 2026-11-08. Synchronize documentation changes to both branches while preserving unrelated source changes. This is a manual synchronization convention, not an automatic background job; do not claim later edits synchronize themselves. Do not copy exercise source onto `main` as part of documentation synchronization.

## Windows coexistence

- Preserve inherited user-wide operating instructions.
- Use filesystem, shell and service APIs. Do not control desktop applications, send simulated input, take focus or open visible automation without explicit authorization for the current task.
- Keep disabled desktop integrations disabled. Stop and verify cleanup of task-owned automation before ending a task.

## File location rule

- Keep all course source code, context, memory, notes and temporary project files under `D:/AA-PYTHON/langchain-course` only.
- If a copy or move destination is unclear, ask the user for the exact destination path before writing. Do not use the generated Codex chat directory for project files.
