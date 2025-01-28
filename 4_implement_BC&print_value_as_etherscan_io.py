import hashlib
import datetime

# Class representing a single block in the blockchain
class Block:
    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number  # Block number in the chain
        self.timestamp = datetime.datetime.now()  # Current timestamp of block creation
        self.transactions = transactions  # Transaction data within the block
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.gas_limit = gas_limit  # Gas limit associated with the block
        self.gas_used = gas_used  # Gas used within the block
        self.miner = miner  # Address or identity of the miner
        self.hash = self.calculate_hash()  # Hash of the current block

    # Method to calculate the hash of the block
    def calculate_hash(self):
        data_string = (
            str(self.block_number)
            + str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.gas_limit)
            + str(self.gas_used)
            + str(self.miner)
        )
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

# Class representing the blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize blockchain with the genesis block

    # Method to create the genesis block (first block in the blockchain)
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", 0, 0, "Genesis Miner")

    # Method to add a new block to the blockchain
    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash  # Set the previous hash to the last block's hash
        self.chain.append(new_block)  # Append the new block to the chain

    # Method to print all the details of a block
    def print_block(self, block):
        print("Block Number:", block.block_number)
        print("Timestamp:", block.timestamp)
        print("Transactions:", block.transactions)
        print("Previous Hash:", block.previous_hash)
        print("Gas Limit:", block.gas_limit)
        print("Gas Used:", block.gas_used)
        print("Miner:", block.miner)
        print("Hash:", block.hash)
        print("")

    # Method to traverse the blockchain and print all blocks
    def traverse_chain(self):
        for block in self.chain:
            self.print_block(block)

# Create a new blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain with specific details
my_blockchain.add_block(Block(1, "Transaction 1", "", 1000000, 500000, "Miner 1"))
my_blockchain.add_block(Block(2, "Transaction 2", "", 2000000, 1500000, "Miner 2"))
my_blockchain.add_block(Block(3, "Transaction 3", "", 3000000, 2500000, "Miner 3"))

# Traverse the blockchain and print all the details of each block
my_blockchain.traverse_chain()
