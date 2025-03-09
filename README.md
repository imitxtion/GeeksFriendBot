# Multifunctional Telegram Bot
> [!WARNING]
> This project is no longer being maintained.


A versatile Telegram bot built with Python and Aiogram 2.0. It uses SQLite for data storage and provides multiple useful functionalities in one package.

## Features

### Latest Anime News
Stay updated with the latest anime news in just one click.

### Anime Finder
Find anime titles by uploading a screenshot.

### To-do List Management
Create, update, and manage your personal to-do list.

### Chat with ChatGPT
Interact with ChatGPT directly within Telegram.

### TikTok Video Downloader
Download TikTok videos without watermarks by simply sending a link.

### TikTok Hashtags Generator
Generate trending hashtags for TikTok videos.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/multifunctional-telegram-bot.git
    cd multifunctional-telegram-bot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file:
    ```env
    TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key
    RAPIDAPI_KEY=your_rapidapi_key
    SAUCENAO_API_KEY=your_saucenao_api_key
    CLIENT_ID=your_reddit_client_id
    CLIENT_SECRET=your_reddit_client_secret
    USER_AGENT=your_reddit_user_agent
    ADMIN_ID=your_telegram_admin_id
    ```

5. Initialize the database:
    ```sh
    python -c "from database.db import Database; Database('database/database.db')"
    ```

## Usage

Run the bot:
```sh
python main.py
```
