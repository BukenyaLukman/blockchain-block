import json
import hashlib

class Block:
    _id = None
    history = None
    parent_id = None
    parent_hash = None



block_A = Block()
block_A._id = 1
block_A.history = 'Bukenya likes cats'




block_B = Block()
block_B.id = 2
block_B.history = 'Sheena likes a dog'
block_B.parent_id = block_A._id
block_B.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()



block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dogs'
block_C.parent_id = block_B._id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()
block_A.history = 'Bukenya hates cats'
## Changing Bukenya's History,
## This is unfair to Nelson, We need to find a way to stop this



## Solution is to use private and public keys
# public key
# Private key
