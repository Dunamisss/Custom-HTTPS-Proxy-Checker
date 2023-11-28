import logging

log_file = "output_files/proxy_checker.log"

def setup_logger():
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,  # Change this to the lowest level you want to log
        format="%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(lineno)d")

def log_section(name):
    logging.info(f"\n{'='*30}\n{name}\n{'='*30}")

def log_error(proxy, error):
    logging.error(f"Proxy validation failed for {proxy}: {error}")