import hashlib
import time

# Block class represents a single block in the blockchain
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()  # Store the time when block is created
        self.data = data  # Data stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0  # Nonce value for mining
        self.hash = self.generate_hash()  # Generate initial hash

    # Generate SHA-256 hash for the block
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
        return block_hash

    # Mine the block by adjusting nonce until hash meets difficulty criteria
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        print("Block mined: {}".format(self.hash))

# Blockchain class represents the entire chain of blocks
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize blockchain with genesis block
        self.difficulty = 2  # Difficulty level for mining

    # Create the first block in the blockchain
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Add a new block to the blockchain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash  # Set previous block hash
        new_block.mine_block(self.difficulty)  # Mine the block
        self.chain.append(new_block)  # Append block to the chain

    # Verify if the blockchain is valid
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash is still valid
            if current_block.hash != current_block.generate_hash():
                return False

            # Check if the previous hash matches the stored value
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Main execution
if __name__ == "__main__":
    blockchain = Blockchain()
    print("Mining block 1...")
    block1 = Block("Transaction 1", "")
    blockchain.add_block(block1)

    print("Mining block 2...")
    block2 = Block("Transaction 2", "")
    blockchain.add_block(block2)

    print("Mining block 3...")
    block3 = Block("Transaction 3", "")
    blockchain.add_block(block3)

    # Validate the blockchain
    print("Is blockchain valid? {}".format(blockchain.is_chain_valid()))

    # Tampering with the blockchain
    blockchain.chain[1].data = "Transaction 12"
    print("Is blockchain valid after tampering? {}".format(blockchain.is_chain_valid()))
