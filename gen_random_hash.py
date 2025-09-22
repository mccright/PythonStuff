import uuid
import hashlib

"""
This is just a reminder about hashing...
Here is what hashlib provides:
hashlib: algorithms_available
hashlib: algorithms_guaranteed
hashlib: blake2b
hashlib: blake2s
See: https://medium.com/@kdaminingclub/unraveling-the-blake2s-hash-algorithm-a-comprehensive-guide-8eb00c95c52c
"Compared to other algorithms like SHA-256 and SHA-3, Blake2S is just as secure but much faster. This makes it a popular choice for many people and companies (Aumasson et al., 2013)."
hashlib: file_digest
hashlib: md5
hashlib: new
hashlib: pbkdf2_hmac
hashlib: sha1
hashlib: sha224
hashlib: sha256
hashlib: sha384
hashlib: sha3_224
hashlib: sha3_256
hashlib: sha3_384
hashlib: sha3_512
hashlib: sha512
hashlib: shake_128
hashlib: shake_256

"""

ones = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
tens = "1        10        20        30        40        50        60        70        8"
separator = '-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -'

def generate_random_hash() -> tuple[str, str]:
    random_uuid = str(uuid.uuid4()).encode('utf-8')
    # print(f"random uuid = {random_uuid}")
    # Use the algorithm most appropriate to your use case.
    # hash_object = hashlib.sha512()
    # hash_algo = "sha512"
    # hash_object = hashlib.sha256()
    # hash_algo = "sha256"
    # hash_object = hashlib.sha1()
    # hash_algo = "sha1"
    # hash_object = hashlib.blake2b()
    # hash_algo = "blake2b"
    # I'm using blake for safety, speed, 
    # simplicity and possibly quantum readiness.
    hash_object = hashlib.blake2s()
    hash_algo = "blake2s"
    # hash_object = hashlib.shake_128()
    # hash_algo = "shake_128"
    hash_object.update(random_uuid)
    return hash_object.hexdigest(), hash_algo


def explore_hashlib():
    print(f"{separator}")
    eh = ''
    for eh in sorted(hashlib.__all__):
        print('hashlib: ', end='')
        print(eh, end='\n')

    print(f"{separator}\r\n")


def explore_hashlib_algos():
    print(f"{separator}\r\n")
    print(f"hashlib.algorithms_available: {hashlib.algorithms_available}")
    print(f"{separator}\r\n")
    print(f"hashlib.algorithms_guaranteed: {hashlib.algorithms_guaranteed}")
    print(f"{separator}\r\n")


random_hash, hash_algo = generate_random_hash()
print(f"Random Hash using {hash_algo}:")
print(f"{random_hash}")
# print(f"{ones}")
# print(f"{tens}")
