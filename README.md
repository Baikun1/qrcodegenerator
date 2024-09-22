# QR Code Generator (Command Line)

This project is a simple Python application that allows users to generate and save QR codes from a URL or string input. The application can take a link as input interactively or as a command-line argument.

## Requirements

- Python 3.x
- The following Python libraries:
  - `pyqrcode`
  - `pypng`

## Installation

1. Clone this repository to your local machine:
   ```bash
     git clone https://github.com/your-username/qr-code-generator.git
     cd qr-code-generator
   ```
2. Install the required libraries:
   ```bash
    pip install pyqrcode pypng
  ```

## Usage

1. Method 1: Interactive Input:
  - Run the script using the following command:
  
  ```bash
  python qr_code_generator.py
  ```
  - You will be prompted to enter a URL or string to generate the QR code.
  
  - After the QR code is generated, the script will ask if you want to save the QR code as a .png file.
  
  - If you choose to save it, enter the full path and filename where you want to save the QR code (including the .png extension).

2. Method 2: Command-Line Argument:
  - You can also provide the URL or string as a command-line argument when running the script:
  
  ```bash
  python qr_code_generator.py "https://www.example.com"
  ```
  - The script will generate the QR code for the provided link and then ask if you want to save it.

## Example:
```bash
python qr_code_generator.py
Enter URL or string to generate QR code: https://www.example.com
Do you want to save the QR code? (yes/no): yes
Enter the full path to save the QR code (with .png extension): /path/to/save/qr_code.png
Success: QR code saved as /path/to/save/qr_code.png
```
