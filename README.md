# Kageki - Discord Bot 🌧️

A feature-rich Discord bot built with discord.py that provides weather information, user utilities, and fun commands.

## 🌟 Features

### Available Commands

- **`/rain`** - Sends a rain GIF animation
- **`/http-code`** - Returns a random HTTP status code with a cat image
- **`/avatar <member>`** - Displays a user's avatar
- **`/info <member>`** - Shows detailed information about a Discord user
- **`/air-quality <city>`** - Gets the air quality index (AQI) for a specified city

### Bot Status
The bot displays a custom streaming status: "𝑾𝒂𝒕𝒄𝒉𝒊𝒏𝒈 𝒕𝒉𝒆 𝒓𝒂𝒊𝒏 ☔" with DND (Do Not Disturb) status.

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Discord Developer Application & Bot Token
- Air Quality API Token from [World Air Quality Index](https://waqi.info/api/)

### Required Python Packages

Install the following packages using pip:

```bash
pip install discord.py python-dotenv requests
```

### Configuration

1. **Create a `.env` file** in the project root directory:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   WEATHER_API_KEY=your_waqi_api_token_here
   ```

2. **Discord Bot Setup:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section
   - Create a bot and copy the token
   - Enable all necessary intents (the bot uses `discord.Intents.all()`)

3. **Air Quality API Setup:**
   - Visit [WAQI API](https://waqi.info/api/)
   - Register for a free API token
   - Add the token to your `.env` file

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd DiscordBot
   ```

2. Create and configure your `.env` file (see Configuration section above)

3. Install dependencies:
   ```bash
   pip install discord.py python-dotenv requests jsonpath-ng
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
DiscordBot/
├── main.py              # Main bot file with commands and event handlers
├── weatherAPI.py        # Air quality API integration
├── embedMessages.py     # Discord embed message utilities
├── .env                 # Environment variables (not included in repo)
├── .gitignore          # Git ignore file
├── README.md           # This file
└── assets/
    └── gif/
        └── rain.gif    # Rain animation for /rain command
```

## 🔧 File Descriptions

### `main.py`
The main bot file containing:
- Bot initialization and configuration
- All slash command implementations
- Event handlers for message logging
- Logging functionality for command usage

### `weatherAPI.py`
Handles air quality data:
- Fetches AQI data from World Air Quality Index API
- Converts numeric AQI values to descriptive categories
- Categories: good, moderate, unhealthy for sensitive groups, unhealthy, very unhealthy, hazardous

### `embedMessages.py`
Creates rich Discord embeds:
- User information displays with avatars
- Formatted user data including username, ID, and account creation date

## 🎯 Usage Examples

### Getting User Information
```
/info @username
```
Returns an embed with:
- User's display name and avatar
- Username and User ID
- Account creation date

### Checking Air Quality
```
/air-quality paris
/air-quality new-york
```
Returns the current air quality index and category for the specified city.

### Fun Commands
```
/rain          # Sends a rain GIF
/http-code     # Random HTTP status code with cat image
/avatar @user  # Shows user's avatar
```

## 🛠️ Development

### Adding New Commands

To add a new slash command, use the following pattern in `main.py`:

```python
@client.tree.command(name="command-name", description="Command description")
async def slash_command(interaction: discord.Integration, parameter: type):
    log("/command-name", interaction)
    # Your command logic here
    return await interaction.response.send_message("Response")
```

### Environment Variables

The bot expects these environment variables in your `.env` file:
- `DISCORD_TOKEN`: Your Discord bot token
- `WEATHER_API_KEY`: Your WAQI API token

## 📝 Logging

The bot includes comprehensive logging:
- All messages are logged with timestamp and author
- Command usage is tracked with user and server information
- Private message vs. server message distinction

## 🔒 Security

- Sensitive tokens are stored in environment variables
- `.env` file is excluded from version control via `.gitignore`
- Bot ignores its own messages to prevent loops

## 📋 Air Quality Index Categories

| AQI Range | Category |
|-----------|----------|
| 0-50 | Good |
| 51-100 | Moderate |
| 101-150 | Unhealthy for Sensitive Groups |
| 151-200 | Unhealthy |
| 201-300 | Very Unhealthy |
| 301+ | Hazardous |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is open source. Please check with the repository owner for specific license information.

## 👤 Author

**Kageki#9156** - Version 0.1

---

*Made with ❤️ using discord.py*  
