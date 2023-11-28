import requests
import random
import logging  
from logging_handler import log_error

def download_proxies(url, user_agents):
    if not url or not url.startswith(('http://', 'https://')):
        logging.error(f"Invalid URL: {url}")
        return url, []
    headers = {'User-Agent': random.choice(user_agents)}  # Select a random user agent
    logging.info(f"Selected User Agent: {headers['User-Agent']}")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if url.endswith('.json'):
                data = response.json()
                proxies = [f"{item['ip']}:{item['port']}" for item in data]
            else:
                proxies = response.text.splitlines()
            logging.info(f"Downloaded {len(proxies)} proxies from {url}")
            return url, proxies
        else:
            logging.error(f"Failed to download proxies from {url}. HTTP status code: {response.status_code}")
            return url, []
    except requests.exceptions.Timeout:
        logging.error(f"Timeout occurred while trying to download proxies from {url}")
        return url, []
    except requests.exceptions.TooManyRedirects:
        logging.error(f"Too many redirects while trying to download proxies from {url}")
        return url, []
    except Exception as e:
        logging.error(f"Failed to download proxies from {url}: {str(e)}")
        return url, []