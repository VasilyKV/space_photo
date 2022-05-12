import os

import requests


def files_download(filename, url):
	directory = os.path.dirname(filename)
	if not os.path.exists(directory):
		os.makedirs(directory)
	response = requests.get(url)
	response.raise_for_status
	with open(filename, 'wb') as file:
		file.write(response.content)


def fetch_spacex_last_launch(folder):
	url = 'https://api.spacexdata.com/v5/launches/6243adcaaf52800c6e919254'	# д.б. /latest но там нет фото
	response = requests.get(url)
	response.raise_for_status
	spacex_photos_url = response.json().get('links').get('flickr').get('original')
	for count, photo_url in enumerate(spacex_photos_url, start=1):
		filename = f'{folder}spacex{count}.jpeg' 
		files_download(filename, photo_url)





