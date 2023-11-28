# Proxy Checker

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

 
[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2023 Dunamisss

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

This Proxy Checker is provided for educational use only. The author Dunamis is not responsible for how it is used or any consequences resulting from its use.

