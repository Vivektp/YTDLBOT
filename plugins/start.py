from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕️Channel⭕️", url="https://t.me/VKPROJECTS")],
        [InlineKeyboardButton(
            "⭕️ Report Bugs 😊 ⭕️", url="https://t.me/VKPBOTS")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n**I'm A POWERFULL YOUTUBE DOWNLOADER Bot💯**\n\n**Please send me any YOUTUBE link,**\n\n**Click /help for more detailS..**\n\n**You must subscribe our channel in order to use me😇**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
