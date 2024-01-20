import openai
import requests

# Set your OpenAI GPT-3 API key
api_key = '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'  # Replace this with your actual API key

# Set the endpoint URL for the ChatGPT API
url = 'https://api.openai.com/v1/chat/completions'

# Set the conversation history
conversation_history = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Who won the world series in 2020?'}
]

# Set the user's latest message
user_message = {'role': 'user', 'content': 'Tell me a joke.'}

# Create the payload for the API request
payload = {
    'messages': conversation_history + [user_message],
    'model': 'gpt-3.5-turbo',
}

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

# Make the API request
response = requests.post(url, headers=headers, json=payload)

# Parse and print the full API response
result = response.json()
print(result)

# Check if 'choices' is present in the response
if 'choices' in result:
    print(result['choices'][0]['message']['content'])
else:
    print("Unexpected response format. Please check the API response structure.")
