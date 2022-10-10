# from typing_extensions import final
import Constants as keys
from telegram.ext import *
import responses as R
import requests, json
import datetime
import re
import random as r

# pip install geopy
from geopy.geocoders import Nominatim

# from decouple import config
# API = config('API_KEY')

print('Bot Is Starting!!!') #initialise the bot

def start_command(update, context):
	update.message.reply_text('Hello There, How May I Help You?')

def vaccine_command(update, context):
	update.message.reply_text("Please Send Your Pin") #add pin prompt
	

def other_chat(update, context):
	text = str(update.message.text).lower()
	user = update.effective_user
	words = [""]
	words.append(text.split())
	if text == "":
		return ""
	else:
		update.message.reply_text("We got your message regarding, " words[r.randInt(0, len(words)-1)])
		

def Important_chat(update, context):
	text = str(update.message.text).lower()
	user = update.effective_user
	words = ["Vaccine, Medic, Injection, Remedevisir"]
	words.append(text.split())
	if text == "Are you Fully Vaccinated or Partially Vaccinated?":
		update.message.reply_text("We got your details regarding vaccination " words[r.randInt(0, len(words)-1)])
		return ""
	else:
		update.message.reply_text("We got your message regarding, " words[r.randInt(0, len(words)-1)])
	

def about_me(update, context):
	# print(update)
	print("Update ID: ", update['update_id'])
	print("Message ID: ", update['message']['message_id'])
	print("chat username: ", update['message']['chat']['username'])
	# print(update['message']['from']['username'])
	ch = update['message']['chat']['username']

	if ch == "Bishant":
		update.message.reply_text("Good Yr!")
	elif ch == "Crey0Le0":
		update.message.reply_text("Tu nhi samjhega bhai chodd!!")
	elif ch == "Ankit":
		update.message.reply_text("Han bhai kya haal hai?")
	elif ch == "Great":
		update.message.reply_text("Oh veere!!! Tusi Great ho")
	elif ch == "NCC Hero":
		update.message.reply_text("Hello again, Sir Bishant")
	elif ch == "Flutter Champ":
		update.message.reply_text("Bishant bhai roxx")
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
		response = "Please Enter Your PIN (Postal Index Number)"
	elif pin_val:
		pin = text
		update.message.reply_text("Showing Results for 7 days from Today!")
		response = R.slot_data(pin)
	else:
		response = R.sample_responses(update, text)

	print(f'Bot: {response}')
	update.message.reply_text(response)

def handle_location(update, context):
	loc = Nominatim(user_agent="GetLoc")
	getLoc = loc.geocode("Gosainganj Lucknow")
	print(getLoc.address)
	print("Latitude = ", getLoc.latitude, "\n")
	print("Longitude = ", getLoc.longitude)
	return (getLoc.latitude, getLoc.longitude)

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
