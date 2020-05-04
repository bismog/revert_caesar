#!/usr/bin/env python
import argparse

MAX_KEY_SIZE = 26

def getMessage():
    print('Enter your message:')
    return raw_input()

def caesar(num, offset):
    symbol = chr(num)
    num += offset
    if symbol.isupper():
        if num > ord('Z'):
            num -= MAX_KEY_SIZE
        elif num < ord('A'):
            num += MAX_KEY_SIZE
    elif symbol.islower():
        if num > ord('z'):
            num -= MAX_KEY_SIZE
        elif num < ord('a'):
            num += MAX_KEY_SIZE
    return num

def revert(num):
    symbol = chr(num)
    if symbol.isupper():
        # A_base + 25 - (num - A_base) = A_base * 2 + 25 - num 
        num_o = ord('A') * 2 + MAX_KEY_SIZE - 1 - num
    elif symbol.islower():
        # a_base + 25 - (num - a_base) = a_base * 2 + 25 - num 
        num_o = ord('a') * 2 + MAX_KEY_SIZE - 1 - num
    return num_o
    

def getTranslatedMessage(message, decrypt, offset):
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            if decrypt:
                num = caesar(revert(num), -offset)
            else:
                num = revert(caesar(num, offset))
            translated += chr(num)
        else:
            translated += symbol
    return translated


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt.')
    parser.add_argument('-d', action="store_true", dest='decrypt', default=False)
    parser.add_argument('-l', action="store", dest="length", default=3)
    args = parser.parse_args()
    message = getMessage()
    print(getTranslatedMessage(message, args.decrypt, args.length))
