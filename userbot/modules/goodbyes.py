from userbot.events import register
from userbot import CMD_HELP, bot, LOGS, CLEAN_GOODBYE, BOTLOG_CHATID
from telethon.events import ChatAction


@bot.on(ChatAction)
async def goodbye_to_chat(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import get_current_goodbye_settings
        from userbot.modules.sql_helper.goodbye_sql import update_previous_goodbye
    except AttributeError:
        return
    cgs = get_current_goodbye_settings(event.chat_id)
    if cgs:
        """user_added=False,
        user_joined=False,
        user_left=True,
        user_kicked=True"""
        if (event.user_left
                or event.user_kicked) and not (await event.get_user()).bot:
            if CLEAN_GOODBYE:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cgs.previous_goodbye)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_goodbye_message = None
            if cgs and cgs.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cgs.f_mesg_id))
                file_media = msg_o.media
                current_saved_goodbye_message = msg_o.message
            elif cgs and cgs.reply:
                current_saved_goodbye_message = cgs.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_goodbye(event.chat_id, current_message.id)


@register(outgoing=True, pattern=r"^.setgoodbye(?: |$)(.*)")
async def save_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import add_goodbye_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#GOODBYE_NOTE\
            \nCHAT ID: {event.chat_id}\
            \nThe following message is saved as the new goodbye note for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                "`Saving media as part of the goodbye note requires the BOTLOG_CHATID to be set.`"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Goodbye note {} for this chat.`"
    if add_goodbye_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('saved'))
    else:
        await event.edit(success.format('updated'))


@register(outgoing=True, pattern="^.checkgoodbye$")
async def show_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import get_current_goodbye_settings
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    cgs = get_current_goodbye_settings(event.chat_id)
    if not cgs:
        await event.edit("`No goodbye message saved here.`")
        return
    elif cgs and cgs.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cgs.f_mesg_id))
        await event.edit(
            "`I am currently farewell new users with this goodbye note.`")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cgs and cgs.reply:
        await event.edit(
            "`I am currently farewell new users with this goodbye note.`")
        await event.reply(cgs.reply)


@register(outgoing=True, pattern="^.rmgoodbye$")
async def del_goodbye(event):
    try:
        from userbot.modules.sql_helper.goodbye_sql import rm_goodbye_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    if rm_goodbye_setting(event.chat_id) is True:
        await event.edit("`Goodbye note deleted for this chat.`")
    else:
        await event.edit("`Do I have a goodbye note here ?`")


CMD_HELP.update({
    "goodbye":
    "\
.setgoodbye <farewell message> or reply to a message with .setgoodbye\
\nUsage: Saves the message as a goodbye note in the chat.\
\n\nAvailable variables for formatting goodbye messages :\
\n`{my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n.checkgoodbye\
\nUsage: Check whether you have a goodbye note in the chat.\
\n\n.rmgoodbye\
\nUsage: Deletes the goodbye note for the current chat.\
"
})
