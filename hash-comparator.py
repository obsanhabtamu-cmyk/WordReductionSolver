import hashlib

file = 'File.gz'

def generate_hash(file):
    sha256 = hashlib.sha256()
    # Open the file in binary read mode ('rb')
    with open(file, 'rb') as file:
        # Read the file in 8192-byte chunks until the end
        while chunk := file.read(8192):
            sha256.update(chunk)
    # Return the 64-character hexadecimal fingerprint
    return sha256.hexdigest()

calculated_hash = generate_hash(file)
expected_hash = "f87d7888e40eb108a7e3c72ae32114e26d2774045155aa09360719d2b2a241a7" # the hash we expect

if calculated_hash != expected_hash:
    print("ERROR: File hash does not match!")
    print(f"Expected:   {expected_hash}")
    print(f"Calculated: {calculated_hash}")
    exit()
else:
    print(f"the file {file} is Safe")