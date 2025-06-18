# FIFA Virtual Assistant

A Python-based virtual assistant named FIFA that can perform various tasks through voice commands.

## Features

- Voice command recognition
- Time and date information
- Weather updates
- Wikipedia searches
- News updates
- YouTube song playback
- Website opening
- Mathematical calculations
- WhatsApp messaging
- OpenAI-powered question answering

## Requirements

- Python 3.8 or higher
- Required Python packages (see requirements.txt)
- API keys for:
  - OpenWeatherMap (Weather API)
  - News API
  - OpenAI API
- WhatsApp Web setup for messaging functionality

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fifa-virtual-assistant.git
cd fifa-virtual-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API keys:
```
WEATHER_API_KEY=your_weather_api_key
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
```

4. Run the assistant:
```bash
python virtual_assistant.py
```

## Usage

The assistant responds to various voice commands:

- "What time is it?" - Get current time
- "What's today's date?" - Get current date
- "Weather in [city]" - Get weather information
- "Wikipedia [topic]" - Search Wikipedia
- "What's the news?" - Get latest news
- "Play [song name]" - Play song on YouTube
- "Open [website]" - Open specified website
- "Calculate" - Perform mathematical calculations
- "Send WhatsApp message" - Send WhatsApp message
- "Ask [question]" - Get answer using OpenAI

## Contributing

Feel free to submit issues and enhancement requests! 