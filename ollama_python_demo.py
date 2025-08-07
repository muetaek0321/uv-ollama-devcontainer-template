from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gpt-oss:20b', messages=[
  {
    'role': 'user',
    'content': 'ollamaとは何ですか？',
  },
])

print(response.message.content)