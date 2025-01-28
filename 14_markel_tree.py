import hashlib

# Function to compute the SHA-256 hash of a given string
def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to build a Merkle Tree from a list of data blocks
def build_merkle_tree(data_blocks):
    # Handle the case where no data blocks are provided
    if not data_blocks:
        return None, []

    # Initialize the current level with the hashes of the data blocks (leaf nodes)
    current_level = [hash_data(block) for block in data_blocks]
    # Store all levels of the tree for reference
    tree_levels = [current_level]

    # Loop until we reduce the tree to a single root hash
    while len(current_level) > 1:
        next_level = []
        
        # If the number of nodes is odd, duplicate the last node
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        # Combine pairs of nodes, hash them, and add to the next level
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            next_level.append(hash_data(combined))
        
        # Append the next level to the tree levels
        tree_levels.append(next_level)
        # Move to the next level
        current_level = next_level

    # Return the root hash (last remaining hash) and the entire tree structure
    return current_level[0], tree_levels

# Function to print the Merkle Tree levels in a readable format
def print_merkle_tree(tree_levels):
    print("Merkle Tree Levels:")
    # Iterate through each level of the tree
    for level_num, level in enumerate(tree_levels):
        print(f"Level {level_num}:")
        # Print each node at the current level
        for i, node in enumerate(level):
            if level_num == 0:
                # Leaf nodes are hashes of individual data blocks
                print(f"  h({i+1})={node}")
            else:
                # Compute the range of leaf nodes combined to form this node
                start = i * (2 ** level_num) + 1
                end = min((i + 1) * (2 ** level_num), len(tree_levels[0]))
                nodes = '+'.join(str(j) for j in range(start, end + 1))
                print(f"  h({nodes})={node}")

# Main function to demonstrate the Merkle Tree construction
def main():
    # Example input data blocks
    data = ["block1", "apple", "app"]

    # Build the Merkle Tree and get the root hash and tree levels
    merkle_root, tree_levels = build_merkle_tree(data)

    # Print the Merkle Tree levels
    print_merkle_tree(tree_levels)

if __name__ == "__main__":
    main()
