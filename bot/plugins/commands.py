#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT & @OwDvEr

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

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("๐๐๐๐๐ข ๐ณ๐๐๐, ๐๐๐ ๐๐๐ ๐ฑ๐๐๐๐๐")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>Hi {message.from_user.mention},</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="๐ค Jแดษชษด Uแดแดแดแดแดs Cสแดษดษดแดส", url=f"https://t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>Mแดแดแด Sแดสแด Bแดแด Is Aแดแดษชษด Iษด FแดสแดแดSแดส Cสแดษดษดแดส</b>")
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
                                    "๐ค Jแดษชษด Uแดแดแดแดแดs Cสแดษดษดแดส", url=f"{MT_CHANNEL}"
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
                                    '๐จ๐ปโ๐ป ๐ฒ๐๐ด๐ฐ๐๐พ๐', url="https://t.me/Owdver_Bot"
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
                                    '๐จ๐ปโ๐ป ๐ฒ๐๐ด๐ฐ๐๐พ๐', url="https://t.me/Owdver_Bot"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)

        return

    buttons = [[
        InlineKeyboardButton('โ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ โ', url=f'http://t.me/OB_FILTERBOT?startgroup=botstart')
        ],[
        InlineKeyboardButton('๐จ๐ปโ๐ป ๐ฒ๐๐ด๐ฐ๐๐พ๐', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐ข', url=f't.me/OB_LINKS')
    ],[
        InlineKeyboardButton('๐ง ๐๐๐ฟ๐ฟ๐พ๐๐', url=f't.me/OWDVER_BOT'),
        InlineKeyboardButton('๐ท๐ด๐ป๐ฟ โ๏ธ', callback_data="help")
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
        InlineKeyboardButton('๐? Home', callback_data='start'),
        InlineKeyboardButton('About ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('โ', callback_data='close')
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
        InlineKeyboardButton('๐? Home', callback_data='start'),
        InlineKeyboardButton('โ', callback_data='close')
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
