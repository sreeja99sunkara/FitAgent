import os
from smolagents import CodeAgent, DuckDuckGoSearchTool
from smolagents.models import OpenAIServerModel

from tools.bmi import bmi_calculator
from tools.calories import calorie_calculator
from tools.diet import diet_suggestion
from tools.workout import workout_generator


def build_agent() -> CodeAgent:
    model = OpenAIServerModel(
        model_id="llama-3.3-70b-versatile",
        api_base="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
    )

    agent = CodeAgent(
        tools=[
            bmi_calculator,
            calorie_calculator,
            workout_generator,
            diet_suggestion,
            DuckDuckGoSearchTool(),
        ],
        model=model,
    )
    return agent