# © @GREATPERSON_XD
from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url("𝗔𝗗𝗗 𝗠𝗘 𝗕𝗔𝗕𝗬", "https://t.me/{BOT_USERNAME}?startgroup=true")
    ],
    [
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/THE_INCRICIBLE"),
        Button.url("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", "https://t.me/INCRICIBLE")
    ],
    [
        Button.inline("𝗛𝗘𝗟𝗣 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ \n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⦿ 24x7 ʀᴜɴ|[ɢʀᴇᴀᴛᴘᴇʀꜱᴏɴ](https://t.me/GREATPERSON_XD)\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/1fbfcd39ef25dd99fb5b7.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
