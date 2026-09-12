<div align="center">
  <img src="hangman.png" alt="Hangyman logo" width="140" />
  <h1>Hangyman</h1>
  <p><b>Play Hangman with your friends inside a Discord server.</b><br/>A Python + discord.py bot that runs a classic guess-the-word game, ported from a command-line hangman script.</p>
  <p>
    <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
    <img alt="discord.py" src="https://img.shields.io/badge/discord.py-5865F2?logo=discord&logoColor=white">
  </p>
</div>

---

Hangyman is a Discord bot that plays **Hangman** in your server. It started life as a
command-line Python game and grew into a bot so friends could play together in a channel.
Someone starts a round, everyone guesses letters (or the whole word), and you have a fixed
number of wrong guesses before the game is lost.

## Features

- **Play in any channel** — type `.` in a text channel to start a new round.
- **Letter or full-word guesses** — guess one letter at a time or attempt the whole word.
- **Seven lives** — each wrong guess costs a life; the game ends when the word is solved or lives run out.
- **Progress display** — the bot shows the word with revealed letters and blanks, plus the letters already tried.
- **Quit anytime** — send `exit` during a game to stop the current round.
- **Bundled word list** — ships with a word list in [`words.py`](words.py) (German words), easy to extend or replace.

## Tech stack

- **Python 3**
- **[discord.py](https://discordpy.readthedocs.io/)** — the Discord API wrapper
- Standard library `random` and `asyncio`

## Getting started

### 1. Create a Discord bot

1. Open the [Discord Developer Portal](https://discord.com/developers/applications) and create a **New Application**.
2. Go to **Bot** → **Add Bot**, then copy the bot **token**.
3. Under **Privileged Gateway Intents**, enable **Message Content Intent** so the bot can read messages.
4. Invite the bot to your server via **OAuth2 → URL Generator** (scope `bot`, with permission to read and send messages).

### 2. Install dependencies

```bash
git clone https://github.com/olivierluethy/Hangyman-Discord.py.git
cd Hangyman-Discord.py
pip install discord.py
```

### 3. Add your token

Open `main.py` and set the `TOKEN` value to your bot token:

```python
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
```

> Keep your token secret. Prefer loading it from an environment variable rather than
> committing it to source control.

### 4. Run the bot

```bash
python main.py
```

When it connects you'll see `We have logged in as ...` in the console, and the bot's
status will read **"Enter . to play!"**.

## How to play

1. In a channel the bot can see, send `.` to start a game.
2. When prompted, reply with a **letter** or a **full word**.
3. Keep guessing — each wrong guess costs one of your seven lives.
4. Solve the word to win, or send `exit` to stop the round.

## License

Released under the [MIT License](LICENSE) © 2026 Olivier Lüthy. You're free to use, modify and distribute this
software, including commercially, as long as the copyright notice and license are included.

## Author

Built by **Olivier Lüthy** — [GitHub](https://github.com/olivierluethy).
