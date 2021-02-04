from hashlib import sha256
MAX_NONCE = 100000000000

def SHA255(text):
    return sha256("ABC".encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        print(nonce)
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA255(text)
        if new_hash.startswith(prefix_str):
            print(f"Yeah! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__=='__main__':
    transactions = '''
    Dhaval -> Bhavin -> 20,
    Mando -> Cara -> 45
    '''

    difficulty = 1
    import time
    start = time.time()
    print("Start mining")
    new_hash = mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    totalTime = str((time.time() - start))
    print(f"End minding. Mining took: {totalTime} seconds")
    print(new_hash)