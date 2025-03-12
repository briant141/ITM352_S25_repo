import json

# Define the dictionary
quiz_data = {
    "What is the airspeed of an unladen swallow in miles/hr": [
        "12",
        "8",
        "11",
        "15"
    ],
    "What is the capital of Texas": [
        "Austin",
        "San Antonio",
        "Dallas",
        "Waco"
    ],
    "The Last Supper was painted by which artist": [
        "Da Vinci",
        "Rembrandt",
        "Picasso",
        "Michelangelo"
    ],
    "Which classic novel opens with the line 'Call Me Ishmael'?": [
        "Moby Dick",
        "Wuthering Heights",
        "The Old Man and the Sea",
        "The Scarlet Letter"
    ],
    "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?": [
        "Fallingwater",
        "Watering Heights",
        "Mossyledge",
        "Taliesin"
    ]
}

# File path - Saves the JSON file in the current working directory
json_file_path = "quiz_questions.json"

# Save dictionary as a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(quiz_data, json_file, indent=4)

print(f"JSON file '{json_file_path}' has been created successfully!")
