import hashlib 

class Block: 
    def __init__(self, data, previous_hash): 
        self.data = data 
        self.previous_hash = previous_hash 
        self.hash = self.calculate_hash() 

    def calculate_hash(self): 
        sha = hashlib.sha256() 
        sha.update(self.data.encode('utf-8') + self.previous_hash.encode('utf-8')) 
        return sha.hexdigest() 

class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()] 

    def create_genesis_block(self): 
        return Block("Genesis Block", "0") 

    def add_block(self, new_block): 
        new_block.previous_hash = self.chain[-1].hash 
        new_block.hash = new_block.calculate_hash() 
        self.chain.append(new_block) 

    def validate_chain(self): 
        for i in range(1, len(self.chain)): 
            current_block = self.chain[i] 
            previous_block = self.chain[i-1] 

            if current_block.hash != current_block.calculate_hash(): 
                print('Invalid hash for block', i) 
                return False 

            if current_block.previous_hash != previous_block.hash: 
                print('Invalid previous hash for block', i) 
                return False 

        print('Blockchain is valid') 
        return True 

    def get_chain_length(self): 
        return len(self.chain) 

    def get_chain_hashrate(self): 
        total_hashrate = 0 
        for block in self.chain: 
            total_hashrate += int(block.hash, 16) 
        return total_hashrate 

    def check_for_51_percent_attack(self): 
        chain_length = self.get_chain_length() 
        total_hashrate = self.get_chain_hashrate() 
        for i in range(chain_length): 
            block_hash = int(self.chain[i].hash, 16) 
            if block_hash / total_hashrate > 0.51: 
                print('51% attack detected at block', i) 
                return True 

        print('No 51% attack detected') 
        return False
