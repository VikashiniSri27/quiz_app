from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions
questions = [
    {
        'question': "What is the capital of France?",
        'options': ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
        'answer': 'Paris'
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ['Mark Twain', 'Charles Dickens', 'William Shakespeare', 'Leo Tolstoy'],
        'answer': 'William Shakespeare'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    # Pass enumerate to the template
    return render_template('quiz.html', questions=questions, enumerate=enumerate)

@app.route('/result', methods=['POST'])
def result():
    user_answers = request.form
    score = 0
    for i, question in enumerate(questions):
        if user_answers.get(f'question-{i}') == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)


