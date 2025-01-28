import hashlib
import datetime

# Class representing a single block in the blockchain
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()  # Current timestamp
        self.data = data  # Data stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    # Calculate the hash of the block using SHA256
    def calculate_hash(self):
        data_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

# Class representing the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize the blockchain with a genesis block

    # Create the genesis block (first block in the chain)
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # Add a new block to the blockchain
    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash  # Set the previous hash to the hash of the last block
        self.chain.append(new_block)  # Append the new block to the chain

    # Traverse and print details of each block in the blockchain
    def traverse_chain(self):
        for block in self.chain:
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("")

# Create a new blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block("Transaction 1", ""))
my_blockchain.add_block(Block("Transaction 2", ""))
my_blockchain.add_block(Block("Transaction 3", ""))
my_blockchain.add_block(Block("Transaction 4", ""))

# Traverse and print the blockchain
my_blockchain.traverse_chain()
