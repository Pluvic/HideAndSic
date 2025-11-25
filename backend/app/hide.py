# Logic for hiding and extracting a UTF-8 string in an image using LSB steganography

from PIL import Image


def hideStringInImage(imagePath: str, secretMessage: str, outputImagePath: str) -> None:
    """Hide `secretMessage` (UTF-8) inside the image at `imagePath` and save to `outputImagePath`.
    """
    img = Image.open(imagePath).convert("RGB")
    binary = ''.join(format(ord(c), '08b') for c in secretMessage) + '00000000'  # fin de message
    pixels = img.load()

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                break
        if idx >= len(binary):
            break
    img.save(outputImagePath)


def extractStringFromImage(imagePath: str) -> str:
    """Extract a hidden UTF-8 string from the image at `imagePath`.
    """
    img = Image.open(imagePath).convert("RGB")
    pixels = img.load()
    width, height = img.size

    bits = []
    byte_bits = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            byte_bits += str(r & 1)

            if len(byte_bits) == 8:
                byte = int(byte_bits, 2)
                if byte == 0:
                    return "".join(chr(b) for b in bits)

                bits.append(byte)
                byte_bits = ""

    return ""


