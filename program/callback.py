from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
       f"""โจ **WELCOME [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) aLLOWS YOU TO PLAY MUSIC AND VIDEO ON GROUPS THROUGH THE NEW TELEGRAM'S VIDEO CHATS!**
๐ก **FIND OUT ALL THE BOT'S COMMANDS AND HOW THEY WORK BY CLICKING ON THE ยป ๐ COMMANDS BUTTON!**
๐ **TO KNOW HOW TO USE THIS BOT, PLEASE CLICK ON THE ยป โ BASIC GUIDE BUTTON!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ BASIC GUIDE", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ COMMANDS", callback_data="cbcmds"),
                    InlineKeyboardButton("โค DONATE", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ OFFICIAL GROUP", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ OFFICIAL CHANNEl", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ SOURCE CODE", url="https://github.com/PRAGULOFFICIAL/MUSIC-BOT/"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )



@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
          f"""โ HOW TO USE THIS BOT ?, READ THE GUIDE BELOW !
1.) FIRST, ADD THIS BOT TO YOUR GROUP.
2.) THEN, PROMOTE THIS BOT AS ADMINISTRATOR ON THE GROUP ALSO GIVE ALL PERMISSIONS EXCEPT ANONYMOUS ADMIN.
3.) AFTER PROMOTING THIS BOT, TYPE /RELOAD IN GROUP TO UPDATE THE ADMIN DATA.
3.) INVITE @{ASSISTANT_NAME} TO YOUR GROUP OR TYPE /USERBOTJOIN TO INVITE HER (UNFORTUNATELY THE USERBOT WILL JOINED BY ITSELF WHEN YOU TYPE `/PLAY (SONG NAME)` OR `/VPLAY (SONG NAME)`).
4.) TURN ON/START THE VIDEO CHAT FIRST BEFORE START TO PLAY VIDEO/MUSIC.
`- END, EVERYTHING HAS BEEN SETUP -`
๐ IF THE USERBOT NOT JOINED TO VIDEO CHAT, MAKE SURE IF THE VIDEO CHAT ALREADY TURNED ON AND THE USERBOT IN THE CHAT.
๐ก IF YOU HAVE A FOLLOW-UP QUESTIONS ABOUT THIS BOT, YOU CAN TELL IT ON MY SUPPORT CHAT HERE: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("GO BACK ๐", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
ยป  CHOOSE THE MENU BELOW TO READ THE EXPLANATION & SEE THE LIST OF AVAILABLE COMMANDS !
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ทADMIN CMNDS ๐ทโโ", callback_data="cbadmin"),
                    InlineKeyboardButton("๐งSUDO CMNDS ๐ง", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("BASIC COMMANDS ๐", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""๐ฎ HERE IS THE BASIC COMMANDS:
ยป /play (SONG NAME/LINK) - PLAY MUSIC ON VIDEO CHAT
ยป /vplay (VIDEO NAME/LINK) - PLAY VIDEO ON VIDEO CHAT
ยป /vstream - PLAY LIVE VIDEO FROM YT LIVE/M3U8
ยป /playlist - SHOW YOU THE PLAYLIST
ยป /video (QUERY) - DOWNLOAD VIDEO FROM YOUTUBE
ยป /song (QUERY) - DOWNLOAD SONG FROM YOUTUBE
ยป /lyric (QUERY) - SCRAP THE SONG LYRIC
ยป /search (QUERY) - SEARCH A YOUTUBE VIDEO LINK
ยป /ping - SHOW THE BOT PING STATUS
ยป /uptime - SHOW THE BOT UPTIME STATUS
ยป /alive  - SHOW THE BOT ALIVE INFO (IN GROUP ONLY)
โก๏ธ __Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("GO BACK ๐", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:
ยป /pause - PAUSE THE STREAM
ยป /resume - RESUME THE STREAM
ยป /skip - SWITCH TO NEXT STREAM
ยป /stop - STOP THE STREAMING
ยป /vmute - MUTE THE USERBOT ON VOICE CHAT
ยป /vunmute - UNMUTE THE USERBOT ON VOICE CHAT
ยป /volume `1-200` - ADJUST THE VOLUME OF MUSIC (USERBOT MUST BE ADMIN)
ยป /reload - RELOAD BOT AND REFRESH THE ADMIN DATA
ยป /userbotjoin - INVITE THE USERBOT TO JOIN GROUP
ยป /userbotleave - ORDER USERBOT TO LEAVE FROM GROUP
โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:
ยป /gban (`USERNAME` OR `USER ID`) - FOR GLOBAL BANNED PEOPLE
ยป /ungban (`USERNAME` OR `USER ID`) - FOR UN-GLOBAL BANNED PEOPLE
ยป /speedtest - RUN THE BOT SERVER SPEEDTEST
ยป /sysinfo - SHOW THE SYSTEM INFORMATION
ยป /update - UPDATE YOUR BOT TO LATEST VERSION
ยป /restart - RESTART YOUR BOT
ยป /leaveall - ORDER USERBOT TO LEAVE FROM ALL GROUP
ยป /leavebot (`CHAT ID`) - ORDER BOT TO LEAVE FROM THE GROUP YOU SPECIFY
ยป /eval - EXECUTE ANY CODE
ยป /sh - RUN ANY COMMAND
ยป /broadcast (`message`) -  SEND A BROADCAST MESSAGE TO ALL GROUPS ENTERED BY BOT
ยป /broadcast_pin (`message`) - SEND A BROADCAST MESSAGE TO ALL GROUPS ENTERED BY BOT WITH THE CHAT PIN
โก __Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("GO BACK ๐", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ONLY ADMIN WITH MANAGE VIDEO CHAT PERMISSION THAT CAN TAP THIS BUTTON !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **SETTINGS OF** {CHAT}\n\nโธ : PAUSE STREAM\nโถ๏ธ : RESUME STREAM\n๐ : MUTE USERBOT\n๐ : UNMUTE USERBOT\nโน : STOP STREAM",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("โ NOTHING IS CURRENTLY STREAMING", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ONLY ADMIN WITH MANAGE VIDEO CHAT PERMISSION THAT CAN TAP THIS BUTTON !", show_alert=True)
    await query.message.delete()
