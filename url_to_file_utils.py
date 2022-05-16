import os
from urllib.parse import urlsplit
from urllib.parse import unquote

import requests


def file_download(filename, url):
	directory = os.path.dirname(filename)
	if not os.path.exists(directory):
		os.makedirs(directory)
	response = requests.get(url)
	response.raise_for_status()
	with open(filename, 'wb') as file:
		file.write(response.content)


def file_ext_from_url(url):
	url_parsed = urlsplit (url)
	path_unquoted = unquote(url_parsed.path)
	file_extension = os.path.split(path_unquoted)[1]
	file_extension = os.path.splitext(file_extension)[1]
	return file_extension
	