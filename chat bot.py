import random
import pyttsx3
from datetime import datetime

# 🧠 Setup
bot_name = 'Bob'
engine = pyttsx3.init()

# 🗣️ Speak function
def speak(text):
    print(f"{bot_name}: {text}")
    engine.say(text)
    engine.runAndWait()

# 👤 Get user's name
user_name = input("What's your name? ").strip().capitalize()
speak(f"Hello {user_name}, I'm {bot_name}. How can I help you today?")

# 🧠 Static responses
commands = {
    "your name": f"My name is {bot_name}.",
    "my name": f"You told me your name is {user_name}.",
    "love you": "Love you too ❤️",
    "joke": "Why did the developer go broke? Because he used up all his cache.",
    "bye": f"Bye {user_name}, see you soon!",
}

# 🎲 Random greetings
greetings = ["Hey!", "Hi there!", "Yo!", "What’s up!", "Hello!"]

# 🧠 Main chat loop
while True:
    user_input = input(f"{user_name}: ").strip().lower()

    if user_input in ['hi', 'hello']:
        speak(random.choice(greetings))

    elif user_input == "time":
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")

    elif user_input == "calculator":
        speak("Let's add two numbers.")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            speak(f"The sum is {result}")
        except ValueError:
            speak("Invalid input. Please enter numbers.")

    elif user_input in commands:
        speak(commands[user_input])

    elif user_input in ['bye', 'exit']:
        speak(f"Goodbye {user_name}! Have a great day!")
        break

    else:
        speak("Sorry, I didn’t understand that.")
