# This file will contain the logic for hiding string in a picture using LSB steganography

from PIL import Image
import os

def hideStringInImage(imagePath: str, secretMessage: str, outputImagePath: str) -> None:
    # Open the image
    image = Image.open(imagePath)
    encoded = image.copy()
    width, height = image.size

    # Convert the secret message to binary
    binaryMessage = ''.join(format(ord(char), '08b') for char in secretMessage)
    binaryMessage += '1111111111111110'  # Delimiter to indicate end of message

    dataIndex = 0
    messageLength = len(binaryMessage)

    for y in range(height):
        for x in range(width):
            if dataIndex < messageLength:
                pixel = list(encoded.getpixel((x, y)))
                for n in range(3):
                    if dataIndex < messageLength:
                        pixel[n] = pixel[n] & ~1 | int(binaryMessage[dataIndex])
                        dataIndex += 1
                encoded.putpixel((x, y), tuple(pixel))
            else:
                break
        if dataIndex >= messageLength:
            break

    # Save the modified image
    encoded.save(outputImagePath)

def extractStringFromImage(imagePath: str) -> str:
    # Open the image
    image = Image.open(imagePath)
    width, height = image.size

    binaryMessage = ""
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                binaryMessage += str(pixel[n] & 1)

    # Split by 8-bits
    allBytes = [binaryMessage[i:i+8] for i in range(0, len(binaryMessage), 8)]
    
    # Convert from bits to characters
    message = ""
    for byte in allBytes:
        char = chr(int(byte, 2))
        if char == chr(255):  # Delimiter found
            break
        message += char

    return message