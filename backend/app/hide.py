# Logic for hiding and extracting a UTF-8 string in an image using LSB steganography

from PIL import Image
from app.encrypt import encryptMessage, decryptMessage

def setUpMessageHiding(secret: str, encrypt: bool, key: bytes) -> bytes:
    """Prepare the secret message for hiding. If `encrypt` is True, encrypt the message using `key`.
    """
    if encrypt:
        iv, ciphertext = encryptMessage(secret, key)
        final = b"\xff" + len(iv).to_bytes(2, 'big') + iv + ciphertext
    else:
        final = b"\xee" + secret.encode('utf-8')
    
    length = len(final)
    return length.to_bytes(4, 'big') + final

def parseExtractedMessage(data: bytes, key: bytes) -> str:
    """Parse the extracted message data. If encrypted, decrypt it using `key`.
    """
    
    length = int.from_bytes(data[0:4], 'big')
    content = data[4:4+length]

    if content[0] == 0xff:
        iv_length = int.from_bytes(content[1:3], 'big')
        iv = content[3:3+iv_length]
        ciphertext = content[3+iv_length:]
        return decryptMessage(iv, ciphertext, key)
    else:
        return content[1:].decode('utf-8')

def hideStringInImage(imagePath: str, secretData: bytes, outputImagePath: str) -> None:
    """Hide `secretMessage` (UTF-8) inside the image at `imagePath` and save to `outputImagePath`.
    """
    img = Image.open(imagePath)
    binary = ''.join(format(byte, '08b') for byte in secretData) + '1111111111111111'
    pixels = img.load()

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary):
                r, g, b, a = pixels[x, y]
                r = (r & ~1) | int(binary[idx])
                pixels[x, y] = (r, g, b, a)
                idx += 1
            else:
                break
        if idx >= len(binary):
            break
    img.save(outputImagePath)


def extractStringFromImage(imagePath: str) -> bytes:
    """Extract a hidden UTF-8 string from the image at `imagePath`.
    """
    img = Image.open(imagePath)
    pixels = img.load()
    width, height = img.size

    bits = []
    byte_bits = ""
    previous_byte = None

    for y in range(height):
        for x in range(width):
            r, _, _, _ = pixels[x, y]

            byte_bits += str(r & 1)

            if len(byte_bits) == 8:
                byte = int(byte_bits, 2)
                if byte == 255 and previous_byte == 255:
                    return bytes(bits)

                bits.append(byte)
                byte_bits = ""
                previous_byte = byte

    return b""


