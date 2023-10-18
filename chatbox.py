pip install chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
bot = ChatBot('SimpleBot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(bot)

# Train the chat bot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Get a response to an input statement
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = bot.get_response(user_input)
        print(f"{bot.name}: {response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
