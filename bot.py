import time 
from colorama import init
from termcolor import colored

init()

print(colored("\n\nTelegram bot creator 1.0.0\nby Anddows\n\n", "red"))

while True:
            inpt = input('*>_ ')
            inpt = inpt.strip()
            if inpt == '{c = telebot.python}':
              token = input("{*>_} your token > ")    
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f"import telebot\n\nbot = telebot.TeleBot('{token}')")
              print(colored('{*>_} successfully', "green"))
              command1 = input("{*>_} your command > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(commands = ['{command1}'])\ndef {command1}_message(message):")
              print(colored('{*>_} successfully', 'green'))

            elif inpt == '{s = commands}':
              command2 = input("{*>_} your command > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(commands = ['{command2}'])\ndef {command2}_message(message):")
              print(colored('{*>_} successfully', 'green'))

            elif inpt == '{bot = w.reply}':
              commandreply = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.reply_to(message, "{commandreply}")')
              print(colored('{*>_} successfully', 'green'))
              #function 
            elif inpt == "{bot = message['text']}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\n@bot.message_handler(content_types = ['text'])\ndef send_message(message):")
              print(colored('{*>_} successfully', 'green'))


              #if 
            elif inpt == "{bot == if}":
              commandif = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   if message.text.lower() == "{commandif}":')
              print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot == send}":
              commandsend = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n        bot.send_message(message.chat.id, "{commandsend}")')
              print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot == elif}":
              commandif2 = input("{*>_} your text > " )
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f'\n\n   elif message.text.lower() == "{commandif2}":')
              print(colored('{*>_} successfully', 'green'))

            elif inpt == "{bot.run = True}":
              print(colored('{*>_} Scanning...', 'red'))
              time.sleep(5)
              with open('bot1.py', 'a') as f:
                 f.write(f"\n\nbot.polling(none_stop = True)")
              print(colored('{*>_} successfully', 'green'))

            else:
              print(colored(f'*>_ CommandError: command <{inpt}> not defined', 'red'))
            
           