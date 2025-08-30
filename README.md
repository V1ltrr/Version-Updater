<h1 align="center">  Version Updater </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-0.1-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/v1ltrr/Version-Updater?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/v1ltrr/Version-Updater?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/v1ltrr/Version-Updater?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/v1ltrr/Version-Updater?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-V1ltrr-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
</p>

---

## Description

**Url Breaker** is a lightweight Python tool designed to perform URL fuzzing.  
It automatically generates various "broken" or modified variants of a target URL and tests each one to identify unexpected behaviors or potential server-side vulnerabilities.

This tool is particularly useful for web security testing, allowing you to verify if certain paths or URL variants not intended by the application are accessible or produce different responses.

## Key Features
- Automatic generation of URL variants including encodings, special sequences, path manipulations, and more.  
- Support for a custom wordlist (`wordlist.txt`) to test your own additional variants.  
- Sends HTTP requests to each variant and displays the HTTP status code.  
- Colorized terminal output for easier result interpretation.  
- Robust error handling to prevent process interruptions due to network issues.  
- Interactive console interface with mode selection and display preferences.  
- Multithreaded scanning for faster execution.  
- Stylish dynamic progress bar in reduced mode for a smooth UX.

## Requirements
- Python 3.6 or higher  
- Python packages:
  - `requests`  
  - `colorama`

## Installation
Clone the repository or download the source files :
```bash
git clone https://github.com/V1ltrr/Version-Updater.git
cd Version-Updater
pip install requests colorama
```
## Usage
Run the script by launching :
```bash
python url_breaker.py
```
### Steps
1. Select the fuzzing mode:  
   - Default built-in list  
   - Custom wordlist from `wordlist.txt`  
   - Exit the program
     
2. Select the display mode :  
   - Extended mode: view all tested URLs and their HTTP codes  
   - Reduced mode: view only a summary (200 & 403) with a progress bar
     
2. Enter the target URL:  
   - Must include the protocol (`http://` or `https://`)  
   - No spaces allowed  
   - Example: `https://example.com/admin`

## Project Structure
```text
Version-Updater/
├── LICENCE              # This documentation file
├── README.md            # This documentation file
├── url_breaker.py       # Main script
├── wordlist.txt         # Optional custom variants file
```

## Internal Details

- Uses `requests` for HTTP requests.  
- URL variants are built using `urllib.parse.urljoin` to ensure valid URLs.  
- Handles network exceptions gracefully.  
- Uses `colorama` for colored terminal output.  
- Interactive CLI with `print()` and `input()` for user interaction.
- Uses concurrent.futures.ThreadPoolExecutor for concurrent requests.

## Limitations and Future Work

- Current fuzzing is based on a static list; future improvements could include dynamic variant generation.   
- Content comparison to detect significant differences between responses.  
- Exporting results to CSV or JSON.  
- Supporting other HTTP methods like POST or PUT.

## Contributing
Contributions are welcome! To contribute :
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

## License
This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.
