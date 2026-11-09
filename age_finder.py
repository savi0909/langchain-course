"""A small ReAct-style agent with a pretend person lookup."""

import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def lookup_birth_date(name: str) -> str:
    """Look up a person's birth date in the small mock database."""
    if name.strip().casefold() == "ada lovelace":
        return "Ada Lovelace was born December 10, 1815."
    return "No information found"


@tool
def lookup_death_date(name: str) -> str:
    """Look up a person's death date in the small mock database."""
    if name.strip().casefold() == "ada lovelace":
        return "Ada Lovelace died November 27, 1852."
    return "No information found"


def find_age(model, question: str) -> str:
    """Run the model/tool conversation ourselves, with a limit on model calls."""
    tools = {tool.name: tool for tool in [lookup_birth_date, lookup_death_date]}
    model_with_tools = model.bind_tools(list(tools.values()))
    messages = [
        SystemMessage(content=(
            "You are AgeFinder. Use the birth and death date tools to find the person's dates. "
            "Calculate their age at death, accounting for their birthday. "
            "If the lookup finds no information, say you do not know."
        )),
        HumanMessage(content=question),
    ]

    for turn in range(1, 6):
        print(f"\nModel call {turn}")
        response = model_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response.text

        for call in response.tool_calls:
            print(f"Tool requested: {call['name']} {call['args']}")
            if call["name"] in tools:
                result = tools[call["name"]].invoke(call["args"])
            else:
                result = "Unknown tool"
            print(f"Tool result: {result}")
            messages.append(ToolMessage(content=result, tool_call_id=call["id"]))

    return "Stopped after five model calls without a final answer."


def main() -> None:
    load_dotenv()
    if os.getenv("GOOGLE_API_KEY"):
        os.environ.pop("GEMINI_API_KEY", None)

    model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
    question = "ada lovelace"
    # input("Who would you like to ask about? ")
    print(f"\nAnswer: {find_age(model, question)}")


if __name__ == "__main__":
    main()
