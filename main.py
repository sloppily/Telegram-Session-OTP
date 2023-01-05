from telethon import TelegramClient, events
import tkinter
from tkinter.filedialog import askopenfilename
tkinter.Tk().withdraw()
from colorama import Fore, Back, Style, init
init(convert=True)
import toml, os, logging, asyncio, re, sys

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )

print(f"""{Fore.LIGHTMAGENTA_EX}
                        _             _ ____     
   ________  __________(_)___  ____  (_) __/_  __
  / ___/ _ \/ ___/ ___/ / __ \/ __ \/ / /_/ / / /
 (__  )  __(__  |__  ) / /_/ / / / / / __/ /_/ / 
/____/\___/____/____/_/\____/_/ /_/_/_/  \__, /  
                                        /____/ {Fore.RESET}
made by {Fore.LIGHTMAGENTA_EX}abductee {Fore.RESET}/ {Fore.LIGHTMAGENTA_EX}@temp992{Fore.RESET}
""")

filename = askopenfilename()

with open("assets/config.toml") as f:
    config = toml.loads(f.read())

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]

client = TelegramClient(
	session=filename,
	api_id=api_id,
	api_hash=api_hash
)

async def main():

    me =  await client.get_me()
    print(f"this sessions number is {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{me.phone}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}\n")



with client:
    client.loop.run_until_complete(client.send_message('me', 'Activity Ping'))
    client.loop.run_until_complete(main())

@client.on(events.NewMessage)
async def my_event_handler(event):
    if "Do not give this code to anyone" in event.raw_text:
            
        temp = re.findall(r'\d+', event.raw_text)
        code = list(map(int, temp))
            
        print(f"your verification code is {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{code[0]}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}")

client.start()
client.run_until_disconnected()