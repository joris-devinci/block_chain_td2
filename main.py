import secrets
import hashlib

BIP39_DICT = {}
with open("bip39_list.txt", "r") as file:
    for i, line in enumerate(file):
        BIP39_DICT[i] = line.strip()
BIP39_REVERSE_DICT = {value:key for key, value in BIP39_DICT.items()}

def generate_seed() -> list[str]: # 12 words

    print("Generating seed")

    entropic = secrets.randbits(128)
    entropic_bits = [(entropic >> i) & 1 for i in range(entropic.bit_length() - 1, -1, -1)]
    # print(f"Entropic bits = \n{entropic_bits}\n")

    digest = hashlib.sha256(entropic.to_bytes(16, "big")).digest()
    digest_bits = [(byte >> i) & 1 for byte in digest for i in range(7, -1, -1)]
    # print(f"Hash digest bits = \n{digest_bits}\n")

    combined_bits = entropic_bits + digest_bits[:4]
    # print(f"Entropic combined with checksome = \n{combined_bits}\n")

    index_list = []
    for i in range(11, 132+1, 11):
        index = "".join(str(val) for val in combined_bits[i-11:i])
        index_value = int(index, 2)
        index_list.append(index_value)
    # print(f"Index list \n{index_list}\n")

    words_list = [BIP39_DICT[index] for index in index_list]
    print(f"Word list = {" ".join(words_list)}")

    return words_list

# def get_root_seet(words_list: list[str]) -> tuple[int, int, int]:

#     index_list = []
#     for word in words_list:
#         index_list.append()
    

def generate_wallet(seed: list[bytes]) -> tuple[int, int, int]: # tuple(master private key, master chain key, master public key)
    pass

    # Generate the master private key and master chain key from the seed

    # Extract master public key


def generate_child(private_key, public_key, chain_key, index) -> tuple[int, int, int]:  # tuple(master private key, master chain key, master public key)
    pass

    # Genertate private and chain key

    # Generate public key


generate_seed()

# while True:

#     value = input("What do you want to do?\n" \
#     "               1. Generate a key\n" \
#     "               2. Create a wallet\n" \
#     "               3. Create child keys\n" \
#     "               4. Exit")

#     match value:
#         case "1":
#             pass
#         case "2":
#             pass
#         case "3":
#             pass
#         case "4":
#             break
#         case _:
#             print("Nothing good seleceted")