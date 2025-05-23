import datetime

class BlockNode:
    def __init__(self, data, timestamp=None):
        self.data = data
        self.timestamp = timestamp or datetime.datetime.now()
        self.next = None

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        new_block = BlockNode(data)
        if self.head is None:
            self.head = new_block
        else:
            current_block = self.head
            while current_block.next:
                current_block = current_block.next
            current_block.next = new_block

    def mine_block(self, data):
        new_block = BlockNode(data)
        new_block.next = self.head
        self.head = new_block

    def traverse(self):
        current_block = self.head
        while current_block:
            print(f"Block Data: {current_block.data}")
            print(f"Timestamp: {current_block.timestamp}")
            print()
            current_block = current_block.next

# Create a new blockchain
blockchain = Blockchain()

# Add blocks to the chain
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")

# Traverse the blockchain and print the data
print("Blockchain before mining new block:")
blockchain.traverse()

# Mine a new block and add it to the chain
blockchain.mine_block("Block 4")

# Traverse the blockchain again after mining new block
print("Blockchain after mining new block:")
blockchain.traverse()
