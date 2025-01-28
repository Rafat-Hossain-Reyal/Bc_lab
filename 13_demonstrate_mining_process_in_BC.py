import hashlib
import time

# Define the block header fields
version = 1
previous_block_hash = "00000000000000000007d28e1a9ac3b37760e3b7bbd3df2b8f670a434f1a86"
merkle_root = "9d7d1c2f4a2e7f520d33de8e7bb28132586d30ef7c6d9b9e446e6c12d1f2c25"
timestamp = int(time.time())
difficulty = 4  # Number of leading zeros required in the hash
nonce = 0

# Combine the header fields into a single string
header = str(version) + previous_block_hash + merkle_root + str(timestamp) + str(difficulty)

# Mining loop to find a valid hash
while True:
    # Add the nonce value to the header
    header_with_nonce = header + str(nonce)
    
    # Compute the SHA-256 hash of the header with nonce
    hash = hashlib.sha256(header_with_nonce.encode()).hexdigest()
    
    # Check if the hash meets the difficulty target
    if hash[:difficulty] == "0" * difficulty:
        print("Block mined successfully!")
        print("Nonce:", nonce)
        print("Hash:", hash)
        break
    
    # Increment the nonce and try again
    nonce += 1
