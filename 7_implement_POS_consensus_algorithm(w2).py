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
    def __init__(self, staking_pool, minimum_stake=10):
        self.chain = [self.create_genesis_block()]  # Initialize with the genesis block
        self.staking_pool = staking_pool  # Dictionary of stakeholders with their stakes
        self.minimum_stake = minimum_stake  # Minimum stake required to participate

    def create_genesis_block(self):
        return Block("Genesis Block", "0")  # The first block with no previous hash

    def get_latest_block(self):
        return self.chain[-1]  # Get the latest block

    def choose_validator(self):
        # Filter out validators with stakes below the minimum requirement
        eligible_validators = {k: v for k, v in self.staking_pool.items() if v >= self.minimum_stake}
        if not eligible_validators:
            print("No eligible validators available.")
            return None

        total_stake = sum(eligible_validators.values())  # Calculate the total stake
        rand = random.uniform(0, total_stake)  # Generate a random number between 0 and total stake

        cumulative_stake = 0
        for stakeholder, stake in eligible_validators.items():
            cumulative_stake += stake
            if cumulative_stake > rand:
                return stakeholder  # Return the selected validator
        return None  # Shouldn't happen if the staking pool isn't empty

    def reward_validator(self, validator):
        # Reward the validator by increasing their stake
        reward_amount = 10  # Example reward amount
        self.staking_pool[validator] += reward_amount
        print(f"{validator} rewarded with {reward_amount} stake. Total stake: {self.staking_pool[validator]}")

    def slash_validator(self, validator):
        # Penalize the validator by reducing their stake
        penalty_amount = 10  # Example penalty amount
        self.staking_pool[validator] = max(0, self.staking_pool[validator] - penalty_amount)
        print(f"{validator} penalized with {penalty_amount} stake. Total stake: {self.staking_pool[validator]}")

    def add_block(self, data):
        # Choose a validator to add the new block
        validator = self.choose_validator()
        if validator:
            print(f"Block proposed by validator: {validator}")
            new_block = Block(data, self.get_latest_block().hash)
            # Simulate block validation (validity check can be more complex)
            if new_block.generate_hash() == new_block.hash:  # Simple validity check
                print(f"Block accepted by the network, added by {validator}")
                self.chain.append(new_block)
                self.reward_validator(validator)  # Reward the validator
            else:
                print("Block rejected due to invalid data!")
                self.slash_validator(validator)  # Slash the validator for invalid block
        else:
            print("No validator selected. Block not added.")

    def is_chain_valid(self):
        # Check if the blockchain is valid by verifying hashes
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.generate_hash() or current_block.previous_hash != previous_block.hash:
                return False
        return True

    def update_stake(self, stakeholder, amount):
        # Dynamically update stake (positive to stake, negative to withdraw)
        if stakeholder in self.staking_pool:
            self.staking_pool[stakeholder] = max(0, self.staking_pool[stakeholder] + amount)
            print(f"{stakeholder}'s stake updated by {amount}. Total stake: {self.staking_pool[stakeholder]}")
        else:
            if amount > 0:
                self.staking_pool[stakeholder] = amount
                print(f"{stakeholder} added to staking pool with {amount} stake.")
            else:
                print(f"Invalid operation. Cannot withdraw from non-existent stakeholder.")

# Example usage:
if __name__ == '__main__':
    # Example stake amounts for users
    staking_pool = {'Alice': 100, 'Bob': 50, 'Charlie': 20}
    blockchain = Blockchain(staking_pool, minimum_stake=10)

    # Dynamically update stakes
    blockchain.update_stake('Alice', 50)  # Alice adds more stake
    blockchain.update_stake('Charlie', -10)  # Charlie withdraws some stake
    blockchain.update_stake('Dave', 30)  # New participant Dave joins

    # Mine and add blocks to the blockchain
    print("\nMining block 1...")
    blockchain.add_block("Transaction 1")

    print("\nMining block 2...")
    blockchain.add_block("Transaction 2")

    print("\nMining block 3...")
    blockchain.add_block("Transaction 3")

    # Verify the blockchain's validity
    print("\nIs blockchain valid? {}".format(blockchain.is_chain_valid()))
