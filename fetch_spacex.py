import os
import requests

from dotenv import load_dotenv

from url_to_file_utils import file_download
from url_to_file_utils import file_ext_from_url


def fetch_spacex_last_launch(folder):
	url = 'https://api.spacexdata.com/v5/launches/latest'
	response = requests.get(url)
	response.raise_for_status()
	spacex_photos_url = response.json().get('links').get('flickr').get('original')
	for count, photo_url in enumerate(spacex_photos_url, start=1):
		file_path = f'{folder}spacex{count}{file_ext_from_url(photo_url)}'
		file_download(file_path, photo_url)


def main():
	load_dotenv()
	TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
	API_KEY = os.getenv('NASA_API_KEY')
	CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
	photo_folder = 'images/'
	fetch_spacex_last_launch(photo_folder)


if __name__ == '__main__':
	main()
