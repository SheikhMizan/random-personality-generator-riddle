from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

riddles = [
    {
        "question": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
        "answer": "Pencil"
    },
    {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "answer": "Echo"
    },
    {
        "question": "I am always in front of you but can never be seen. What am I?",
        "answer": "Future"
    },
    {
        "question": "I am full of keys but can't open any locks. What am I?",
        "answer": "Keyboard"
    },
    {
        "question": "I can be cracked, made, told, and played. What am I?",
        "answer": "Joke"
    },
    {
        "question": "What gets wetter and wetter the more it dries?",
        "answer": "Towel"
    },
    {
        "question": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?",
        "answer": "Map"
    },
    {
        "question": "I am an odd number. Take away one letter and I become even. What number am I?",
        "answer": "Seven"
    },
    {
        "question": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
        "answer": "Pencil"
    },
    # {
    #     "question": "I have keys but no locks. I have space but no room. You can enter, but can't go outside. What am I?",
    #     "answer": "Keyboard"
    # },
    # {
    #     "question": "I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
    #     "answer": "Fire"
    # },
    # {
    #     "question": "I am always hungry, I must always be fed, the finger I touch will soon turn red. What am I?",
    #     "answer": "Fire"
    # },
    # {
    #     "question": "I have keys but can't open locks. I have a space but no room. You can enter, but can't go outside. What am I?",
    #     "answer": "Keyboard"
    # },
    # {
    #     "question": "I am a word of letters three; add two and fewer there will be. What am I?",
    #     "answer": "Few"
    # },
    # {
    #     "question": "I am a path situated between high natural masses. Remove my first letter and you have a path situated between man-made masses. What am I?",
    #     "answer": "Mountain"
    # },
    # {
    #     "question": "I'm light as a feather, yet the strongest person can't hold me for much longer than a minute. What am I?",
    #     "answer": "Breath"
    # },
    # {
    #     "question": "I'm always in front of you but can't be seen. What am I?",
    #     "answer": "Future"
    # },
    {
        "question": "I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        "answer": "Fire"
    }
]

def calculate_personality(answers):
    personality_scores = {
        "Introvert": 0,
        "Extrovert": 0,
        "Analytical": 0,
        "Creative": 0,
        "Adventurous": 0,
        "Practical": 0
    }
    
    for answer in answers:
        if answer.lower() == "pencil":
            personality_scores["Analytical"] += 1
        elif answer.lower() == "echo":
            personality_scores["Introvert"] += 1
        elif answer.lower() == "future":
            personality_scores["Practical"] += 1
        elif answer.lower() == "keyboard":
            personality_scores["Creative"] += 1
        elif answer.lower() == "joke":
            personality_scores["Extrovert"] += 1
        elif answer.lower() == "towel":
            personality_scores["Adventurous"] += 1
        elif answer.lower() == "map":
            personality_scores["Analytical"] += 1
        elif answer.lower() == "seven":
            personality_scores["Practical"] += 1
        # Add more conditions for remaining riddles
        
    # Determine the personality based on the scores
    personality = max(personality_scores, key=personality_scores.get)
    
    return personality

@app.route("/")
def home():
    random.shuffle(riddles)
    return render_template("home.html", riddles=riddles)

@app.route("/result", methods=["POST"])
def result():
    user_answers = []
    for riddle in riddles:
        answer = request.form.get(riddle["question"])
        user_answers.append(answer)
    personality = calculate_personality(user_answers)
    return render_template("result.html", personality=personality)

if __name__ == "__main__":
    app.run()
