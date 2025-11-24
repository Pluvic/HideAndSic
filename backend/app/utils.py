import hashlib
from itertools import count
import math

def calculateHashes(filePath: str) -> dict:
    """Calculate MD5, SHA1, and SHA256 hashes of a file."""
    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()
    hash_sha256 = hashlib.sha256()

    with open(filePath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            hash_sha1.update(chunk)
            hash_sha256.update(chunk)

    return {
        "md5": hash_md5.hexdigest(),
        "sha1": hash_sha1.hexdigest(),
        "sha256": hash_sha256.hexdigest(),
    }

def calculateEntropy(filePath: str) -> float:
    """Calculate the entropy of a file."""
    with open(filePath, "rb") as f:
        byteArr = list(f.read())
        if not byteArr:
            return 0
        occurrences = [0] * 256
        for byte in byteArr:
            occurrences[byte] += 1
        entropy = 0
        for count in occurrences:
            if count == 0:
                continue
            p = count / len(byteArr)
            entropy -= p * math.log2(p)
        return entropy