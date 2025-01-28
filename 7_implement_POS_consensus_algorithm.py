import hashlib 
import time 

class Block: 
    def __init__(self, data, previous_hash): 
        self.timestamp = time.time()  # Block creation time
        self.data = data  # Data stored in the block
        self.previous_hash = previous_hash  # Previous block's hash
        self.hash = self.generate_hash()  # Generate block's hash

    def generate_hash(self): 
        # Combine block contents and hash them
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) 
        return hashlib.sha256(block_contents.encode()).hexdigest() 

class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()]  # Initialize with the genesis block

    def create_genesis_block(self): 
        return Block("Genesis Block", "0")  # The first block with no previous hash

    def get_latest_block(self): 
        return self.chain[-1]  # Get the latest block

    def add_block(self, new_block): 
        # Set the previous hash and generate the new block's hash
        new_block.previous_hash = self.get_latest_block().hash 
        new_block.hash = new_block.generate_hash() 
        self.chain.append(new_block)  # Add new block to the chain

    def is_chain_valid(self): 
        # Check if the blockchain is valid by verifying hashes
        for i in range(1, len(self.chain)): 
            current_block = self.chain[i] 
            previous_block = self.chain[i-1] 
            if current_block.hash != current_block.generate_hash() or current_block.previous_hash != previous_block.hash: 
                return False 
        return True 

if __name__ == '__main__': 
    blockchain = Blockchain() 

    # Mine and add blocks to the blockchain
    print("Mining block 1...") 
    block1 = Block("Transaction 1", "") 
    blockchain.add_block(block1) 

    print("Mining block 2...") 
    block2 = Block("Transaction 2", "") 
    blockchain.add_block(block2) 

    print("Mining block 3...") 
    block3 = Block("Transaction 3", "") 
    blockchain.add_block(block3) 

    # Verify the blockchain's validity
    print("Is blockchain valid? {}".format(blockchain.is_chain_valid()))
