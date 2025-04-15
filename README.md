# WiCrack-Py

**WiCrack-Py** is a Python-based Wi-Fi password cracking tool built using the `pywifi` library. This tool is designed for **educational purposes** to demonstrate the process of brute-forcing Wi-Fi passwords using a wordlist. It can be used to test the security of your own Wi-Fi networks.

> **Important**: This tool should only be used on networks for which you have **explicit permission** to test. Unauthorized access to networks is illegal.

---

## 🛠️ Features:
- **Brute-Force Wi-Fi Passwords**: Automatically tries each password from a wordlist.
- **Easy to Use**: Simply input your target SSID and provide a wordlist file.
- **Real-Time Feedback**: Displays the current password being tested and the result.
- **Educational Tool**: Helps you understand the importance of strong passwords and the vulnerabilities of Wi-Fi networks.

---

## 💻 Installation (Windows Only):

Follow these steps to get **WiCrack-Py** up and running on your machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/idushamanakacyber/WiCrack-Py.git

2. **Install the required libraries**:
   ```bash
   pip install pywifi 

## 🚀 Usage:

To use WiCrack-Py, follow these steps:

1. **Run the script**:

   ```bash
   python wicrack.py

2. Enter the target SSID and path to your wordlist when prompted.
3. The tool will begin testing passwords from the wordlist and display the progress in the terminal.

## 📝 Example:
*Here’s how it looks in the terminal**:

   ```
Enter target SSID: YourWiFi
Enter path to wordlist file: /path/to/wordlist.txt
Trying password: password1
Trying password: password2
...
Success! Password is: password123
   ```   

## ⚠️ Disclaimer:
This tool is for educational purposes only.

Use responsibly: Only test Wi-Fi networks you own or have explicit permission to test.

Unauthorized access to networks is illegal and punishable by law.

## 📜 License:
This project is licensed under the MIT License - see LICENSE for details.

## 👨‍💻 Author:
Idusha Manaka

GitHub: @idushamanakacyber
