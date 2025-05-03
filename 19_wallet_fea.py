import requests 

# Function to check balance of a wallet 
def check_balance(address): 
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance" 
    response = requests.get(url) 
    if response.status_code == 200: 
        balance = response.json()['balance'] 
        print(f"Balance of {address}: {balance} satoshis") 
    else: 
        print("Error checking balance") 

# Function to view transaction history of a wallet 
def view_history(address): 
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full" 
    response = requests.get(url) 
    if response.status_code == 200: 
        history = response.json()['txs'] 
        for tx in history: 
            print(f"Transaction hash: {tx['hash']}")
            print(f"Amount: {tx['total']} satoshis") 
            print(f"Confirmations: {tx['confirmations']}\n") 
    else: 
        print("Error viewing transaction history") 

# Function to create multiple addresses within a wallet 
def create_address(): 
    url = "https://api.blockcypher.com/v1/btc/main/addrs" 
    response = requests.post(url) 
    if response.status_code == 201: 
        address = response.json()['address'] 
        print(f"New address created: {address}") 
    else: 
        print("Error creating new address") 

# Function to set transaction fees 
def set_fees(fees): 
    # Your code to set transaction fees goes here 
    print(f"Transaction fees set to {fees} satoshis") 

# Sample usage of the functions 
address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2" 
check_balance(address) 
view_history(address) 
create_address() 
set_fees(100)
