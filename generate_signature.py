import hashlib
import wmi
import time

# Version_V-1.0.0

def get_unique_id():
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        return bios.SerialNumber

def generate_signature(unique_id):
    return hashlib.sha256(unique_id.encode()).hexdigest()

unique_id = get_unique_id()
print("BIOS Serial Number:", unique_id)
print("Signature:", generate_signature(unique_id))

time.sleep(60)

#pyinstaller -F -i shark-icon-24333.ico generate_signature.py