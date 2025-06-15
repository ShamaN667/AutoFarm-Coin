
from telethon.sync import TelegramClient
import asyncio, time

api_id = 24672908
api_hash = 'baa672aca754ae942370318edc6fa58c'
session = 'sessions/anon1.session'
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
            await client.send_message(group_id, f'[anon1] Бонус #{counter} отправлен')
        except Exception as e:
            await client.send_message(group_id, f'[anon1] Ошибка: {e}')
        await asyncio.sleep(3600)

with client:
    client.loop.run_until_complete(main())
