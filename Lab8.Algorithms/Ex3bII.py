import random

def assign_requirements(requirements):
    R1, R2 = random.sample(requirements, 2)  # Pick two different random elements
    return R1, R2

# Example list of additional requirements
requirements_list = [
    "Write scores to a file",
    "Notify user of high score",
    "Allow multiple answers",
    "Allow multiple correct answers",
    "Choose question category",
    "Provide hint option",
    "Explain correct answers",
    "Interactive question entry",
    "Add timer & bonus points",
    "50/50 lifeline feature"
]

# Test the function
print("Assigned Requirements:", assign_requirements(requirements_list))