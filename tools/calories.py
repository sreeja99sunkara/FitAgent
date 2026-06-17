from smolagents import tool


@tool
def calorie_calculator(
    weight: float,
    height: float,
    age: int,
    gender: str,
    goal: str,
) -> str:
    """
    Calculates daily calorie requirements.

    Args:
        weight: Weight in kilograms.
        height: Height in centimeters.
        age: Age in years.
        gender: male or female.
        goal: weight_loss, maintenance, or muscle_gain.
    """
    gender = gender.lower()
    goal = goal.lower()

    # Mifflin-St Jeor Equation
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Assuming moderate activity
    maintenance = bmr * 1.55

    if goal == "weight_loss":
        target = maintenance - 500
    elif goal == "muscle_gain":
        target = maintenance + 300
    else:
        target = maintenance

    return (
        f"BMR: {bmr:.0f} kcal/day\n"
        f"Maintenance Calories: {maintenance:.0f} kcal/day\n"
        f"Recommended Calories for {goal}: {target:.0f} kcal/day"
    )