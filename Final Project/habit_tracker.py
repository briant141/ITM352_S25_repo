# habit_tracker.py
import json
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Main data setups that you will see in the json as well as putting a new json file inside the folder
habits = []
completion_log = {}
data_file = os.path.join(os.path.dirname(__file__), 'habit_data.json')

# Data is loaded from the json file, meaning it will get whatever is from the last saved (habit names, completion, anything saved in that json file)
def load_data():
    global habits, completion_log
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
            habits = data.get('habits', [])
            completion_log = data.get('completion_log', {})

# For the actual save data, it will look for whenever a habit is added or removed as well as marking things complete. 
# So every big changes is saved to the json file immediately, meaning data persists in each session
def save_data():
    with open(data_file, 'w') as f:
        json.dump({'habits': habits, 'completion_log': completion_log}, f)

# The main core features as you can tell, adding habits and removing habits
def add_habit(habit):
    if habit in habits:
        print("Habit already exists.")
    else:
        habits.append(habit)
        completion_log[habit] = []
        save_data()
        print(f"Added habit: {habit}")


def remove_habit(habit):
    if habit in habits:
        habits.remove(habit)
        completion_log.pop(habit, None)
        save_data()
        print(f"Habit is now gone 🥺😔: {habit}")
    else:
        print("Habit not found.")


# Lines 56–71: Used AI to help me create index-based selection for marking habits complete.
# "Can you make a Python menu that lets users select from a list of habits by number to mark one as complete?"
# The AI-suggested index-based menu avoids typing full habit names and improves the user experience.
def mark_habit_by_index():
    if not habits:
        print("No habits to mark.")
        return
    print("\nYour Habits:")
    for idx, habit in enumerate(habits, 1):
        print(f"{idx}. {habit}")
    try:
        choice = int(input("Select a habit number to mark as complete: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            today = datetime.now().strftime("%Y-%m-%d")
            if today in completion_log[habit]:
                print("Already marked for today.")
            else:
                completion_log[habit].append(today)
                save_data()
                print(f"Marked {habit} as completed today.")
        else:
            print("Invalid habit number bum.")
    except ValueError:
        print("Please enter a valid number you bum.")


# Lines 82-92: Used AI to simplify summary viewing with numbered habit selection.
# "Can you make it so users can select a habit from a numbered list to view a summary instead of typing it?"
# This basically helps me replace full text input with a simpler numeric option (e.g. 1, 2, 3, 4)
def show_summary_by_index():
    if not habits:
        print("Uh oh, no habits to show.")
        return
    print("\nYour Habits:")
    for idx, habit in enumerate(habits, 1):
        print(f"{idx}. {habit}")
    try:
        choice = int(input("Select a habit number to view summary: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            total = len(completion_log.get(habit, []))
            streak = calculate_streak(habit)
            print(f"\nSummary for '{habit}':")
            print(f"Total completions: {total}")
            print(f"Current streak: {streak} days\n")
        else:
            print("Invalid habit number.")
    except ValueError:
        print("Please enter a valid number.")

# Lines 101–111: Used AI to help me implement the habit streak calculation logic.
# "Write a function to calculate the current streak of consecutive days a habit has been completed based on a list of dates."
# The loop logic ensures the streak is correctly counted back from today.
def calculate_streak(habit):
    dates = sorted(completion_log.get(habit, []))
    streak = 0
    today = datetime.now().date()
    for i in range(len(dates)-1, -1, -1):
        date_obj = datetime.strptime(dates[i], "%Y-%m-%d").date()
        if date_obj == today - timedelta(days=streak):
            streak += 1
        else:
            break
    return streak

# A visual summary so the users can see their total progress in completion of their habits
def visualize_progress():
    if not habits:
        print("No habits to display.")
        return
    habit_names = habits
    counts = [len(completion_log[h]) for h in habits]
    plt.bar(habit_names, counts)
    plt.xlabel("Habits")
    plt.ylabel("Completions")
    plt.title("Habit Completion Overview")
    plt.tight_layout()
    plt.show()

# This is the main menu, what you first see when you launch the app
# This main loop structure was refined for simplicity and user-friendliness.
def main_menu():
    load_data()
    # test_streak()
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. Mark Habit as Complete")
        print("4. Show Habit Summary")
        print("5. Visualize Progress")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_habit(input("Enter habit name 😃😃: "))
        elif choice == '2':
            remove_habit(input("Are you sure you want to remove a habit? 😢 Type in the full name of the habit (check habit_tracker.json) "))
        elif choice == '3':
            mark_habit_by_index()
        elif choice == '4':
            show_summary_by_index()
        elif choice == '5':
            visualize_progress()
        elif choice == '6':
            save_data()
            print("We have saved your progress! Latah!")
            break
        else:
            print("Invalid choice. Try again.")

# I am trying to test to see if the streak function actually works here (which it does)
"""
def test_streak():
    test_habit = "TestHabit"
    test_dates = [
        "2025-04-28",
        "2025-04-29",
        # "2025-04-30",
        "2025-05-01",
        "2025-05-02"  # Adjust based on today's date
    ]
    completion_log[test_habit] = test_dates
    streak = calculate_streak(test_habit)
    print(f"Streak for '{test_habit}': {streak}")
"""
if __name__ == '__main__':
    main_menu()


