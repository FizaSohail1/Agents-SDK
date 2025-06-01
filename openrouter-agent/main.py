import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

history = []

OPENAI_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

client = AsyncOpenAI(
    api_key= OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# gemini client
agent = Agent(
    name="Knowledge Agent",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free" ,openai_client=client),
    instructions="You are a helpful AI assistant. Answer user queries in detail."
)

@cl.on_message
async def main(message: cl.Message):
    # Use async Runner
    res = await Runner.run(agent, history)
    history.append({"role":"user","content": res})

    await cl.Message(content=res.final_output).send()

print(history)    


