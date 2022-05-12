import os
import telegram
import time

from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_apod
from fetch_nasa import fetch_nasa_epic


def main():
	load_dotenv()
	TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
	API_KEY = os.getenv('NASA_API_KEY')
	CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
	EXECUTION_PERIOD = 1*60*24 # seconds
	PHOTO_FOLDER = 'images/'
	PHOTOS_AMAUNT_NASA_APOD = 5
	PHOTOS_AMAUNT_NASA_EPIC = 2
	
	bot = telegram.Bot(TG_TOKEN)
	while True:
		fetch_nasa_apod(API_KEY, PHOTOS_AMAUNT_NASA_APOD, PHOTO_FOLDER)
		fetch_nasa_epic(API_KEY, PHOTOS_AMAUNT_NASA_EPIC, PHOTO_FOLDER)
		fetch_spacex_last_launch(PHOTO_FOLDER)
		photos_list = os.listdir(path=PHOTO_FOLDER)
		for photo_name in photos_list:
			with open(f'{PHOTO_FOLDER}{photo_name}', 'rb') as photo:
				bot.send_photo(chat_id=CHAT_ID, photo=photo)
			time.sleep(EXECUTION_PERIOD)
if __name__ == '__main__':
    main()
