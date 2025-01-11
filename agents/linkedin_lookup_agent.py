import os

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_ollama.llms import OllamaLLM

os.environ["TAVILY_API_KEY"] = "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"

def get_profile_url_tavily(name: str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

def lookup(name: str):
    llm = OllamaLLM(
        base_url="http://localhost:11434",  # Ensure the Ollama server is running locally
        model="llama3.2:1b",
        verbose=True
    )

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                        Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]

    return linked_profile_url

# Example usage
if __name__ == "__main__":
    name = "John Doe"  # Replace with the name you want to search
    profile_url = lookup(name)
    print(profile_url)
