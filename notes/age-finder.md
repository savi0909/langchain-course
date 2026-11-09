# AgeFinder

Run `uv run python age_finder.py` with `GOOGLE_API_KEY` in the project's `.env`.
Try asking: `How old was Ada Lovelace when she died?` The expected answer is 36.
The mock lookup only knows Ada Lovelace; it does not search the internet.

`bind_tools` describes the available tool to Gemini; it does not run the tool.
Our `for` loop calls the model explicitly. Gemini can request the separate
`lookup_birth_date` and `lookup_death_date` tools. Our code runs each requested
tool and appends a `ToolMessage` containing its result and matching tool-call ID.
Gemini may request both tools in one model call or across multiple calls. The next
model call receives the full conversation.
If no tool is requested, the model's text is the answer. The loop stops after
five model calls if no final answer arrives.
