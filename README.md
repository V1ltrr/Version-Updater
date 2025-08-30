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

**Windows Update Manager** is a lightweight Python tool designed to manage and update installed software on a Windows system.  
It scans all installed applications via the Windows registry and cross-references them with `winget` to identify available updates.  
Users can view installed software, check for updates, and perform updates centrally from a single interactive interface.

This tool is particularly useful for keeping multiple applications up-to-date efficiently, especially for users managing many programs on a Windows machine.

## Key Features
- Retrieves all installed software and their versions directly from the Windows registry.
- Checks for available updates using `winget`.
- Allows updating all software at once or updating a specific application by its `winget` ID.
- Verifies the version after each update to ensure successful installation.
- Interactive console interface with command-based navigation.
- Stylish white dynamic progress bar when scanning installed software.
- Colorized terminal output for better readability.
- Displays available commands after every action for easier usage.
- Cross-verification of software versions post-update.

## Requirements
- Windows 10 or higher
- Python 3.6 or higher
- Python packages:
  - `colorama`

## Installation
Clone the repository or download the source files :
```bash
git clone https://github.com/V1ltrr/version-updater.git
cd windows-update-manager
pip install colorama
```
## Usage
Run the script by launching :
```bash
python version_updater.py
```
### Steps
1. Use one of the available commands :
- list → Display all installed software.
- updates → Check which software has available updates.
- upgrade all → Update all software available via winget.
- upgrade <ID> → Update a specific software by its winget ID.
- exit → Quit the program.
     
2. Follow on-screen instructions to perform updates and verify software versions.

## Project Structure
```text
Version-Updater/
├── LICENCE              # This documentation file
├── README.md            # This documentation file
├── version_updater.py   # Main script
```

## Internal Details
- Uses winreg to read installed software from the Windows registry.
- Uses subprocess to interact with winget for updates.
- Colorama is used for colorized terminal output.
- Interactive CLI with print() and input() for user commands.
- Progress bar displayed during scanning of installed software.
- After each update, the script rechecks the installed version to confirm success.

## Contributing
Contributions are welcome! To contribute :
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
