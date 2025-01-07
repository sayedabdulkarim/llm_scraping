import requests
import json  # Import the json module for parsing

# Define the server URL and prompt details
url = "http://localhost:11434/api/chat"
model = "llama3.2:1b"
prompt = "What is the capital of France?"

# Send the request to the server
response = requests.post(
    url,
    json={
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    },
    stream=True  # Enable streaming
)

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
