# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module which contains afk-related commands """

from datetime import datetime
import time
from random import choice, randint

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    "Gue sibuk, nanti aja yaa, chatnya disimpen dulu, klo gue on baru bilang apa yang kamu mau katakan",
    "Gue lagi pergi. Jika lu mau apa-apa, tinggalkan pesan setelah bunyi:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!",
    "OOOOWWWW lu terlambat, gue udh off, mungkin nanti klo mau sesuatu tuh bilangnya pas gue on.",
    "Gue bakal kembali beberapa menit dan klo engga...,\ntunggu aja dulu.",
    "Gue lagi g disini, mungkin lagi ditempat lain...\nMungkin.",
    "Ada hiu makan kangkung,\nberarti dia vegetarian,\nChat aja dulu gue,\nNanti baru gue bales.",
    "LU SAHAA NJIER!!!",
    "Gue bakal on,\ntapi klo gue g on,\nberarti gue on nya nanti.",
    "Sabarrr, tunggu gue on duluuu.",
    "Kaga kelar-kelar bumsettt.",
    "Gue dalam perjalanan melewati 7 Samudra and 7 Negara,\n7 Perairan and 7 Benua,\n7 Gunung and 7 Lembah,\n7 Dataran and 7 Gundukan,\n7 Kolam and 7 Danau,\n7 Mata Air and 7 Padang Rumput,\n7 Kota and 7 Lingkungan,\n7 Blok and 7 Rumah...\n\nDimana tak ada satupun chat lu yg sampe ke gue!",
    "Gue lagi g main hp sebentar, tapi klo lu teriak sekencang-kencangnya ke layar hp lu, mungkin gue bakal mendengar lu.",
    "Gue pergi ke arah sana\n---->",
    "Gue pergi ke arah sana\n<----",
    "Please tinggalkan pesan dan buat gue merasa klo pesannya itu penting.",
    "Gue lagi g disini jadi berhenti ngechat gue,\natau klo engga lu bakal meliat layar hp lu penuh dengan chat yg lu kirim.",
    "Jika gue disini,\ngue bakal beritahu lu.\n\nTapi gue lagi pergi,\njadi, tunggu ajah...",
    "Gue lagi pergi!\nNtahlah, gue g tau kapan pulang!\nBerharapnya sih beberapa menit dari sekarang!",
    "Gue lagi g ada, jadi please tinggalkan pesan, nama lu, nomor hp, dan alamat lu,\ndan gue akan ngestalking (memata-matai) lu nanti.",
    "Sorry, gue lagi g make telegram.\nJadi tolonglah jangan SPAM SPAM euy.\ngue nanti bakal on kok.",
    "Tumben nih nyari gue, ada apa niich",
    "Hidup itu singkat, Banyak hal yang bisa dilakukan...\nNah jadi gue lagi lakuin salah satunya..",
    "Lagi nyari kantong ajaib doraemon, terus bantuin kera sakti nyari kitab suci, lalu bantuin naruto ngalahin madara supaya dia bisa jadi hokage",
]

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"Gue OFF!\
        \nKarena: `{string}`")
    else:
        await afk_e.edit("Gue OFF!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    ISAFK = True
    afk_time = datetime.now()  # pylint:disable=E0602
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("Gue sudah Online.")
        time.sleep(3)
        await msg.delete()
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "beberapa saat yang lalu"
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Kemaren"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` yang lalu"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` yang lalu"
            else:
                afk_since = f"`{int(seconds)}s` yang lalu"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(str(choice(AFKSTR), {afk_since}, {AFKREASON}))
                    await mention.reply(f"Gue OFF sejak {afk_since}.\
                        \nKarena: `{AFKREASON}`")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(str(choice(AFKSTR)))
                        await mention.reply(f"Gue masih OFF sejak {afk_since}.\
                            \nKarena: `{AFKREASON}`")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "Beberapa saat yang lalu"
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Kemaren"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` yang lalu"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` yang lalu"
            else:
                afk_since = f"`{int(seconds)}s` yang lalu"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(str(choice(AFKSTR)))
                    await sender.reply(f"Gue OFF sejak {afk_since}.\
                        \nKarena: `{AFKREASON}`")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(str(choice(AFKSTR)))
                        await sender.reply(f"Gue masih OFF sejak {afk_since}.\
                            \nKarena: `{AFKREASON}`")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
"
})
