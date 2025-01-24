def chatbot():
    print("Hello! I'm your chatbot. Ask me something or say 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "how was your day" in user_input:
            print("Chatbot: My day was great, thank you for asking! How about yours?")
        elif "what's the weather" in user_input or "what is the weather" in user_input:
            print("Chatbot: I'm not sure about the current weather, but it's always a good idea to check a weather app!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly! How are you?")
        elif "what's your name" in user_input or "what is your name" in user_input:
            print("Chatbot: I'm your friendly chatbot! I don't have a name yet, but you can give me one.")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")
            
# Run the chatbot
chatbot()