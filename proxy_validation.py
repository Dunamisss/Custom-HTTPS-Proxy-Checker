import requests
import random
from logging_handler import log_error
import logging
import time

def validate_proxy(proxy, user_agents, timeout=5):
    headers = {'User-Agent': random.choice(user_agents)}
    logging.info(f"Chosen User Agent: {headers['User-Agent']}")
    logging.info(f"Validating proxy: {proxy}")

    try:
        response = requests.get("https://www.google.com", proxies={"https": f"http://{proxy}"}, headers=headers, timeout=timeout)
        if response.status_code == 200:
            logging.debug(f"Proxy validation successful for {proxy}")
            return True
        else:
            log_error(proxy, f"Received status code {response.status_code}")
    except requests.exceptions.ConnectTimeout:
        log_error(proxy, "Connection timeout")
    except requests.exceptions.ProxyError:
        log_error(proxy, "Error with the proxy server")
    except Exception as e:
        log_error(proxy, str(e))

    return False

def validate_proxy_with_retry(proxy, user_agents, max_retries=3, timeout=5, delay=5):
    retries = 0
    while retries < max_retries:
        try:
            if validate_proxy(proxy, user_agents, timeout):
                return True
            else:
                retries += 1
                time.sleep(delay)  # Add a delay before retrying
        except Exception as e:
            log_error(proxy, str(e))
            retries += 1
            time.sleep(delay)  # Add a delay before retrying

    log_error(proxy, f"Max retries reached. Proxy is considered dead.")
    return False