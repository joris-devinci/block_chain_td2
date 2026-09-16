import secrets
import hashlib
import hmac
from ecdsa import SigningKey, SECP256k1

BIP39_DICT = {}
with open("bip39_list.txt", "r") as file:
    for i, line in enumerate(file):
        BIP39_DICT[i] = line.strip()
BIP39_REVERSE_DICT = {value:key for key, value in BIP39_DICT.items()}



def generate_seed() -> list[str]: # 12 words

    print("=====Generating seed=====")

    entropic = secrets.randbits(128)
    entropic_bits = [(entropic >> i) & 1 for i in range(entropic.bit_length() - 1, -1, -1)]
    print(f"Entropic bits = \n{entropic_bits}\n")

    digest = hashlib.sha256(entropic.to_bytes(16, "big")).digest()
    digest_bits = [(byte >> i) & 1 for byte in digest for i in range(7, -1, -1)]
    print(f"Hash digest bits = \n{digest_bits}\n")

    combined_bits = entropic_bits + digest_bits[:4]
    print(f"Entropic combined with checksome = \n{combined_bits}\n")

    index_list = []
    for i in range(11, 132+1, 11):
        index = "".join(str(val) for val in combined_bits[i-11:i])
        index_value = int(index, 2)
        index_list.append(index_value)
    print(f"Index list \n{index_list}\n")

    words_list = [BIP39_DICT[index] for index in index_list]
    print(f"Word list = {" ".join(words_list)}")

    return words_list



def get_root_seed(words_list: list[str]) -> bytes:
    print(f"=====Getting the Mnemonics root seed=====\n")

    index_list = []
    for word in words_list:
        index_list.append(BIP39_REVERSE_DICT[word])
    print(f"Index list = \n{index_list}\n")

    bits_list = [(index >> i) & 1 for index in index_list for i in range(10, -1, -1)]
    print(f"Bits list = \n{bits_list}\n")

    root_seed_list = bits_list[:-4]
    root_seed = int("".join(map(str, root_seed_list)), 2)
    print(f"Root list = \n{root_seed_list}\n")

    checksum = bits_list[-4:]
    print(f"Checksum = \n{checksum}\n")

    digest = hashlib.sha256(root_seed.to_bytes(16, "big")).digest()
    digest_bits = [(byte >> i) & 1 for byte in digest for i in range(7, -1, -1)]
    digest_checksum = digest_bits[:4]
    print(f"Checksum from digest from the root seed = \n{digest_checksum}\n")

    if checksum != digest_checksum:
        raise ValueError("Invaled words did not pass the checksum")

    root_seed = bytes(
        int("".join(map(str, root_seed_list[i:i+8])), 2)
        for i in range(0, len(root_seed_list), 8)
    )
    print(f"Root seed = {root_seed}\n")
    return root_seed


def generate_wallet() -> tuple[bytes, bytes, bytes]: # tuple(master private key, master chain key, master public key)

    value = input("Plz give me the Mnemonics words: ")
    words_list = value.split(" ")
    seed = get_root_seed(words_list)

    print("\n=====Generating a Wallet=====\n")

    hmac_output = hmac.new(b"Bitcoin seed", seed, "sha512").digest()
    print(f"HMAC output = \n{hmac_output}")

    masterprivatekey, masterchaincode = hmac_output[:32], hmac_output[32:]
    print(f"Master private key = \n{masterprivatekey}\n")
    print(f"Master chain code = \n{masterchaincode}\n")

    # Getting the master public key
    scalar = SigningKey.from_string(masterprivatekey, curve = SECP256k1)
    ecc = scalar.get_verifying_key() 
    masterpublickey = ecc.to_string("compressed") # 64 -> 32 bytes
    print(f"Master public key = \n{masterpublickey}\n")

    return masterprivatekey, masterchaincode, masterpublickey


def generate_child(private_key, public_key, chain_key, index) -> tuple[int, int, int]:  # tuple(master private key, master chain key, master public key)
    pass

    # Genertate private and chain key

    # Generate public key


# ========================================
# TEST FUNCTIONS
# ========================================

# generate_seed()
# get_root_seed(["winter", "tree", "talent", "plug", "flavor", "horror", "intact", "weird", "loyal", "turtle", "city", "comfort"])



# ========================================
# WHILE LOOP
# ========================================

while True:
    
    value = input("\nWhat do you want to do?\n" \
    "               1. Generate a seed\n" \
    "               2. Create a wallet\n" \
    "               3. Create child keys\n" \
    "               4. Exit\n")

    match value:
        case "1":
            generate_seed()
        case "2":
            generate_wallet()
        case "3":
            generate_child()
        case "4":
            break
        case _:
            print("\nYou seleceted a invalid option please select (1, 2, 3 or 4)\n")