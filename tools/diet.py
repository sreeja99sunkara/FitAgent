from smolagents import tool


@tool
def diet_suggestion(goal: str, diet_type: str = "vegetarian") -> str:
    """
    Suggests a diet plan.

    Args:
        goal: weight_loss, muscle_gain, or maintenance.
        diet_type: vegetarian or non_vegetarian.
    """
    goal = goal.lower()
    diet_type = diet_type.lower()

    diets = {
        ("weight_loss", "vegetarian"): """
Breakfast: Oats + Fruits
Lunch: Brown Rice + Dal + Salad
Snack: Green Tea + Nuts
Dinner: Vegetable Soup + Paneer
""",
        ("weight_loss", "non_vegetarian"): """
Breakfast: Eggs + Fruits
Lunch: Grilled Chicken + Salad
Snack: Nuts
Dinner: Fish + Vegetables
""",
        ("muscle_gain", "vegetarian"): """
Breakfast: Milk + Peanut Butter Toast
Lunch: Rice + Paneer + Dal
Snack: Protein Shake
Dinner: Chapati + Soy Chunks
""",
        ("muscle_gain", "non_vegetarian"): """
Breakfast: Eggs + Milk
Lunch: Chicken Breast + Rice
Snack: Protein Shake
Dinner: Fish + Sweet Potato
""",
        ("maintenance", "vegetarian"): """
Balanced meals with vegetables,
whole grains, fruits and protein.
""",
        ("maintenance", "non_vegetarian"): """
Balanced meals with lean meat,
vegetables and whole grains.
""",
    }

    return diets.get((goal, diet_type), "Please choose valid goal and diet type.")