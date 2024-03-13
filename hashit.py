import sys
import hashlib


def help_message():
    print("=" * 50)
    print("Usage: python script.py <algorithm> <keyword>")
    print("Options:")
    print("  <algorithm> - The hashing algorithm to use. Choose from:")
    print("md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256, "
          "blake2b, blake2s")
    print("  <keyword>   - The keyword to hash.")
    print("  all         - Compute all supported hash algorithms for the keyword.")
    print("  -h, --help  - Display this help message.")


def convert_keyword(hash_type):
    hash_value = hash_type(keyword.encode()).hexdigest()
    print(f"[+] Hash {algorithm} of '{keyword}': {hash_value}")


def algorithm_hash():
    if algorithm == "md5":
        hash_algorithm = hashlib.md5
    elif algorithm == "sha1":
        hash_algorithm = hashlib.sha1
    elif algorithm == "sha224":
        hash_algorithm = hashlib.sha224
    elif algorithm == "sha256":
        hash_algorithm = hashlib.sha256
    elif algorithm == "sha384":
        hash_algorithm = hashlib.sha384
    elif algorithm == "sha512":
        hash_algorithm = hashlib.sha512
    elif algorithm == "sha3_224":
        hash_algorithm = hashlib.sha3_224
    elif algorithm == "sha3_256":
        hash_algorithm = hashlib.sha3_256
    elif algorithm == "sha3_384":
        hash_algorithm = hashlib.sha3_384
    elif algorithm == "sha3_512":
        hash_algorithm = hashlib.sha3_512
    elif algorithm == "shake_128":
        hash_algorithm = hashlib.shake_128
    elif algorithm == "shake_256":
        hash_algorithm = hashlib.shake_256
    elif algorithm == "blake2b":
        hash_algorithm = hashlib.blake2b
    elif algorithm == "blake2s":
        hash_algorithm = hashlib.blake2s
    else:
        print("Invalid argument. Type -h or --h if you need any help.")
        return None, None

    return hash_algorithm


def all_hashes():
    hash_md5 = hashlib.md5(keyword.encode()).hexdigest()
    hash_sha1 = hashlib.sha1(keyword.encode()).hexdigest()
    hash_sha224 = hashlib.sha224(keyword.encode()).hexdigest()
    hash_sha256 = hashlib.sha256(keyword.encode()).hexdigest()
    hash_sha384 = hashlib.sha384(keyword.encode()).hexdigest()
    hash_sha512 = hashlib.sha512(keyword.encode()).hexdigest()
    hash_sha3_224 = hashlib.sha3_224(keyword.encode()).hexdigest()
    hash_sha3_256 = hashlib.sha3_256(keyword.encode()).hexdigest()
    hash_sha3_384 = hashlib.sha3_384(keyword.encode()).hexdigest()
    hash_sha3_512 = hashlib.sha3_512(keyword.encode()).hexdigest()
    hash_shake_128 = hashlib.shake_128(keyword.encode()).hexdigest(16)
    hash_shake_256 = hashlib.shake_256(keyword.encode()).hexdigest(32)
    hash_blake2b = hashlib.blake2b(keyword.encode()).hexdigest()
    hash_blake2s = hashlib.blake2s(keyword.encode()).hexdigest()

    print(f"All supported hashes to '{keyword}':")
    print(f"[+] Hash md5: {hash_md5}")
    print(f"[+] Hash sha1: {hash_sha1}")
    print(f"[+] Hash sha224: {hash_sha224}")
    print(f"[+] Hash sha256: {hash_sha256}")
    print(f"[+] Hash sha384: {hash_sha384}")
    print(f"[+] Hash sha512: {hash_sha512}")
    print(f"[+] Hash sha3_224: {hash_sha3_224}")
    print(f"[+] Hash sha3_256: {hash_sha3_256}")
    print(f"[+] Hash sha3_384: {hash_sha3_384}")
    print(f"[+] Hash sha3_512: {hash_sha3_512}")
    print(f"[+] Hash shake_128: {hash_shake_128}")
    print(f"[+] Hash shake_256: {hash_shake_256}")
    print(f"[+] Hash blake2b: {hash_blake2b}")
    print(f"[+] Hash blake2s: {hash_blake2s}")


try:
    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]:
        help_message()
    elif len(sys.argv) != 3:
        print("Invalid number of arguments. Type -h or --help if you need any help.")
    else:
        algorithm = str(sys.argv[1])
        keyword = str(sys.argv[2])

        if algorithm == "all":
            all_hashes()
        else:
            use_hash = algorithm_hash()
            if use_hash:
                convert_keyword(use_hash)

except IndexError:
    print("IndexError: Please type '-h --' if you need help.")
    print("Usage: python script.py <algorithm> <keyword>")

except TypeError:
    print(f"TypeError: Please provide a valid hashing algorithm.")
  
