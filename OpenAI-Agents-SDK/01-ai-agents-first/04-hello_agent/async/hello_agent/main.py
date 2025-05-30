# uv run main.py
# type : ignore
import os
from agents import Agent, AsyncOpenAI, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.run import RunConfig
from dotenv import load_dotenv

set_tracing_disabled(disabled=True)
# for load env secret 
load_dotenv()

API_KEY =os.environ.get("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
)

agent = Agent(
    name = "Assistant",
    instructions = "You're helpful assistant."
)
# agent loop             name   input
result = Runner.run_sync(agent, "Who is the founder of Pakistan?", run_config = config)

print(result.final_output)