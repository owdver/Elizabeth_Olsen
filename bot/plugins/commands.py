#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT & @OwDvEr
import os
import logging


from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot import UPDATE_CHANNEL # Update Text Message Channel Update
from bot import MRK_YT_MASTER
from bot import MT_GROUP
from bot import MT_CHANNEL # Main Channel Added
from bot.motech import MT_BOT_UPDATES
logger = logging.getLogger(__name__)

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start owdver"):
        if UPDATE_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(UPDATE_CHANNEL))
            try:
                user = await bot.get_chat_member(int(UPDATE_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text ="Sorry Sir, Your Banned to use me",
                        parse_mode="markdown",
                        desable_webpage_preview=True
                    )
                    return
                exept UserNotParticipant:
                    ident, file_id = cmd.text.split("_-_-_-_")
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="**Please Join My Updates Channel to use this Bot!**",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardMarkup("🤖 Join Updates Channel", url=invite_link.invite_link)
                                ]
                                [
                                    InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                                ]
                            ]
                        ),
                        parse_mode="markdown"
                    )
                    return
                except Exceptetion:
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Something went Wrong",
                        parse_mode="markdown",
                        disable_webpage_preview=True
                    )
                    return
                
                        

                    
               await update.reply_text("𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎, 𝚈𝚘𝚞 𝚊𝚛𝚎 𝙱𝚊𝚗𝚗𝚎𝚍")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>നിങ്ങൾക്ക് മൂവീസ് വേണോ? എങ്കിൽ തായെ കാണുന്ന ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക\nഎന്നിട്ട് ഗ്രൂപ്പിൽ പോയി വീണ്ടും മൂവിയിൽ ക്ലിക് ചെയ്ത് start കൊടുത്തു നോക്കൂ..!😁</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⭕️ 𝙹𝚘𝚒𝚗 𝙾𝚞𝚛 𝙼𝚊𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⭕️", url=f"https://t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>ഈ ചാനലിൽ  @{UPDATE_CHANNEL} ബോട്ടിനെ അഡ്മിൻ ആക്. എന്നിട്ട് /start കൊടുക്</b>")
            return  
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕️ 𝙹𝚘𝚒𝚗 𝙾𝚞𝚛 𝙼𝚊𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⭕️', url=f"{MT_CHANNEL}"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨🏻‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url="https://t.me/Owdver_Bot"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨🏻‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url="https://t.me/Owdver_Bot"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('➕ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕', url=f'http://t.me/OB_FILTERBOT?startgroup=botstart')
        ],[
        InlineKeyboardButton('👨🏻‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢', url=f't.me/OB_LINKS')
    ],[
        InlineKeyboardButton('🔧 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('𝙷𝙴𝙻𝙿 ⚙️', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏠 Home', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('❌', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('🏠 Home', callback_data='start'),
        InlineKeyboardButton('❌', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
