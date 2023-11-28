from proxy_validation import validate_proxy
from logging_handler import log_error
from tqdm import tqdm
import sys



def check_custom_proxies(custom_proxies_file, user_agents):
    if custom_proxies_file:
        with open(custom_proxies_file, 'r') as proxy_textfile:
            custom_proxies = [proxy_line.strip() for proxy_line in proxy_textfile.readlines()]
        response = input(f"A .txt file with {len(custom_proxies)} custom proxies was found. Do you want to check these proxies? (yes/no): ")
        if response.lower() == 'yes':
            # Ask the user for the number of proxies to check
            num_desired_proxies = get_user_input(custom_proxies, 'custom')
            # Check the custom proxies with a progress bar
            working_custom_proxies = []
            for proxy in tqdm(custom_proxies[:num_desired_proxies], desc="Checking custom proxies"):
                if validate_proxy(proxy, user_agents):
                    working_custom_proxies.append(proxy)
            with open('working_custom_proxies.txt', 'w') as working_file:
                working_file.write('\n'.join(working_custom_proxies))
            print(f"Working custom proxies: {len(working_custom_proxies)}")
        response = input("Do you want to check the built-in proxies? (yes/no): ")
        if response.lower() == 'yes':
            # Continue with built-in proxies
            return True
        else:
            sys.exit("Goodbye!")
    else:
        # Continue with built-in proxies
        return True

def get_user_input(proxies, proxy_type='built-in'):
    while True:
        try:
            num_desired_proxies = input(f"Enter the number of {proxy_type} proxies you want to check (out of {len(proxies)}), or type 'all' for all of them: ")
            if num_desired_proxies.lower() == 'all':
                num_desired_proxies = len(proxies)
                break
            num_desired_proxies = int(num_desired_proxies)
            if num_desired_proxies < 0:
                print("Number of proxies cannot be negative. Please try again.")
            elif num_desired_proxies > len(proxies):
                print(f"Number of proxies cannot be greater than the number of available proxies ({len(proxies)}). Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number or 'all'.")
    return num_desired_proxies