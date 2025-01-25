import hashlib
import wmi

def get_unique_id():
    """Get the unique BIOS serial number."""
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        return bios.SerialNumber

def generate_signature(unique_id):
    """Generate a SHA-256 hash based on the unique ID."""
    return hashlib.sha256(unique_id.encode()).hexdigest()

def is_authorized_pc(stored_signature):
    """Compare the current PC's signature with the authorized signature."""
    current_signature = generate_signature(get_unique_id())
    return stored_signature == current_signature

# Replace this with the signature of the authorized PC
AUTHORIZED_SIGNATURE = "precomputed_signature_here" #a169c71b542eb023007b83cd8eeb097d78b1ce7c80d81781ffd00b420c84b077

if not is_authorized_pc(AUTHORIZED_SIGNATURE):
    print("Unauthorized system. This program cannot run on this PC.")
    exit(1)

print("Authorized system. Program running...")
