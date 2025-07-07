VirtualAssistant Function Outputs

Below are the expected outputs for each function in the `VirtualAssistant` class, based on running each function at least once with typical input values.

## 3. `get_time()`
**Expected Output:**
```
FIFA: The current time is 03:45 PM
```

---

## 4. `get_date()`
**Expected Output:**
```
FIFA: Today is June 10, 2024
```

---

## 6. `search_wikipedia(query)`
**Input:** `search_wikipedia("Python programming language")`

**Expected Output:**
```
FIFA: Searching Wikipedia...
FIFA: According to Wikipedia:
FIFA: Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation.
```

---

## 9. `play_song(query)`
**Input:** `play_song("play Shape of You")`

**Expected Output:**
```
FIFA: Searching for the song on YouTube...
FIFA: Opening YouTube for you to play the song.
```

## 5. `get_news()`
**Expected Output:**
```
FIFA: [Title of the latest news article]
```
If API key is missing:
```
FIFA: News API key not found. Please set it in the .env file.
```

## 7. `get_weather(city)`
**Input:** `get_weather("London")`

**Expected Output:**
```
FIFA: The temperature in London is 18°C with scattered clouds
```
If API key is missing:
```
FIFA: Weather API key not found. Please set it in the .env file.
```

---

## 8. `answer_with_openai(question)`
**Input:** `answer_with_openai("What is the capital of France?")`

**Expected Output:**
```
FIFA: The capital of France is Paris.
```
If API key is missing:
```
FIFA: OpenAI API key not found. Please set it in the .env file.
```

---


---

## 10. `open_website(website)`
**Input:** `open_website("google")`

**Expected Output:**
```
FIFA: Opening Google
FIFA: Would you like to sign in to your Google account? Say yes or no
User: yes
FIFA: Opening Google sign in page
```

---

## 11. `calculate()`
**Sample Interaction:**
```
FIFA: Please enter the first number
User: 5
FIFA: Please enter the second number
User: 3
FIFA: What operation would you like to perform? Say plus, minus, multiply, or divide
User: plus
FIFA: 5.0 + 3.0 equals 8.0
```

---

## 12. `send_whatsapp_message()`
**Sample Interaction:**
```
FIFA: Please say the phone number with country code
User: 1234567890
FIFA: I heard the number as 1234567890. Is this correct? Say yes or no
User: yes
FIFA: What message would you like to send?
User: Hello from FIFA!
FIFA: Sending your message...
FIFA: Message sent successfully!
```

---

## 13. `run()`
**Sample Startup:**
```
FIFA: Hello! I'm FIFA. How can I help you?
```

**Sample Exit:**
```
FIFA: Goodbye! Have a great day!
```

---

*Note: All outputs are prefixed by the assistant's name (default: FIFA) and may vary based on user input, API responses, and system time.*