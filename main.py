import secrets

def generate_seed(mnemonic:list[str]) -> list[bytes]: # 12 words
    pass
    # Generate random 128 bit number

    # Hash that number take the first 4 bits and add it to the random number

    # The you split the bits into 12 11 bit thing and search up the index of the words and jsut display them

    # return the bits



def generate_wallet(seed: list[str]) -> tuple[int, int, int]: # tuple(master private key, master chain key, master public key)
    pass

    # Generate the master private key and master chain key from the seed

    # Extract master public key


def generate_child(private_key, public_key, chain_key, index) -> tuple[int, int, int]:  # tuple(master private key, master chain key, master public key)
    pass

    # Genertate private and chain key

    # Generate public key



while True:

    value = input("What do you want to do?\n" \
    "               1. Generate a key\n" \
    "               2. Create a wallet\n" \
    "               3. Create child keys\n" \
    "               4. Exit")

    match value:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            break
        case _:
            print("Nothing good seleceted")