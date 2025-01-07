import requests
import json

# Define the server URL and prompt details
url = "http://localhost:11434/api/chat"
model = "llama3.2:1b"
information = "Albert Einstein was a theoretical physicist who developed the theory of relativity."

# Define the request payload
payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": f"Given the information '{information}', create a short summary and two interesting facts."
        }
    ]
}

# Send the request to the local Ollama server
response = requests.post(url, json=payload, stream=True)

# Check the response status
if response.status_code == 200:
    # Aggregate the streamed response
    full_response = ""
    for chunk in response.iter_lines():
        if chunk:
            try:
                # Parse each chunk as JSON
                chunk_data = json.loads(chunk.decode("utf-8"))
                message_content = chunk_data.get("message", {}).get("content", "")
                full_response += message_content
            except json.JSONDecodeError as e:
                print("Error parsing chunk:", e)
    print("Response from LLM:", full_response)
else:
    print(f"Error {response.status_code}: {response.text}")
