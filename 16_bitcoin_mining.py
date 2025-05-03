import time
import hashlib

class Block:
    def __init__(self, transactions, previous_block_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_block_hash = previous_block_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_header = str(self.timestamp) + str(self.transactions) + str(self.previous_block_hash) + str(self.nonce)
        return hashlib.sha256(block_header.encode()).hexdigest()

    def mine_block(self, difficulty):
        print('Mining block...')
        start_time = time.time()

        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        time_elapsed = end_time - start_time

        print('Block mined:', self.hash)
        print('Time elapsed:', time_elapsed)

difficulty = 2

print('Mining genesis block...')
transactions = ['transaction1', 'transaction2', 'transaction3']
previous_block_hash = '0' * 64

block = Block(transactions, previous_block_hash)
block.mine_block(difficulty)

print('Mining block 1...')
transactions = ['transaction4', 'transaction5', 'transaction6']
previous_block_hash = block.hash

block = Block(transactions, previous_block_hash)
block.mine_block(difficulty)

print('Mining block 2...')
transactions = ['transaction7', 'transaction8', 'transaction9']
previous_block_hash = block.hash

block = Block(transactions, previous_block_hash)
block.mine_block(difficulty)
