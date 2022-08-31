from telethon import TelegramClient, events

api_id = 4455656
api_hash = 'tyutuutu'

with open("hash.txt", "r") as f:
    api_hash = f.read()


client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    print(chat_id)
    print(event.raw_text)


client.start()
client.run_until_disconnected()
