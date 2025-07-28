print("Welcome to EduBot! 🌟 Ask me anything. Type 'exit' to leave.")

while True:
    q = input("You: ").lower()

    if "exit" in q:
        print("EduBot: Bye! Keep learning 📚")
        break
    elif "hello" in q or "hi" in q:
        print("EduBot: Hello, my friend! 😊")
    elif "sad" in q or "tired" in q:
        print("EduBot: It's okay to feel that way. I'm here to help you.")
    elif "2+2" in q:
        print("EduBot: 2 + 2 = 4 📊")
    elif "photosynthesis" in q:
        print("EduBot: It's how plants make food using sunlight. 🌱")
    elif "gravity" in q:
        print("EduBot: Gravity is the force that pulls everything towards the Earth.")
    elif "your name" in q:
        print("EduBot: I'm EduBot, your learning buddy!")
    else:
        print("EduBot: Hmm... I don't know that yet, but I'm learning! 🧠")
