# 🤖 Multi-Agents using Agent SDK

This repo showcases three types of AI agents built using the OpenAI Agent SDK, demonstrating how to integrate with different LLM providers such as Gemini via Google's API and OpenRouter. Each agent has a different execution style: asynchronous, synchronous, and Chainlit UI integration.

## 📦 Setup Instructions

1. Clone this repository.
2. Install required dependencies using **uv**


```bash 
uv add openai-agents
```
```bash 
uv add python-dotenv
```
```bash 
uv add chainlit
```
```bash 
uv add litellm
```


⚠️ Don’t forget to create a .env file and store your API keys:

**env**

```bash 
GEMINI_API_KEY=your_gemini_api_key 
OPEN_ROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_KEY=your_openai_api_key
```
## 📂 Agents Description
### 1. basic-agent
- Uses async runner and the Gemini model via Google API.
- A simple terminal-based agent that responds to user prompts.
To run:
```bash
 cd basic-agent
 uv run main.py
 ```

### 2. sync_basic-agent
- A synchronous version of the basic agent.
- Ideal for quick command-line interactions.
 To run:
 ```bash
 cd sync-basic-agent
 uv run main.py
 ```

### 3. litellm-agent
- Built using the LiteLLM SDK.
- Very lightweight and portable.
To run:
 ```bash
 cd litellm-agent
 uv run main.py
 ```

### 4. openrouter-agent
- Utilizes OpenRouter and integrates with Chainlit for web-based interaction.
- Designed for real-time UI response via deepseek-chat model.
- Connects to GPT models (like GPT-4.1-mini) using litellm.completion.
To run: 
 ```bash
 cd openrouter-agent
 uv run main.py
 ```
Open your browser at http://localhost:8000 to interact with the agent.

## 🗂️ Summary Table
| Agent Name       | Execution        | Model Used                        | Interface |
|------------------|------------------|-----------------------------------|-----------|
| `basic-agent`     | Asynchronous      | Gemini 2.0 Flash (Google)         | Terminal  |
| `syn_basic-agent` | Synchronous       | Gemini 2.0 Flash (Google)         | Terminal  |
| `openrouter-agent`| Async + Chainlit  | DeepSeek Chat V3 (OpenRouter)     | Web UI    |
| `litellm-agent`   | LiteLLM-based     | GPT-4.1-mini (via LiteLLM)        | Terminal  |




## ✅ Key Concepts Demonstrated
- Using OpenAI-compatible SDK with external providers (Google Gemini, OpenRouter)
- Async and sync agent execution
- Chat interface with Chainlit
- Custom instructions and multi-agent flexibility


### 👨‍🏫 Created By

**Fiza Sohail**

As part of my AI and LLM learning project.

