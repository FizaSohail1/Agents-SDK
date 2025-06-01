import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI (
    api_key= GEMINI_API_KEY,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel (
    model= "gemini-2.0-flash",
    openai_client= client
)

agent = Agent (
    name="Instructor",
    model= model,
    instructions="You are a helpfull assitant"
)

runner = Runner.run_sync(agent, "Hello how are you")
print(runner.final_output)
