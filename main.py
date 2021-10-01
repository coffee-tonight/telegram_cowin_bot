# from typing_extensions import final
import Constants as keys
from telegram.ext import *
import responses as R
import requests, json
import datetime
import re

# from decouple import config
# API = config('API_KEY')

print('Bot is starting')

def start_command(update, context):
	update.message.reply_text('Hello there, how may I help you')

def vaccine_command(update, context):
	update.message.reply_text("Please send your pin")

def about_me(update, context):
	# print(update)
	print("Update ID: ", update['update_id'])
	print("Message ID: ", update['message']['message_id'])
	print("chat username: ", update['message']['chat']['username'])
	# print(update['message']['from']['username'])
	ch = update['message']['chat']['username']

	if ch == "sbishant":
		update.message.reply_text("good Yr!")
	elif ch == "Crey0Le0":
		update.message.reply_text("Tu chutiya hi rahega chodd!!")
	elif ch == None:
		update.message.reply_text("Ohh bhaii kya baat hai mozz kr di oye!")

def handle_message(update, context):
	text = str(update.message.text).lower()
	user = update.effective_user
	print(f'{user["username"]}: {text}')

	response = ''
	regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
	p = re.compile(regex)

	m = re.match(p, text)
	if m is None:
		pin_val = False
	else:
		pin_val = True

	slot_book_cmd = ["vaccine", "vaccinated", "book slot", "slot", "slot booking", "details"]
	if any(x in text for x in slot_book_cmd):
		# update.message.reply_text("Please enter your PIN")
		response = "Please enter your PIN"
	elif pin_val:
		pin = text
		update.message.reply_text("Showing results for 7 days from today!")
		response = R.slot_data(pin)
	else:
		response = R.sample_responses(update, text)

	print(f'Bot: {response}')
	update.message.reply_text(response)

def handle_location(update, context):
	pass

def error(update, context):
	print(f"Update {update} caused error {context.error}")

def main():
	# updater = Updater(API, use_context=True)
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	#dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("vaccine", vaccine_command))
	dp.add_handler(CommandHandler("about_me", about_me))
	mh = dp.add_handler(MessageHandler(Filters.text, handle_message))
	
	dp.add_error_handler(error)


	updater.start_polling()
	updater.idle()

main()