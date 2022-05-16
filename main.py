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
	execution_period = 600  # seconds
	photo_folder = 'images/'
	photos_amount_nasa_apod = 5
	photos_amount_nasa_epic = 2
	bot = telegram.Bot(TG_TOKEN)
	while True:
		fetch_nasa_apod(API_KEY, photos_amount_nasa_apod, photo_folder)
		fetch_nasa_epic(API_KEY, photos_amount_nasa_epic, photo_folder)
		fetch_spacex_last_launch(photo_folder)
		photos_list = os.listdir(path=photo_folder)
		for photo_name in photos_list:
			with open(f'{photo_folder}{photo_name}', 'rb') as photo:
				bot.send_photo(chat_id=CHAT_ID, photo=photo)
		time.sleep(execution_period)


if __name__ == '__main__':
	main()

