from smolagents import tool


@tool
def workout_generator(goal: str) -> str:
    """
    Generates a workout plan based on fitness goal.

    Args:
        goal: weight_loss, muscle_gain, or maintenance.
    """
    goal = goal.lower()

    workouts = {
        "weight_loss": """
Monday: 30 min Cardio + Full Body Workout
Tuesday: Walking + Core Exercises
Wednesday: HIIT (20 mins)
Thursday: Strength Training
Friday: Cardio + Abs
Saturday: Outdoor Activity
Sunday: Rest
""",
        "muscle_gain": """
Monday: Chest + Triceps
Tuesday: Back + Biceps
Wednesday: Legs
Thursday: Shoulders
Friday: Upper Body
Saturday: Lower Body
Sunday: Rest
""",
        "maintenance": """
Monday: Full Body Workout
Tuesday: Cardio
Wednesday: Yoga/Stretching
Thursday: Strength Training
Friday: Cardio
Saturday: Sports Activity
Sunday: Rest
""",
    }

    return workouts.get(goal, "Please choose: weight_loss, muscle_gain, or maintenance.")