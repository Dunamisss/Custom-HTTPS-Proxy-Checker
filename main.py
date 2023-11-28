from logging_handler import setup_logger, log_section
from proxy_validation import validate_proxy, validate_proxy_with_retry
from proxy_downloading import download_proxies
from user_interaction import check_custom_proxies, get_user_input
import concurrent.futures
from tqdm import tqdm
import re
import os

# Create output directory if it doesn't exist
output_dir = 'output_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set up logging with detailed format
setup_logger()

# Logging script initiation
log_section("Started: Proxy Checker.")

# Load URLs from 'proxy_urls.txt'
with open('proxy_urls.txt') as url_file:
    urls = [url.rstrip() for url in url_file]

# Read user agents from 'user_agents.txt'
with open('user_agents.txt') as ua_file:
    user_agents = [ua.rstrip() for ua in ua_file]

# Check if 'custom_proxies' folder exists and contains a .txt file
custom_proxies_folder = 'custom_proxies'
custom_proxies_file = next((file.path for file in os.scandir(custom_proxies_folder) if file.name.endswith('.txt')), None)

# Global list to store proxies
proxies = []

# If 'custom_proxies' folder contains a .txt file, prompt the user
check_custom_proxies(custom_proxies_file, user_agents)

# Update the logging for each URL in the script
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(tqdm(executor.map(lambda url: download_proxies(url, user_agents), urls), total=len(urls), desc="Downloading Proxies"))

# Flatten the results and filter valid IP:Port combinations
proxies = [proxy for url, sublist in results for proxy in sublist if re.match(r'\d+\.\d+\.\d+\.\d+:\d+', proxy)]

# save valid proxies
with open(os.path.join(output_dir, 'https.txt'), 'w') as https_file:
    https_file.write('\n'.join(proxies))

# Ask the user for the number of proxies to check
num_desired_proxies = get_user_input(proxies)

# Ask the user for the number of threads
while True:
    try:
        num_threads = int(input("Enter the number of threads you want to use: "))
        if num_threads < 1:
            print("Number of threads must be at least 1. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Use concurrent.futures to check proxies in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    working_proxies = list(tqdm(executor.map(lambda proxy: validate_proxy_with_retry(proxy, user_agents), proxies[:num_desired_proxies]), total=num_desired_proxies, desc="Checking Proxies"))

# Save working proxies to file
working_proxies_list = [proxy for proxy, is_working in zip(proxies, working_proxies) if is_working]
with open(os.path.join(output_dir, 'working_proxies.txt'), 'w') as working_file:
    working_file.write('\n'.join(working_proxies_list))

num_working_proxies = len(working_proxies_list)
log_section(f"Total working proxies: {num_working_proxies}")

num_failed_proxies = num_desired_proxies - num_working_proxies
log_section(f"{num_working_proxies} working proxies and {num_failed_proxies} failed proxies out of {num_desired_proxies}")

result_summary = f"Working Proxies: {num_working_proxies}\nFailed Proxies: {num_failed_proxies}"
with open(os.path.join(output_dir, 'proxy_results.txt'), 'w') as results_file:
    results_file.write(result_summary)

print(f"\nWorking Proxies: {num_working_proxies}")
print(f"Failed Proxies: {num_failed_proxies}")

log_section("Script Execution Summary")
log_section(result_summary)
log_section("Proxy Checker Script Execution Completed.")
