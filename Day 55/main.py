from flask import Flask
import random

answer = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1> Guess a number between 0 and 9</h1>' \
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2RlZnNoNWcyNjYya2UzdHpraW1oNDJoZTBvdzc1aGUwcjNoenNpcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif">'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > answer:
        return '<h1 style= "color: red">Too High</h1>' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW5yNDdsMmU4bHFhNmozbDdsZnJ2N2hudmdybmxrZWVhYzJ6bW12dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif">'

    elif guess < answer:
        return '<h1 style= "color: red">Too Low</h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2cyeDJteHA0d2o5amxoeHd1NHphbDd0cWNkZ2czbDJ1a3c4ZnFvZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yFQ0ywscgobJK/giphy.gif">'

    else:
        return '<h1 style="color: green">That\'s correct</h1>' \
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXozdGRmYjN4OXYzOTk3bWR4M29vdGc4bTRibWVqcWs5ZjFuN2pzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VIPdgcooFJHtC/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
