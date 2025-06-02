import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

response = completion(
    model="gpt-4.1-mini",  
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Agentic AI?"}
    ]
)

print("\n ✅ Response: \n\n", response['choices'][0]['message']['content'])
