import wmi

def get_unique_id():
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        return bios.SerialNumber

print("BIOS Serial Number:", get_unique_id())


import hashlib

def generate_signature(unique_id):
    return hashlib.sha256(unique_id.encode()).hexdigest()

unique_id = get_unique_id()
signature = generate_signature(unique_id)
print("Signature:", signature)

