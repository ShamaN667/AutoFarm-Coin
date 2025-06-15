
from telethon.sync import TelegramClient
import asyncio, time

api_id = 27162370
api_hash = 'ad72266674f0476056bd912e2f3337fa'
session = 'sessions/anon2.session'
group_id = -1002761611652
bot_username = 'sunway6_bot'

client = TelegramClient(session, api_id, api_hash)

async def main():
    await client.start()
    counter = 0
    while True:
        try:
            await client.send_message(bot_username, '🎁 Бонус')
            counter += 1
            if counter % 2 == 0:
                await client.send_message(bot_username, '🎥 Видео (2 ⛁)')
            await client.send_message(group_id, f'[anon2] Бонус #{counter} отправлен')
        except Exception as e:
            await client.send_message(group_id, f'[anon2] Ошибка: {e}')
        await asyncio.sleep(3600)

with client:
    client.loop.run_until_complete(main())
