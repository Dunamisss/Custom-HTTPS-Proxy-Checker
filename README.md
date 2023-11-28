# Custom Https Proxy Checker

This script is a simple and efficient tool for downloading and validating proxies. It's designed to be easy to use and highly customizable.

## Features

- **Proxy Downloading**: The script automatically downloads proxies from URLs listed in a text file.
- **Multithreaded Proxy Validation**: Proxies are validated in parallel using multithreading, significantly speeding up the process compared to sequential checks.
- **User Customization**: You can specify the number of proxies to check and the number of threads to use.
- **Custom Proxy Checking**: If a .txt file is found in the 'custom_proxies' folder, the script will prompt you to check these proxies.
- **Output Files**: The script saves valid proxies and working proxies to separate files in the 'output_files' directory.
- **Detailed Logging**: Detailed information about the script's execution is logged to a file, making it easy to troubleshoot any issues.
- **Proxy Rotation** & **UserAgent Rotation** Thanks to who ever created the UserAgent.txt 

## Usage

1. (Optional) Add your proxy URLs to 'proxy_urls.txt' or simple just use the built in ones.
2. (Optional) Add your custom proxies to a .txt file in the 'custom_proxies' folder.
3. Run the script: `python main.py`
4. Follow the prompts to specify the number of proxies to check and the number of threads to use.

## Requirements

- Python 3.6 or higher
- Required Python packages: `requests`, `tqdm`

## Results
Working proxies are saved to `working_proxies.txt`.
Valid proxies are saved to `https.txt`.
Execution summary and results are logged in `proxy_results.txt`.

## Script Execution Summary
For a detailed summary of the script's execution, refer to the log file `proxy_checker.log`.

## Licence
This project is licensed under the [MIT License](LICENSE).

---

This Proxy Checker is provided for educational use only. The author Dunamis is not responsible for how it is used or any consequences resulting from its use.

