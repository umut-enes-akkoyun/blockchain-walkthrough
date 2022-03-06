import hashlib
import json
import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="Konya Bilim Merkezi 11. Bilim Festivali", proof = 100)

#yeni blok oluşturmak JSON formatında. Bunu zincire eklemek.
    def new_block(self, proof, previous_hash = None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.asctime(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.chain[-1]['hash'] ,
        }
        self.pending_transactions = []
        block['hash'] = self.hash(block) #tüm bloğun alınmış hashi kendi içine ekstra olak eklenir
        if len(self.chain) == 0:
            self.chain.append(block)

        elif block['hash'][-3:] == "f11": #11. festivale özel sonu f11 ile biten mdancilik mekanizması
            self.chain.append(block)

        return block

    @property
    def last_block(self):
        return self.chain[-1]

#transfer sırası
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount }
        self.pending_transactions.append(transaction)
        
        return self.last_block['index'] + 1

#tüm bloğun hashi alınır
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
    for i in range(1000000000):
        t1 = blockchain.new_transaction('Umut', 'Satoshi' , '5 BTC')
        blockchain.new_block(i)
        if last_blockxx != len(blockchain.chain):
            last_blockxx = len(blockchain.chain)
            break
            
    print("{block_sayi}. block: ", blockchain.chain[block_sayi])
