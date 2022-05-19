import datetime
import os
import requests

from dotenv import load_dotenv

from url_to_file_utils import download_file, get_file_extension


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
		file_extension = get_file_extension(photo_url)
		if file_extension:
			file_path = f'{folder}nasa_apod{count}{file_extension}'
			download_file(file_path, photo_url)


def fetch_nasa_epic(api_key, photos_amount, folder):
	payload = {
		'api_key': f'{api_key}'
	}
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	url_archive = 'https://api.nasa.gov/EPIC/archive/natural/'
	response = requests.get(url, params=payload)
	response.raise_for_status()
	nasa_epics = response.json()
	for count, nasa_epic in enumerate(nasa_epics[:photos_amount], start=1):
			date = datetime.datetime.fromisoformat(nasa_epic.get('date')).strftime("%Y/%m/%d")
			image = nasa_epic.get('image')
			photo_url = f'{url_archive}{date}/png/{image}.png?api_key={api_key}'
			file_path = f'{folder}nasa_epic{count}.png'
			download_file(file_path, photo_url)


def main():
	load_dotenv()
	api_key = os.getenv('NASA_API_KEY')
	photo_folder = 'images/'
	photos_amount_nasa_apod = 10
	photos_amount_nasa_epic = 1
	fetch_nasa_apod(api_key, photos_amount_nasa_apod, photo_folder)
	fetch_nasa_epic(api_key, photos_amount_nasa_epic, photo_folder)


if __name__ == '__main__':
	main()
