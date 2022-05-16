import os
import telegram
import time

from dotenv import load_dotenv


def main():
	load_dotenv()
	TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
	CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
	execution_period = 600  # seconds
	photo_folder = 'images/'
	bot = telegram.Bot(TG_TOKEN)
	while True:
		photos_list = os.listdir(path=photo_folder)
		for photo_name in photos_list:
			with open(f'{photo_folder}{photo_name}', 'rb') as photo:
				bot.send_photo(chat_id=CHAT_ID, photo=photo)
		time.sleep(execution_period)


if __name__ == '__main__':
	main()
