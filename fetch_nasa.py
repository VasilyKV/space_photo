import datetime
import os
from urllib.parse import urlsplit
from urllib.parse import unquote

import requests


def files_download(filename, url):
	directory = os.path.dirname(filename)
	if not os.path.exists(directory):
		os.makedirs(directory)
	response = requests.get(url)
	response.raise_for_status
	with open(filename, 'wb') as file:
		file.write(response.content)


def file_ext_from_url(url):
	url_parsed = urlsplit (url)
	path_unquoted = unquote(url_parsed.path)
	file_extension = os.path.split(path_unquoted)[1]
	file_extension = os.path.splitext(file_extension)[1]
	return file_extension


def fetch_nasa_apod(api_key, photos_amaunt, folder):
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
		filename = f'{folder}nasa_apod{count}{file_ext_from_url(photo_url)}'
		files_download(filename, photo_url)


def fetch_nasa_epic(api_key, photos_amaunt, folder):
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
			filename = f'{folder}nasa_epic{count}.png'
			files_download(filename, photo_url)
			if count >= photos_amaunt: break

