import hashlib
import json
from time import time

# Block class to represent each block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time when the block was created
        self.data = data  # Data (e.g., transaction details) stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.hash = self.calculate_hash()  # Current block's hash

    # Calculate the hash of the current block
    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Blockchain class to represent the entire blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize the blockchain with the genesis block

    # Create the first block (genesis block) of the blockchain
    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    # Add a new block to the blockchain
    def add_block(self, data):
        previous_block = self.chain[-1]  # Get the last block in the chain
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)  # Create a new block
        self.chain.append(new_block)  # Add the new block to the chain

    # Verify the integrity of the blockchain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Check if the current block's hash and previous block's hash are valid
            if current_block.hash != current_block.calculate_hash() or current_block.previous_hash != previous_block.hash:
                return False
        return True

# Example usage
blockchain = Blockchain()
blockchain.add_block("Transaction 1")  # Add first transaction
blockchain.add_block("Transaction 2")  # Add second transaction
blockchain.add_block("Transaction 3")  # Add third transaction

# Check if the blockchain is valid
print("Blockchain is valid:", blockchain.is_chain_valid())

# Simulate tampering with the blockchain
blockchain.chain[1].data = "Tampered Transaction"  # Modify the second block's data
blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()  # Recalculate the hash of the tampered block

# Check if the blockchain is still valid after tampering
print("Blockchain is valid after tampering:", blockchain.is_chain_valid())
