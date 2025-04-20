# Flask Quiz Game App – Assignment 3
# Requirement 1, 3 + Extra Credit 2, 6
# Used the workshop starter structure and a bit of AI to help me on some parts

from flask import Flask, render_template, request, redirect, session, url_for
import random, json, os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Load questions from JSON
with open('questions.json') as f:
    all_questions = json.load(f)

# All of the app.route below helps us tell the quiz app on which URL to activate which function
# REQUIREMENT 1: user identification and history
# This part helps us with user name and category selection also starts a new sessions with randomized questions in the chosen category
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['category'] = request.form['category']
        session['score'] = 0
        session['question_index'] = 0

        # This part right here shuffles the questions around so I think it matches with EXTRA CREDIT: Requirement 6, randomized quiz categories
        selected_questions = all_questions[session['category']]
        random.shuffle(selected_questions)
        session['questions'] = selected_questions

        return redirect(url_for('quiz'))

    return render_template('index.html')

# REQUIREMENT 3: Time-based based, check on quiz.html
# This part displays our question one at a time with the given answer options
# via POST is how it accepts the user's answers and calculating the feedback that we need
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    index = session.get('question_index', 0)
    questions = session.get('questions', [])

    if index >= len(questions):
        return redirect(url_for('result'))

    current_question = questions[index]
    options = list(zip('abcd', current_question['options']))

    if request.method == 'POST':
        # This part over here is where it will check if what the user chose was correct or not and it will update the scores and move onto the next question
        # I used AI specifically on lines 51-64 because I needed to make it more cleaner compared to the workshop version.
        # This part not only made it more scalable, but not as hard-coded.
        selected = request.form.get('answer')
        selected_text = dict(options).get(selected, "")
        correct = current_question['correct_answers']

        if selected_text in correct:
            session['score'] += 1
            feedback = "Nice job, lets go!"
        else:
            feedback = f"NOPE! Correct answer is: {correct[0]}"

        session['question_index'] += 1
        return render_template('feedback.html', feedback=feedback, score=session['score'], index=index+1)

    return render_template('quiz.html', question=current_question, options=options, index=index+1, total=len(questions))

# EXTRA credit requirement: Leaderboard system and displaying your final result of the quiz being completed
# AI was used to help implement category-based questions, leaderboard logic, and timer functionality, all reviewed and customized to match the workshop format.
# I used AI on lines 75-91 here to help me implement the leaderboard logic, which then I smoothly transitioned to help me with my individual requirement
@app.route('/result')
def result():
    name = session.get('name', 'Guest')
    score = session.get('score', 0)
    total = len(session.get('questions', []))

    # Over here saves it to the leaderboard
    leaderboard_file = 'leaderboard.json'
    entry = {"name": name, "score": score}

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file) as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    data.sort(key=lambda x: x["score"], reverse=True)
    data = data[:10]

    with open(leaderboard_file, "w") as f:
        json.dump(data, f, indent=4)

    return render_template('result.html', score=score, total=total, name=name)

# The leaderboard page where it displays the top users in this quiz
@app.route('/leaderboard')
def leaderboard():
    with open('leaderboard.json') as f:
        top_scores = json.load(f)
    return render_template('leaderboard.html', leaderboard=top_scores)

# Runs the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
