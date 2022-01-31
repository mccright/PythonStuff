import base64
import sys
# The Crypto module comes from pycryptodome
# https://pypi.org/project/pycryptodome/
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


# The following is a 64-character clear-text secret.  
# It is not useful code as-is.
# Under many circumstances you might be able to pull the secret
# at run time from the environment's 'secrets manager'
the_bytes = bytes('NHPt8v0gfvyVta9bhr5vwexum2oaxdwiuedqp3sgNDkkwnf5g9j7kwe2c1anvg38', "utf8")


def encrypt_aes_cbc(clear_text):
    input_text = bytes(clear_text, "utf8")
    # https://legrandin.github.io/pycryptodome/Doc/3.2/Crypto.Hash.CMAC-module.html
    # SHA256.digest: The size of the resulting hash in bytes = 32
    key = SHA256.new(the_bytes).digest()
    # https://legrandin.github.io/pycryptodome/Doc/3.2/Crypto.Cipher.AES-module.html
    # AES: size of a data block (in bytes) / block_size = 16
    #      Size of a key (in bytes) / key_size = (16, 24, 32) 
    IV = Random.new().read(AES.block_size)
    encrypt_it = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(input_text) % AES.block_size
    input_text += bytes([padding]) * padding
    data = IV + encrypt_it.encrypt(input_text)
    return base64.b64encode(data).decode("utf8")


def decrypt_aes_cbc(crypt_text):
    input_crypt_bytes = base64.b64decode(crypt_text.encode("utf8"))
    key = SHA256.new(the_bytes).digest()
    IV = input_crypt_bytes[:AES.block_size]
    decrypt_it = AES.new(key, AES.MODE_CBC, IV)
    data = decrypt_it.decrypt(input_crypt_bytes[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        return ""
    return data[:-padding].decode("utf8")


if __name__ == '__main__':
    # Storing the 'secret' clear text message in code like this
    # is not appropriate for any real-world use cases other than
    # demonstrations.  
    # clear_text_input = "This is some clear text content."
    # Asking for a string like below with little risk management
    # is still not going to be risk appropriate for most use cases.
    try:
        clear_text_input = input("Input your string for encryption: ")
    except Exception as e:
        print("Generic failure this run. Error: {} -- {}".format(e, (sys.exc_info())))
        exit()
    encrypted_text = encrypt_aes_cbc(clear_text_input)
    print(f"{encrypted_text}")
    clear_text_output = decrypt_aes_cbc(encrypted_text)
    print(f"{clear_text_output}")

