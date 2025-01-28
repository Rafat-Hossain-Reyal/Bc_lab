import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(data_blocks):
    if not data_blocks:
        return None, []
    current_level = [hash_data(block) for block in data_blocks]
    tree_levels = [current_level]
    while len(current_level) > 1:
        next_level = []
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            next_level.append(hash_data(combined))
        tree_levels.append(next_level)
        current_level = next_level
    return current_level[0], tree_levels

def generate_proof(word, data_blocks, tree_levels):
    word_hash = hash_data(word)
    if word_hash not in tree_levels[0]:
        return None, []
    proof = []
    index = tree_levels[0].index(word_hash)
    current_index = index
    for level in tree_levels[:-1]:
        sibling_index = current_index ^ 1
        if sibling_index < len(level):
            proof.append((level[sibling_index], current_index % 2 == 0))
        current_index //= 2
    return word_hash, proof

def verify_proof(word_hash, proof, merkle_root):
    current_hash = word_hash
    for sibling_hash, is_left in proof:
        if is_left:
            current_hash = hash_data(current_hash + sibling_hash)
        else:
            current_hash = hash_data(sibling_hash + current_hash)
    return current_hash == merkle_root

def print_merkle_tree(tree_levels):
    print("Merkle Tree Levels:")
    for level_num, level in enumerate(tree_levels):
        print(f"Level {level_num}:")
        for i, node in enumerate(level):
            if level_num == 0:
                print(f"  h({i+1})={node}")
            else:
                start = i * (2 ** level_num) + 1
                end = min((i + 1) * (2 ** level_num), len(tree_levels[0]))
                nodes = '+'.join(str(j) for j in range(start, end + 1))
                print(f"  h({nodes})={node}")

def print_proof(word, word_hash, proof, tree_levels):
    print("\nProof of Membership:")
    if proof:
        print(f"Word '{word}' is a member of the Merkle tree.")
        print(f"h({word})={word_hash}")
        print("Proof details:")
        for level, (sibling_hash, is_left) in enumerate(proof):
            position = "left" if is_left else "right"
            print(f"Level {level + 1}: Sibling hash on the {position} is {sibling_hash}")

def main():
    data = ["1", "2", "3", "4","5", "6", "7", "8"]
    merkle_root, tree_levels = build_merkle_tree(data)
    print_merkle_tree(tree_levels)
    word = "5"
    word_hash, proof = generate_proof(word, data, tree_levels)
    print_proof(word, word_hash, proof, tree_levels)
    is_valid = verify_proof(word_hash, proof, merkle_root)
    print(f"Verification result: {is_valid}")

if __name__ == "__main__":
    main()
