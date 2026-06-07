# FitAgent

FitAgent is an AI-powered Fitness Coach Agent built using **SmolAgents** and **Hugging Face Inference API**. The agent interacts with users through natural language and dynamically selects tools to provide personalized fitness recommendations.

## Features

*  BMI Calculation
*  Daily Calorie Requirement Estimation
*  Personalized Workout Plans
*  Diet Recommendations
*  Natural Language Interaction using AI Agents

## Tech Stack

* Python
* SmolAgents
* Hugging Face Hub
* Hugging Face Inference API
* Google Colab

## Tools Implemented

### BMI Calculator

Calculates Body Mass Index (BMI) based on height and weight.

### Calorie Calculator

Estimates:

* Basal Metabolic Rate (BMR)
* Maintenance Calories
* Goal-Based Calories (Weight Loss / Maintenance / Muscle Gain)

### Workout Generator

Provides customized weekly workout schedules for:

* Weight Loss
* Muscle Gain
* Maintenance

### Diet Suggestion

Generates diet plans based on:

* Fitness Goal
* Vegetarian Preference
* Non-Vegetarian Preference

## Example Query

```text
I am 20 years old,
female,
52kg,
172cm.

My goal is muscle gain.

Give me:
1. BMI
2. Daily calorie requirement
3. Workout plan
4. Diet recommendation
```

## Sample Output

```text
BMI = 17.58

Maintenance Calories: 2080 kcal/day

Recommended Calories for muscle_gain:
2380 kcal/day

Workout Plan:
Monday: Chest + Triceps
Tuesday: Back + Biceps
...

Diet Plan:
Breakfast: Milk + Peanut Butter Toast
Lunch: Rice + Paneer + Dal
...
```

## Installation

```bash
pip install -U smolagents
pip install -U ddgs
```

## Usage

1. Create a Hugging Face account.
2. Generate an access token.
3. Login using:

```python
from huggingface_hub import login
login()
```

4. Run the notebook.
5. Interact with the Fitness Coach Agent using natural language.

## Future Improvements

* Water Intake Calculator
* Progress Tracking
* Fitness Goal Monitoring
* Web Search Integration
* Streamlit Web Application
* Memory-Based Personal Fitness Assistant

## Learning Outcomes

This project demonstrates:

* Agentic AI Concepts
* Tool Calling
* Natural Language Interfaces
* AI Workflow Design
* Integration of Multiple Specialized Tools

## Author

Sreeja S

Built as a hands-on project while learning Agentic AI with SmolAgents.
