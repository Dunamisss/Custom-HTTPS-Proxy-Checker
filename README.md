# Proxy Checker

## Overview

The **Proxy Checker** is a Python script designed for efficiently checking the working status of proxies. It is equipped with features to validate both built-in and custom proxies, providing users with a streamlined process to identify functional proxies for their needs.

## Key Features

- **Built-in and Custom Proxies:** The script allows users to check the status of both built-in proxies and custom proxies loaded from a .txt file.
  
- **Parallel Processing:** Proxies are checked in parallel using concurrent.futures, ensuring faster execution and efficient validation.

- **User Agent Rotation:** The script employs random user agents to mimic diverse client environments during proxy validation.

- **Logging:** Detailed logging is implemented, providing insights into the selected user agents, checked proxies, and execution summary.

## How to Use

### Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)

### Setup

1. Clone the repository to your local machine.
2. Install the required packages by running:
  ```bash
   pip install -r requirements.txt
   ```

# Execution
Run the script using the following command:

Prepare a list of proxy URLs in a text file named proxy_urls.txt.
Specify user agents in a text file named user_agents.txt.
Optionally, create a folder named custom_proxies and place a .txt file with custom proxies for additional validation.

Run the script using the following command:

```bash
python proxy_checker.py
```
Follow on-screen prompts to check built-in proxies or custom proxies if available.

Results
Working proxies are saved to working_proxies.txt.
Valid proxies are saved to https.txt.
Execution summary and results are logged in proxy_results.txt.
Script Execution Summary
For a detailed summary of the script's execution, refer to the log file proxy_checker.log.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
