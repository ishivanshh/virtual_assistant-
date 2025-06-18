import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import requests
import json
import os
from dotenv import load_dotenv
import openai
import webbrowser
from pytube import YouTube
import re
import pywhatkit as kit
import csv

class VirtualAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Load environment variables
        load_dotenv()
        
        # Create data directory if it doesn't exist
        if not os.path.exists('assistant_data'):
            os.makedirs('assistant_data')
            
        # Load or create user preferences
        self.preferences_file = 'assistant_data/preferences.json'
        self.load_preferences()

    def load_preferences(self):
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, 'r') as f:
                self.preferences = json.load(f)
        else:
            self.preferences = {
                'name': 'FIFA',
                'user_name': 'User',
                'voice_id': None
            }
            self.save_preferences()

    def save_preferences(self):
        with open(self.preferences_file, 'w') as f:
            json.dump(self.preferences, f, indent=4)

    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.preferences['name']}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen for user input"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio)
                print(f"{self.preferences['user_name']}: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("No speech detected within timeout period.")
                return ""
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Could you repeat?")
                return ""
            except sr.RequestError:
                self.speak("Sorry, there was an error with the speech recognition service.")
                return ""
            except Exception as e:
                self.speak("Sorry, there was an error. Please try again.")
                return ""

    def get_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")

    def get_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        self.speak(f"Today is {current_date}")

    def get_news(self):
        """Get the latest news"""
        api_key = os.getenv('NEWS_API_KEY')
        if not api_key:
            self.speak("News API key not found. Please set it in the .env file.")
            return
            
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            if data["status"] == "ok" and data["articles"]:
                self.speak(data["articles"][0]["title"])
            else:
                self.speak("Sorry, I couldn't fetch the latest news.")
        except Exception as e:
            self.speak("Sorry, there was an error getting the news.")

    def search_wikipedia(self, query):
        """Search Wikipedia for information"""
        try:
            self.speak("Searching Wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia:")
            self.speak(results)
        except Exception as e:
            self.speak("Sorry, I couldn't find that information on Wikipedia.")

    def get_weather(self, city):
        """Get weather information for a city"""
        api_key = os.getenv('WEATHER_API_KEY')
        if not api_key:
            self.speak("Weather API key not found. Please set it in the .env file.")
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                self.speak(f"The temperature in {city} is {temp}°C with {weather}")
            else:
                self.speak("Sorry, I couldn't get the weather information.")
        except Exception as e:
            self.speak("Sorry, there was an error getting the weather information.")

    def answer_with_openai(self, question):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            self.speak("OpenAI API key not found. Please set it in the .env file.")
            return
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            answer = response.choices[0].message.content.strip()
            self.speak(answer)
        except Exception as e:
            self.speak("Sorry, I couldn't get an answer from OpenAI.")

    def play_song(self, query):
        """Play a song from YouTube based on the query"""
        try:
            self.speak("Searching for the song on YouTube...")
            search_query = query.replace("play", "").strip()
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            self.speak("Opening YouTube for you to play the song.")
        except Exception as e:
            self.speak("Sorry, I couldn't play the song.")

    def open_website(self, website):
        """Open specified website"""
        try:
            if "google" in website.lower():
                webbrowser.open("https://www.google.com")
                self.speak("Opening Google")
            elif "instagram" in website.lower():
                webbrowser.open("https://www.instagram.com")
                self.speak("Opening Instagram")
            elif "linkedin" in website.lower():
                webbrowser.open("https://www.linkedin.com")
                self.speak("Opening LinkedIn")
            elif "spotify" in website.lower():
                webbrowser.open("https://open.spotify.com")
                self.speak("Opening Spotify")
        except Exception as e:
            self.speak("Sorry, I couldn't open the website.")

    def calculate(self):
        """Perform mathematical calculations with interactive input"""
        try:
            # Get first operand
            self.speak("Please enter the first number")
            operand1 = self.listen()
            if not operand1:
                return
            operand1 = float(operand1)

            # Get second operand
            self.speak("Please enter the second number")
            operand2 = self.listen()
            if not operand2:
                return
            operand2 = float(operand2)

            # Get operation
            self.speak("What operation would you like to perform? Say plus, minus, multiply, or divide")
            operation = self.listen()
            if not operation:
                return

            # Perform calculation based on operation
            result = None
            if "plus" in operation.lower() or "add" in operation.lower():
                result = operand1 + operand2
                operation_symbol = "+"
            elif "minus" in operation.lower() or "subtract" in operation.lower():
                result = operand1 - operand2
                operation_symbol = "-"
            elif "multiply" in operation.lower() or "times" in operation.lower():
                result = operand1 * operand2
                operation_symbol = "×"
            elif "divide" in operation.lower():
                if operand2 == 0:
                    self.speak("Sorry, cannot divide by zero")
                    return
                result = operand1 / operand2
                operation_symbol = "÷"
            else:
                self.speak("Sorry, I don't understand that operation")
                return

            # Speak the result
            self.speak(f"{operand1} {operation_symbol} {operand2} equals {result}")

        except ValueError:
            self.speak("Sorry, please enter valid numbers")
        except Exception as e:
            self.speak("Sorry, I couldn't perform the calculation")

    def send_whatsapp_message(self):
        """Send WhatsApp message using phone number with verification"""
        while True:
            try:
                # Get phone number
                self.speak("Please say the phone number with country code")
                phone_number = self.listen()
                if not phone_number:
                    continue
                
                # Clean the phone number
                phone_number = ''.join(filter(str.isdigit, phone_number))
                
                # Verify the number
                self.speak(f"I heard the number as {phone_number}. Is this correct? Say yes or no")
                verification = self.listen()
                
                if not verification:
                    continue
                    
                if "no" in verification.lower():
                    self.speak("Let's try entering the number again.")
                    continue
                elif "yes" in verification.lower():
                    # Get message
                    self.speak("What message would you like to send?")
                    message = self.listen()
                    if not message:
                        continue
                    
                    # Send message
                    self.speak("Sending your message...")
                    kit.sendwhatmsg_instantly(
                        phone_no=f"+{phone_number}",
                        message=message,
                        wait_time=10,
                        tab_close=True
                    )
                    self.speak("Message sent successfully!")
                    break
                else:
                    self.speak("Please say yes or no to confirm the number.")
                    continue
                
            except Exception as e:
                self.speak("Sorry, I couldn't send the WhatsApp message. Please make sure you have WhatsApp Web set up and the phone number is correct.")
                self.speak("Would you like to try again? Say yes or no")
                retry = self.listen()
                if not retry or "no" in retry.lower():
                    break

    def run(self):
        """Main loop for the virtual assistant"""
        self.speak(f"Hello! I'm {self.preferences['name']}. How can I help you?")
        
        while True:
            command = self.listen()
            
            if not command:
                continue
                
            if "exit" in command or "goodbye" in command:
                self.speak("Goodbye! Have a great day!")
                break
                
            elif "time" in command:
                self.get_time()
                
            elif "date" in command:
                self.get_date()
                
            elif "wikipedia" in command:
                query = command.replace("wikipedia", "").strip()
                if query:
                    self.search_wikipedia(query)
                else:
                    self.speak("What would you like to search for?")
                    
            elif "weather" in command:
                city = command.replace("weather in", "").replace("weather", "").strip()
                if city:
                    self.get_weather(city)
                else:
                    self.speak("Which city's weather would you like to know?")
            elif "news" in command.lower():
                self.get_news()
            elif "play" in command.lower():
                self.play_song(command)
            elif "calculate" in command.lower():
                self.calculate()
            elif "google" in command.lower():
                self.open_website("google")
            elif "instagram" in command.lower():
                self.open_website("instagram")
            elif "linkedin" in command.lower():
                self.open_website("linkedin")
            elif "spotify" in command.lower():
                self.open_website("spotify")
            elif "whatsapp" in command.lower() or "send message" in command:
                self.send_whatsapp_message()
            elif "help" in command:
                self.speak("I can help you with: 1). Date and Time 2). News 3). Play songs 4). Weather 5). Wikipedia 6). Calculate 7). OpenAI 8). Open websites (Google, Instagram, LinkedIn, Spotify) 9). Send WhatsApp messages 10). Just ask me what you need!")
            else:
                self.answer_with_openai(command)

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()  

