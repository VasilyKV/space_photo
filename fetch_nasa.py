import datetime
import os
import requests

from dotenv import load_dotenv

from url_to_file_utils import file_download
from url_to_file_utils import file_ext_from_url


def fetch_nasa_apod(api_key, photos_amount, folder):
	payload = {
		'api_key': f'{api_key}',
		'count': photos_amount
	}
	url = 'https://api.nasa.gov/planetary/apod'
	response = requests.get(url, params=payload)
	response.raise_for_status()
	nasa_apods = response.json()
	for count, nasa_apod in enumerate(nasa_apods, start=1):
		photo_url = nasa_apod.get('url')
		file_path = f'{folder}nasa_apod{count}{file_ext_from_url(photo_url)}'
		file_download(file_path, photo_url)


def fetch_nasa_epic(api_key, photos_amount, folder):
	payload = {
		'api_key': f'{api_key}'
	}
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	response = requests.get(url, params=payload)
	response.raise_for_status()
	nasa_epics = response.json()
	for count, nasa_epic in enumerate(nasa_epics, start=1):
			date = datetime.datetime.fromisoformat(nasa_epic.get('date')).strftime("%Y/%m/%d")
			image = nasa_epic.get('image')
			photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={api_key}'
			file_path = f'{folder}nasa_epic{count}.png'
			file_download(file_path, photo_url)
			if count >= photos_amount: break


def main():
	load_dotenv()
	TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
	API_KEY = os.getenv('NASA_API_KEY')
	CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
	photo_folder = 'images/'
	photos_amount_nasa_apod = 10
	photos_amount_nasa_epic = 1
	fetch_nasa_apod(API_KEY, photos_amount_nasa_apod, photo_folder)
	fetch_nasa_epic(API_KEY, photos_amount_nasa_epic, photo_folder)


if __name__ == '__main__':
	main()
