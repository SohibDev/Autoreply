from telethon import TelegramClient, events
from telethon.tl.types import User, InputDocument
import json
import os
import time

# API ma'lumotlari
api_id = 24741875
api_hash = '338aa56d049877498dd27266d272d6c7'

# Clientni yaratamiz
client = TelegramClient('anon', api_id, api_hash)

# Foydalanuvchilar ro‘yxatini saqlash uchun fayl
USER_FILE = 'sent_users.json'

if not os.path.exists(USER_FILE):
    with open(USER_FILE, 'w') as f:
        json.dump({}, f)  # list emas, dict

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    if not isinstance(sender, User):
        return

    user_id = str(sender.id)

    with open(USER_FILE, 'r') as f:
        users = json.load(f)

    now = time.time()
    last_time = users.get(user_id, 0)

    if now - last_time > 86400:  # 24 soatdan keyin
        # 1. Sticker yuborish
        await client.send_file(sender.id, InputDocument(
            id=1678292242239848466,
            access_hash=-9035853454252166357,
            file_reference=b''
        ))

        # 2. Matn 1
        message1 = (
            "👋 Assalomu alaykum, hurmatli mijoz!\n\n"
            "Tez orada operatorlarimiz Siz bilan bog‘lanishadi.\n"
            "Agar kutishni istamasangiz, @onlinexizmat_bot ga murojaatingizni yozib qoldirishingiz mumkin.\n"
            "Shuningdek, @ASRXIZMATLARI Kanalimizga obuna bo‘lib, operator javobini kuting 😊."
        )
        await client.send_message(sender.id, message1)

        # 3. Matn 2
        message2 = (
            "📞 Agar botga yozishni istamasangiz:\n\n"
            "📞 +998557012100\n"
            "📞 +998992231112\n\n"
            "Yuqorida ko‘rsatilgan raqamlarimizga to‘g'ridan-to‘g'ri aloqaga chiqishingiz mumkin 😊"
        )
        await client.send_message(sender.id, message2)

        # Vaqtni yangilash
        users[user_id] = now
        with open(USER_FILE, 'w') as f:
            json.dump(users, f)

# Clientni ishga tushirish
client.start()
print("🤖 Userbot ishga tushdi...")
client.run_until_disconnected()
