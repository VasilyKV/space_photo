import os
import shutil
import telegram
import time

from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic


def main():
	load_dotenv()
	tg_token = os.getenv('TELEGRAM_TOKEN')
	api_key = os.getenv('NASA_API_KEY')
	chat_id = os.getenv('TELEGRAM_CHAT_ID')
	execution_period = int(os.getenv('EXECUTION_PERIOD'))
	photo_folder = 'images/'
	photos_amount_nasa_apod = 5
	photos_amount_nasa_epic = 2
	bot = telegram.Bot(tg_token)
	while True:
		fetch_nasa_apod(api_key, photos_amount_nasa_apod, photo_folder)
		fetch_nasa_epic(api_key, photos_amount_nasa_epic, photo_folder)
		fetch_spacex_last_launch(photo_folder)
		photos_list = os.listdir(path=photo_folder)
		for photo_name in photos_list:
			photo_path = f'{photo_folder}{photo_name}'
			with open(photo_path, 'rb') as photo:
				bot.send_photo(chat_id=chat_id, photo=photo)
			time.sleep(execution_period)
		shutil.rmtree(photo_folder, ignore_errors=True)


if __name__ == '__main__':
	main()

