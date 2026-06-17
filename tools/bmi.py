from smolagents import tool

@tool
def bmi_calculator(weight: float, height: float) -> str:
    """
    Calculates BMI.

    Args:
        weight: Weight in kg.
        height: Height in cm.
    """
    bmi = weight / ((height / 100) ** 2)
    return f"BMI = {bmi:.2f}"