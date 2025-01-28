import hashlib 
import time 
import random

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
    def __init__(self, staking_pool):
        self.chain = [self.create_genesis_block()]  # Initialize with the genesis block
        self.staking_pool = staking_pool  # Dictionary of stakeholders with their stakes

    def create_genesis_block(self): 
        return Block("Genesis Block", "0")  # The first block with no previous hash

    def get_latest_block(self): 
        return self.chain[-1]  # Get the latest block

    def choose_validator(self):
        # Choose a validator based on their stake (more stake = higher chance of being chosen)
        total_stake = sum(self.staking_pool.values())  # Calculate the total stake
        rand = random.uniform(0, total_stake)  # Generate a random number between 0 and total stake
        
        # Print the random number for transparency
        print(f"Random number generated: {rand}")

        cumulative_stake = 0
        for stakeholder, stake in self.staking_pool.items():
            cumulative_stake += stake
            if cumulative_stake > rand:
                return stakeholder  # Return the selected validator
        return None  # Shouldn't happen if the staking pool isn't empty

    def add_block(self, data):
        # Choose a validator to add the new block
        validator = self.choose_validator()
        if validator:
            print(f"Block added by validator: {validator}")
            new_block = Block(data, self.get_latest_block().hash)
            new_block.previous_hash = self.get_latest_block().hash  # Set the previous hash
            new_block.hash = new_block.generate_hash()  # Generate the new block's hash
            self.chain.append(new_block)  # Add new block to the chain
        else:
            print("No validator selected.")

    def is_chain_valid(self): 
        # Check if the blockchain is valid by verifying hashes
        for i in range(1, len(self.chain)): 
            current_block = self.chain[i] 
            previous_block = self.chain[i-1] 
            if current_block.hash != current_block.generate_hash() or current_block.previous_hash != previous_block.hash: 
                return False 
        return True

# Example usage:
if __name__ == '__main__': 
    # Example stake amounts for users
    staking_pool = {'Alice': 100, 'Bob': 200, 'Charlie': 50}  # Dictionary of stakeholders and their stakes
    blockchain = Blockchain(staking_pool) 

    # Mine and add blocks to the blockchain
    print("Mining block 1...") 
    blockchain.add_block("Transaction 1") 

    print("Mining block 2...") 
    blockchain.add_block("Transaction 2") 

    print("Mining block 3...") 
    blockchain.add_block("Transaction 3") 

    # Verify the blockchain's validity
    print("Is blockchain valid? {}".format(blockchain.is_chain_valid()))
