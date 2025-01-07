from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
# Define the prompt template
summary_template = """
Given the information {information} about a person, create:
1. A short summary.
2. Two interesting facts about them.
"""

# Create a PromptTemplate
summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template
)

# Initialize the LLM with your local Ollama server
llm = OllamaLLM(
    base_url="http://localhost:11434",  # Ensure the Ollama server is running locally
    model="llama3.2:1b",
    verbose=True
)

# Combine the template and the LLM
chain = summary_prompt_template | llm

# Input data for the prompt
information = "Albert Einstein was a theoretical physicist who developed the theory of relativity."

# Invoke the chain
res = chain.invoke(input={"information": information})

# Print the response
print(res)

PromptTemplate()