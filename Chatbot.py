import requests

def get_weather(city="Las Vegas"):
    """Fetches real-time weather data for a given city."""
    api_key = "your_api_key"  # Replace with a valid API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The current weather in {city} is {temp}°F with {description}."
        else:
            return "Sorry, I couldn't fetch the weather. Please check a weather app."
    except Exception as e:
        return "Error retrieving weather data."

def chatbot():
    """A chatbot that responds to basic queries and retrieves real-world data."""
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
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")
            
# Run the chatbot
chatbot()
