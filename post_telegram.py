import os
import telegram
import time

from dotenv import load_dotenv


def main():
	load_dotenv()
	tg_token = os.getenv('TELEGRAM_TOKEN')
	chat_id = os.getenv('TELEGRAM_CHAT_ID')
	execution_period = int(os.getenv('EXECUTION_PERIOD'))
	photo_folder = 'images/'
	bot = telegram.Bot(tg_token)
	while True:
		photos_list = os.listdir(path=photo_folder)
		for photo_name in photos_list:
			with open(f'{photo_folder}{photo_name}', 'rb') as photo:
				bot.send_photo(chat_id=chat_id, photo=photo)
		time.sleep(execution_period)


if __name__ == '__main__':
	main()
