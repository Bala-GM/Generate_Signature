import hashlib
import wmi
import sys
import tkinter.messagebox as messagebox

def get_unique_id():
    """Get the unique BIOS serial number."""
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        return bios.SerialNumber

def generate_signature(unique_id):
    """Generate a SHA-256 hash based on the unique ID."""
    return hashlib.sha256(unique_id.encode()).hexdigest()

def is_authorized_pc(stored_signatures):
    """Check if the current PC's signature matches any authorized signature."""
    current_signature = generate_signature(get_unique_id())
    return current_signature in stored_signatures

# List of authorized PC signatures
AUTHORIZED_SIGNATURES = [
    "a169c71b542eb023007b83cd8eeb097d78b1ce7c80d81781ffd00b420c84b077",
    "6f771f8d9a8fafa6255c1a22428eace4d106d5706a573976d2126a45a673adbe"
]

if not is_authorized_pc(AUTHORIZED_SIGNATURES):
    print("Unauthorized system. This program cannot run on this PC.")
    messagebox.showinfo("Unauthorized system", "This program cannot run on this PC.")
    sys.exit()

print("Authorized system. Program running...")