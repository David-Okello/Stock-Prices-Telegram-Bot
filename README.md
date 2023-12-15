# Telegram Stock Bot

This Python script implements a simple Telegram bot using the Telebot library to provide stock-related information. The bot retrieves stock data from Yahoo Finance using the yfinance library.

## Prerequisites

Before running the script, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install telebot yfinance
```

## Configuration
1. API Key and Environment Variables:

The bot requires certain environment variables to be set for API keys and social media usernames. Ensure you have the following environment variables configured:
    
    API_KEY: Telegram bot API key
    github: GitHub username
    instagram: Instagram username
    twitter: Twitter username
    replit: Repl.it username

2. Telegram Bot:

Create a new Telegram bot and obtain the API key. Set the API_KEY environment variable with this key.

## Usage
1. Run the script using the following command:
```bash
python your_script_name.py 
```
2. Interact with the bot on Telegram using the following commands:
    ```
    /start: Introduction and list of available commands.
    /greet: Receive a greeting response.
    /getstocks: Get stock data for hardcoded stocks (tsla, gme, amc, nok).
    price stockname: Get 5-minute period and 1-minute interval stock data for the specified stock.
    ```
## Disclaimer
This script is a basic implementation and may require further enhancements for production use. Use it responsibly, and ensure compliance with the terms of service of the external APIs used.

Feel free to contribute, report issues, or suggest improvements.

```bash 
Replace `your_script_name.py`, `your_github_username`, `your_twitter_username`, `your_instagram_username`, and `your_replit_username` with appropriate values. Additionally, include relevant links to your social media profiles in the README.
```