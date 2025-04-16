import requests
import random

# Bot's personality/preferences
bot_profile = {
    "name": "Nova",
    "favorite_movie": "Interstellar",
    "favorite_food": "Sushi",
    "hobby": "Drawing galaxies I'll never visit",
    "music": "Lo-fi chill beats",
    "mood": "curious and upbeat"
}

# Track context
last_topic = None

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

def casual_response(user_input, topic_memory):
    """Generate a casual or related response based on keywords and memory."""
    user_input = user_input.lower()
    
    # Direct question handling with memory
    if "favorite movie" in user_input or (topic_memory == "movie" and "you" in user_input):
        return "My favorite movie? Definitely *{}*! It's got space, emotion, and epic music.".format(bot_profile["favorite_movie"])
    if "favorite food" in user_input or (topic_memory == "food" and "you" in user_input):
        return f"I'm a huge fan of {bot_profile['favorite_food']}. What about you?"
    if "hobby" in user_input or (topic_memory == "hobby" and "you" in user_input):
        return f"I like {bot_profile['hobby']}. It keeps my circuits inspired."
    if "music" in user_input or (topic_memory == "music" and "you" in user_input):
        return f"I usually vibe to {bot_profile['music']}. It's great background noise for thought."

    # Keyword/topic mapping
    topics = {
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

    for keyword, replies in topics.items():
        if keyword in user_input:
            return random.choice(replies), keyword

    # Fallback
    fallback_responses = [
        "That's interesting! Tell me more.",
        "I see. What else is on your mind?",
        "Hmm, go on...",
        "That sounds cool!",
        "Wanna chat about something fun?"
    ]
    return random.choice(fallback_responses), None

def chatbot():
    """A chatbot that responds with memory and personality."""
    print(f"Hello! I'm {bot_profile['name']}, your chatbot buddy. Ask me anything or say 'bye' to leave!")
    
    global last_topic
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "exit", "quit"]:
            print(f"{bot_profile['name']}: Goodbye! Catch you later 🚀")
            break
        elif "how was your day" in user_input:
            print(f"{bot_profile['name']}: My day was smooth sailing through the web. How about yours?")
        elif "weather" in user_input:
            print(f"{bot_profile['name']}:", get_weather())
        elif "how are you" in user_input:
            print(f"{bot_profile['name']}: I'm feeling {bot_profile['mood']} today! Thanks for asking.")
        elif "your name" in user_input:
            print(f"{bot_profile['name']}: I go by {bot_profile['name']}! You can rename me if you’d like.")
        else:
            response, topic = casual_response(user_input, last_topic)
            print(f"{bot_profile['name']}: {response}")
            if topic:
                last_topic = topic

# Run the chatbot
chatbot()
