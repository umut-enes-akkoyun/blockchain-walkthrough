import hashlib
import json
import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="Konya Bilim Merkezi 11. Bilim Festivali", proof = 100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.
    def new_block(self, proof, previous_hash = None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.asctime(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.chain[-1]['hash'] ,
        }
        self.pending_transactions = []
        block['hash'] = self.hash(block)
        if len(self.chain) == 0:
            self.chain.append(block)

        elif block['hash'][-3:] == "f11":
            self.chain.append(block)

        return block

#Search the blockchain for the most recent block.
    @property
    def last_block(self):
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount }
        self.pending_transactions.append(transaction)
        
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash

blockchain = Blockchain()
last_blockxx = len(blockchain.chain)
print("Genesis block: ", blockchain.chain[0])

for block_sayi in range(1,5):
    from_user = input("From : ")
    to_user = input("\nto : ")
    amount = input("\nBTC amount :")
    for i in range(1000000000):
        t1 = blockchain.new_transaction(from_user, to_user , amount +  'BTC')
        blockchain.new_block(i)
        if last_blockxx != len(blockchain.chain):
            last_blockxx = len(blockchain.chain)
            break
            
    print("{block_sayi}. block: ", blockchain.chain[block_sayi])
