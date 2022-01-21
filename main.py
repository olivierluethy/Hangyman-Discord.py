import discord
import random
from discord import user
from words import words
from discord.ext import commands
import asyncio

TOKEN = '__REDACTED_DISCORD_TOKEN__'

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    # Setting status
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Enter . to play!"))


@client.event
async def on_message(message):
    # Random Word
    word = random.choice(words)

    # Anzahl Leben
    allowed_errors = 7

    # All guesses are going in this list
    user_guesses = list()

    # To format the output of all user guesses
    user_guessess = ""

    # Space between guess parts
    space = "----------------"

    # To check if the word has been
    done = False

    # If user wants to exit
    exit = False

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel}')

    if message.author == client.user:
        return

    if user_message.lower() == '.':
        while not done and exit == False:

            await message.channel.send('Guess a word or a letter')
            guess = await client.wait_for("message")

            if guess.content.lower() == "exit":
                exit = True
                await message.channel.send('Game has stopped')
                break

            if guess.content.lower() in user_guesses:
                await message.channel.send("Please choose an other word or letter!")
            else:
                progress_word = ""

                for c in word.lower():
                    if guess.content.lower() == c or c in user_guesses:
                        progress_word += c
                    else:
                        progress_word += "\_ "

                user_guesses.append(guess.content.lower())

                user_guessess += guess.content.lower() + " "

                if guess.content.lower() not in word.lower():
                    allowed_errors = allowed_errors - 1

                if guess.content.lower() == word or progress_word == word:
                    await message.channel.send(f"Correct. You won. The word was {word}.")
                    done = True
                else:
                    if allowed_errors == 0:
                        await message.channel.send(f"You lost! The word was {word}.")
                        break
                    else:
                        await message.channel.send("Progress: %s" % progress_word)
                        await message.channel.send(f"Allowed errors: {allowed_errors}")
                        await message.channel.send(f"Guessed letters: {user_guessess}")
                        await message.channel.send(space)
                        done = False

client.run(TOKEN)
