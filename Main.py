import discord
import os
import random

client = discord.Client()

im_varients = ["I'm", "i'm", 'Im', "IM", "Im", "I'M"]
dad_varients = ["dad", "Dad", "PaPa", "papa"]
cursed_words = ["Daddy", "daddy", "dady", "Dady"]
responces_general = [
                    "Rome did not create a great empire by having meetings, they did it by killing all people who opposed them.",
                    "Doing a job RIGHT the first time gets the job done. Doing the job WRONG fourteen times gives you job security.",
                    "Eagles may soar, but weasels don’t get sucked into jet engines.",
                    "If at first you don’t succeed, try management.",
                    "Never put off until tomorrow what you can avoid altogether.",
                    "TEAMWORK…means never having to take all the blame yourself.",
                    "Go the extra mile. It makes your boss look like an incompetent slacker",
                    "When the going gets tough, the tough take a coffee break.",
                    "What’s brown and sticky? A stick.",
                    "Two guys walked into a bar. The third guy ducked.",
                    "Why are elevator jokes so classic and good? They work on many levels.",
                    "What did the police officer say to his belly-button? You’re under a vest.",
                    "What kind of drink can be bitter and sweet? Reali-tea.",
                    "Want to know why nurses like red crayons? Sometimes they have to draw blood.",
                    "My wife asked me to go get 6 cans of Sprite from the grocery store. I realized when I got home that I had picked 7 up.",
                    "Why is Peter Pan always flying? Because he Neverlands."
                    ]
found = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Discord event system, sets up a reciver for an message event.
@client.event
async def on_message(message):
    #Prevents messaging to own message
    if message.author == client.user:
        return
    msg = message.content
    sentance = msg.split()

    #Checks the message for any of the words in Intro varient
    for word in sentance:
        #Hi back joke generator
        if word in im_varients: 
            index = sentance.index(word)
            output = "Hi " + sentance[index + 1] + " I'm dad!"
            await message.channel.send(output)
            return

        #Condones the use of certain words
        #TODO - put users in the shamebox for using the word Daddy 
        if word in cursed_words:
            await message.channel.send("No") 
            return
        
        #if the word "dad" is found at all in any message, send a joke responce 
        #(mix of bad inspirational quotes and dad jokes)
        if word in dad_varients:
            await message.channel.send(random.choice(responces_general))
            return


#Client.Run is refering to the discord client, this is what will tell the bot to go. 
#os.getenv will search the .env (simmilar to config files in other languages) to get the token
client.run(os.getenv('TOKEN'))
