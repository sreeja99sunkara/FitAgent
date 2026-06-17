# FitAgent

FitAgent is an AI-powered Fitness Coach Agent built using **SmolAgents** and **Groq (LLaMA 3.3 70B)**. The agent interacts with users through natural language and dynamically selects tools to provide personalized fitness recommendations.

## Features

- BMI Calculation
- Daily Calorie Requirement Estimation
- Personalized Workout Plans
- Diet Recommendations
- Natural Language Interaction using AI Agents
- Web Search for Nutrition & Fitness Information

## Tech Stack

- Python
- SmolAgents
- Groq API (LLaMA 3.3 70B)
- Hugging Face Hub
- DuckDuckGo Search

## Project Structure

```
FitAgent/
├── main.py               # Entry point
├── fitnessagent/
│   ├── __init__.py
│   └── agent.py          # Agent setup
├── tools/
│   ├── __init__.py
│   ├── bmi.py
│   ├── calories.py
│   ├── workout.py
│   └── diet.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Tools Implemented

### BMI Calculator
Calculates Body Mass Index (BMI) based on height and weight.

### Calorie Calculator
Estimates:
- Basal Metabolic Rate (BMR)
- Maintenance Calories
- Goal-Based Calories (Weight Loss / Maintenance / Muscle Gain)

### Workout Generator
Provides customized weekly workout schedules for:
- Weight Loss
- Muscle Gain
- Maintenance

### Diet Suggestion
Generates diet plans based on:
- Fitness Goal
- Vegetarian / Non-Vegetarian Preference

### Web Search Tool
Finds fitness and nutrition information using DuckDuckGo Search.

## Installation

```bash
pip install -r requirements.txt
```

## Setup

1. Get a free Groq API key at [console.groq.com](https://console.groq.com)

```env
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
```

## Usage

```bash
python main.py
```

## Example Query

```text
I am 20 years old, female, 52kg, 172cm.
My goal is muscle gain.
Give me:
1. BMI
2. Daily calorie requirement
3. Workout plan
4. Diet recommendation
5. High-protein non-vegetarian foods
```

## Sample Output

```text
BMI = 17.58
Maintenance Calories: 2080 kcal/day
Recommended Calories for muscle_gain: 2380 kcal/day

Workout Plan:
Monday: Chest + Triceps
Tuesday: Back + Biceps
...

Diet Plan:
Breakfast: Milk + Peanut Butter Toast
Lunch: Rice + Paneer + Dal
...
```

## Future Improvements

- Water Intake Calculator
- Progress Tracking
- Fitness Goal Monitoring
- Streamlit Web Application
- Memory-Based Personal Fitness Assistant

## Learning Outcomes

This project demonstrates:
- Agentic AI Concepts
- Tool Calling
- Natural Language Interfaces
- AI Workflow Design
- Integration of Multiple Specialized Tools

## Author

Sreeja S

Built as a hands-on project while learning Agentic AI with SmolAgents.
