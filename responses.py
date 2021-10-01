from time import sleep
import requests, json
import datetime
# from main import main

def sample_responses(update, input_text):
	user_message = str(input_text).lower()
	print(user_message)

	slot_book_cmd = ["vaccine", "vaccinated", "book slot", "slot", "slot booking"]

	if "help" in input_text.lower():
		# print("Bot: Yes Pl, tell how may I help you?")
		return "Yes Pl, tell me how may I help you? \n\nTry asking for vaccination or Slot booking details. \n\nOr use command /vaccine"

	elif "how are you" in input_text.lower():
		# print("Bot: I am fine")
		return "I am fine, how about you?"
	
	else:
		return "Sorry nothing detected!"


def slot_data(pin):
	pin = pin
	date = datetime.date.today().strftime("%d-%m-%Y")

	# print(date, pin)
	# url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
	url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date}'
	browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76Safari/537.36'}
	# print("url: ", url)
	response = requests.get(url, headers=browser_header)
	print(response)
	json_data = response.json()
	final_text = ''
	if len(json_data['centers'])==0:
		# print("\nSlots Not Available\n")
		return "Slots are not available currently!"
	else:
		# print(json_data)

		for centers in json_data['centers']:
			final_text = final_text + centers["name"] + "\n--------------------\n"
			# for slots in json_data['centers'][0]['sessions']:
			for slots in centers['sessions']:

				final_text = final_text +'\n\t'+ "Date: " + str(slots['date']) + "Available Capacity: " + "\n\t" + str(slots['available_capacity']) + '\n\t' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n\t' + "Vaccine: "+str(slots['vaccine'])+ '\n\t'
				final_text = final_text + '----------------------------------------------------------\n'

		return final_text[:4000] + "...."






	# new_data = user_message.split(':')
	# pin = new_data[0]
	# date = new_data[1]
	# try:
	# 	pin = int(pin)
	# except Exception as e:
	# 	pass
	# if(int(pin)<10000 and int(pin)>0):

	# 	url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
	# 	browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
	# 	print(url)
	# 	response = requests.get(url, headers=browser_header)
	# 	print(response)
	# 	json_data = response.json()
	# 	final_text = ''
	# 	if len(json_data['sessions'])==0:
	# 		print("\nSlots Not Available\n")
	# 	else:
	# 		for slots in json_data['sessions']:
	# 			final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
	# 			final_text = final_text + '----------------------------------------'

		# return final_text
	# else:
	# 	return "Invalid input"