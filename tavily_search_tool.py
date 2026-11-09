"""A visible model/tool loop using Gemini and Tavily search."""

import json
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langsmith import traceable


@traceable(
    name="Custom Search Agent",
    process_inputs=lambda inputs: {
        "question": inputs["question"],
        "max_model_calls": inputs.get("max_model_calls", 5),
    },
)
def run_search(model, search_tool, question: str, max_model_calls: int = 5) -> str:
    """Call the model, run its requested search tools, and return its answer."""
    model_with_tools = model.bind_tools([search_tool])
    messages = [
        SystemMessage(content=(
            "You are a search assistant. Use the search tool when needed, "
            "answer using its results, and include source URLs. "
            "If a search fails or lacks information, say so."
        )),
        HumanMessage(content=question),
    ]

    for call_number in range(1, max_model_calls + 1):
        print(f"\n--- LLM call {call_number}: sending conversation to Gemini ---")
        response = model_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            print("--- Gemini returned a final answer ---")
            return response.text

        for tool_call in response.tool_calls:
            name = tool_call["name"]
            arguments = tool_call["args"]
            print(f"\n--- Tool requested: {name} ---")
            print(f"Arguments: {json.dumps(arguments, ensure_ascii=False)}")

            if name != search_tool.name:
                tool_result = "Unknown tool requested."
            else:
                try:
                    tool_result = search_tool.invoke(arguments)
                except Exception as exc:
                    # Do not print credentials or send exception details to the model.
                    tool_result = f"Search failed ({type(exc).__name__})."

            result_text = (
                tool_result if isinstance(tool_result, str)
                else json.dumps(tool_result, ensure_ascii=False, default=str)
            )
            print(f"Tool result: {result_text}")
            messages.append(
                ToolMessage(content=result_text, tool_call_id=tool_call["id"])
            )

    return "Stopped after reaching the model-call limit without a final answer."


def main() -> None:
    load_dotenv()
    if os.getenv("GOOGLE_API_KEY"):
        os.environ.pop("GEMINI_API_KEY", None)

    model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
    search_tool = TavilySearch()
    question = "search for top 3 restaurants in bengaluru india?"
    print(f"Question: {question}")
    print(f"\nFinal answer:\n{run_search(model, search_tool, question)}")


if __name__ == "__main__":
    main()
