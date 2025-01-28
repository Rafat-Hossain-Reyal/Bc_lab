import hashlib 
import datetime 

class Block:
    def __init__(self, timestamp, data, previous_hash): 
        self.timestamp = timestamp 
        self.data = data 
        self.previous_hash = previous_hash 
        self.hash = self.calculate_hash() 

    def calculate_hash(self): 
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) 
        return hashlib.sha256(hash_string.encode()).hexdigest() 

class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()] 

    def create_genesis_block(self): 
        return Block(datetime.datetime.now(), "Genesis Block", "0") 

    def get_latest_block(self): 
        return self.chain[-1] 

    def add_block(self, new_block): 
        new_block.previous_hash = self.get_latest_block().hash 
        new_block.hash = new_block.calculate_hash() 
        self.chain.append(new_block) 

    def is_valid(self): 
        for i in range(1, len(self.chain)): 
            current_block = self.chain[i] 
            previous_block = self.chain[i-1] 

            if current_block.hash != current_block.calculate_hash(): 
                return False 

            if current_block.previous_hash != previous_block.hash: 
                return False 

        return True 

# Create a blockchain and add blocks 
blockchain = Blockchain() 
blockchain.add_block(Block(datetime.datetime.now(), "Block 1", "")) 
blockchain.add_block(Block(datetime.datetime.now(), "Block 2", "")) 
blockchain.add_block(Block(datetime.datetime.now(), "Block 3", "")) 

# Check if the blockchain is valid 
print("Is blockchain valid?", blockchain.is_valid()) 

# Manipulating the blockchain (introducing an invalid block) 
blockchain.chain[1].data = "Modified Block" 

# Check if the manipulated blockchain is valid 
print("Is manipulated blockchain valid?", blockchain.is_valid())
