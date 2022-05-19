import os
import requests

from dotenv import load_dotenv

from url_to_file_utils import download_file, get_file_extension


def fetch_spacex_last_launch(folder):
	url = 'https://api.spacexdata.com/v5/launches/latest'
	response = requests.get(url)
	response.raise_for_status()
	spacex_photos_url = response.json().get('links').get('flickr').get('original')
	for count, photo_url in enumerate(spacex_photos_url, start=1):
		file_path = f'{folder}spacex{count}{get_file_extension(photo_url)}'
		download_file(file_path, photo_url)


def main():
	load_dotenv()
	photo_folder = 'images/'
	fetch_spacex_last_launch(photo_folder)


if __name__ == '__main__':
	main()
