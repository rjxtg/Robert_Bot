#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://paisakamalo.in/')
    START_TXT = environ.get("START_TXT", "✨ Hᴇʟʟᴏ {},    
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ."
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪꜱ ᴍʏ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅꜱ."""
    ABOUT_TXT = """<b>✯ ᴍʏ ɴᴀᴍᴇ: {}</b>
<b>✮ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/CK_offical>RJ</a></b>
<b>✮ ʟɪʙʀᴀʀʏ: ᴘʀᴏɢʀᴀᴍ</b>
<b>✮ ʟᴀɴɢᴜᴀɢᴇ:  ᴘʏᴛʜᴏɴ 𝟹</b>
<b>✮ ᴅᴀᴛᴀ ʙᴀsᴇ: ᴍᴏɴɢᴏ ᴅʙ</b>
<b>✮ ʙᴏᴛ sᴇʀᴠᴇʀ: <a href=tg://settings>ᴘʀɪᴠᴀᴛᴇ</a></b>
<b>✮ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v4.5 [ sᴛᴀʙʟᴇ ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
ᴛʜɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ
»sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ~ ᴘʀɪᴠᴀᴛᴇ 🤒"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᎯℕUℛᎯᎶ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Am_RoBots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᎯℕUℛᎯᎶ

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs : <code>{}</code>
◉ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ : <code>{}</code> MB
◉ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ : <code>{}</code> MB"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝙂𝙍𝙊𝙐𝙋 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝙏𝙊𝙏𝘼𝙇 𝙈𝙀𝙈𝘽𝙀𝙍𝙎 ⪼ <code>{}</code></b>
<b>᚛› 𝘼𝘿𝘿𝙀𝘿 𝘽𝙔 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝙄𝘿 - <code>{}</code></b>
<b>᚛› 𝙉𝘼𝙈𝙀 - {}</b>
"""
