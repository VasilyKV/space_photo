import datetime
import os
from urllib.parse import urlsplit
from urllib.parse import unquote

import requests
from dotenv import load_dotenv


def files_download(filename, url):
	directory = os.path.dirname(filename)
	if not os.path.exists(directory):
		os.makedirs(directory)
	response = requests.get(url)
	response.raise_for_status
	with open(filename, 'wb') as file:
		file.write(response.content)


def fetch_spacex_last_launch():
	url = 'https://api.spacexdata.com/v5/launches/6243adcaaf52800c6e919254'	# д.б. /latest но там нет фото
	response = requests.get(url)
	response.raise_for_status
	spacex_photos_url = response.json().get('links').get('flickr').get('original')
	for count, photo_url in enumerate(spacex_photos_url, start=1):
		filename = f'images/spacex{count}.jpeg' 
		files_download(filename, photo_url)


def file_ext_from_url(url):
	url_parsed = urlsplit (url)
	path_unquoted = unquote(url_parsed.path)
	file_extension = os.path.split(path_unquoted)[1]
	file_extension = os.path.splitext(file_extension)[1]
	return file_extension


def fetch_nasa_apod(api_key, photos_amaunt):
	payload = {
		'api_key': f'{api_key}',
		'count': f'{photos_amaunt}'
		}
	url = 'https://api.nasa.gov/planetary/apod'
	response = requests.get(url, params=payload)
	response.raise_for_status
	nasa_apods = response.json()
	for count, nasa_apod in enumerate(nasa_apods, start=1):
		photo_url = nasa_apod.get('url')
		filename = f'images/nasa_apod{count}{file_ext_from_url(photo_url)}'
		files_download(filename, photo_url)


def fetch_nasa_epic(api_key, photos_amaunt):
	payload = {
			'api_key': f'{api_key}'
			}	
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	response = requests.get(url, params=payload)
	response.raise_for_status
	nasa_epics = response.json()
	for count, nasa_epic in enumerate(nasa_epics, start=1):
			date = datetime.datetime.fromisoformat(nasa_epic.get('date')).strftime("%Y/%m/%d")
			image = nasa_epic.get('image')
			photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={api_key}'
			filename = f'images/nasa_epic{count}.png'
			files_download(filename, photo_url)
			if count >= photos_amaunt: break


def main():
	load_dotenv()
	api_key = os.getenv('NASA_API_KEY')
	photos_amaunt_nasa_apod = 2
	photos_amaunt_nasa_epic = 2
	fetch_spacex_last_launch()
	fetch_nasa_apod(api_key, photos_amaunt_nasa_apod)
	fetch_nasa_epic(api_key, photos_amaunt_nasa_epic)

if __name__ == '__main__':
    main()


