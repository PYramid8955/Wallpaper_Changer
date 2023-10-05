import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep

HEADERS = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0",
	"Accept": "*/*"
}

def get_nofollow_links(url):
	try:
		response = requests.get(url, headers=HEADERS)
		response.raise_for_status()  # Raise an HTTPError for bad requests
		soup = BeautifulSoup(response.text, 'html.parser')
		nofollow_links = soup.find_all('a', rel='nofollow')
		return [link.get('href') for link in nofollow_links]
	except requests.exceptions.HTTPError as errh:
		print(f"HTTP Error: {errh}")
	except requests.exceptions.ConnectionError as errc:
		print(f"Error Connecting: {errc}")
	except requests.exceptions.Timeout as errt:
		print(f"Timeout Error: {errt}")
	except requests.exceptions.RequestException as err:
		print(f"Request Exception: {err}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	return []

def getLinks(search_query, verify = 0):
	try:
		url = f'https://unsplash.com/s/photos/{search_query}?orientation=landscape&license=free'
		nofollow_links = get_nofollow_links(url)
		if nofollow_links:
			if not verify:
				response = choice(nofollow_links)
			else:
				response = len(nofollow_links)
			return response
		else:
			return None
	except KeyboardInterrupt:
		print("\nOperation interrupted by the user.")
	except Exception as e:
		print(f"An error occurred: {e}")

