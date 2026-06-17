from huggingface_hub import login
import os
from dotenv import load_dotenv
from fitnessagent import build_agent

QUERY = """I am 20 years old, female, 52kg, 172cm.
My goal is muscle gain.
Give me:
1. BMI
2. Daily calories
3. Workout plan
4. Diet plan
5. Top 5 high-protein non-vegetarian foods
"""


def main():
    load_dotenv()
    login(token=os.getenv("HF_TOKEN"))
    agent = build_agent()
    result = agent.run(QUERY)
    print(result)


if __name__ == "__main__":
    main()