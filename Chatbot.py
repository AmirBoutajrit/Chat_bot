import requests
import random

def get_weather(city="Las Vegas"):
    """Fetches real-time weather data for a given city."""
    api_key = "4d81fec323b8fbaaea8a6052ca18c00d"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The current weather in {city} is {temp}°F with {description}."
        else:
            return f"Sorry, I couldn't fetch the weather for {city}. (Error: {data.get('message', 'Unknown error')})"
    except Exception:
        return "Error retrieving weather data."


def casual_response(user_input):
    """Generate a casual or related response based on simple keyword detection."""
    responses = {
        "food": ["I love hearing about food! What's your favorite dish?", "Tacos or pizza? Tough choice!"],
        "hobby": ["Do you have a hobby you enjoy?", "Hobbies are great for relaxing. I wish I could paint."],
        "bored": ["Boredom happens! Want to chat or hear a fun fact?"],
        "happy": ["I'm glad to hear that! What's making you happy today?"],
        "sad": ["I'm sorry you're feeling that way. I'm here if you want to talk."],
        "game": ["Games are so much fun. Do you play video games or board games?"],
        "school": ["School can be tough, but it's worth it! What are you studying?"],
        "work": ["Work can be stressful sometimes. Hope you're managing okay!"],
        "movie": ["Movies are great! Got a favorite one?"],
        "music": ["Music is such a vibe. What kind of music do you like?"]
    }

    for keyword, reply_list in responses.items():
        if keyword in user_input:
            return random.choice(reply_list)

    # Default fallback casual response
    fallback_responses = [
        "That's interesting! Tell me more.",
        "I see. What else is on your mind?",
        "Hmm, go on...",
        "That sounds cool!",
        "Wanna chat about something fun?"
    ]
    return random.choice(fallback_responses)


def chatbot():
    """A chatbot that responds to basic queries and simple conversation."""
    print("Hello! I'm your chatbot. Ask me something or say 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "how was your day" in user_input:
            print("Chatbot: My day was great, thank you for asking! How about yours?")
        elif "weather" in user_input:
            print("Chatbot:", get_weather())
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly! How are you?")
        elif "your name" in user_input:
            print("Chatbot: I'm your friendly chatbot! I don't have a name yet, but you can give me one.")
        else:
            # Let the bot respond casually regardless of the topic
            print("Chatbot:", casual_response(user_input))


# Run the chatbot
chatbot()
