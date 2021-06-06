from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CVq1hZgABAX7-YLsut_f48vHDZ4ltdMhKgvfxLF4AAksBAAOtKVT0XH4wyum0PB4E")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [BUJEL](https://t.me/n0tus3rn4m3).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Contact Me 📩", url="https://t.me/n0tus3rn4m3")
                ],[
                    InlineKeyboardButton(
                        "🌀 Powered", url="https://t.me/QintilQuda"
                    ),     
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/VcgMusicGroup"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/QintilQuda"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Bujel_MusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/QintilQuda")
                ]
            ]
        )
   )


