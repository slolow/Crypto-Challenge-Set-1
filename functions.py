import codecs
from bitarray import bitarray


def hex_to_base64(_hex):
    """ converts hex string to base 64 """

    return codecs.encode(codecs.decode(_hex, 'hex'), 'base64').decode()


def xor_hex(_hex1, _hex2):
    """"
    take xor of two hex strings and returns result in hex

    1. converts hex to bytes and bytes to bit arrays 
    2. perform xor on bit arrays
    3. Transform result back two hex
    """

    ba1 = bitarray()
    ba2 = bitarray()
    ba1.frombytes(bytes.fromhex(_hex1))
    ba2.frombytes(bytes.fromhex(_hex2))
    xor = ba1 ^ ba2

    return xor.tobytes().hex()


def xor_hex_2(_hex1, _hex2):
    """ xor of two hex strings. returns result in hex string"""
    
    int1 = int(_hex1, base=16)
    int2 = int(_hex2, base=16)
    int_res = int1 ^ int2

    return hex(int_res)[2:]


def single_char_xor(char_value, input_bytes):
    """XOR a single character against every byte of input_bytes
    
    char_value: int representing char in ASCII table
    input_bytes: bytes

    return: bytearray
    """
    print('input_bytes: ' + str(type(input_bytes)))
    output_bytes = bytearray()
    for byte in input_bytes: 
        print('byte: ' + str(type(byte)))
        output_bytes.append(char_value ^ byte)
    return output_bytes


def get_english_score(input_bytes):
    """Compares each input byte to a character frequency chart and returns
    the score of a message based on the relative frequency the characters 
    occur in the English language"""

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def repeating_key_XOR(input_bytes, key):
    """encrypt input_bytes with key using the repeating-key XOR algorithm """
    output_bytes = bytearray()
    div = len(key)
    i = 0 
    for byte in input_bytes:
        # example: len(key) = 3 --> and i = 2 --> i % div = 2 % 3 = 2, i = 3 --> i % div = 0 
        output_bytes.append(byte ^ ord(key[i % div])) 
        i += 1

    return output_bytes


def hamming_distance(string1, string2):
    """hamming distance measures the minimum number of substitutions
    required to change one string into the other string.
    It is just the number of different bits
    """

    a = bitarray()
    b = bitarray()
    a.frombytes(string1.encode())
    b.frombytes(string2.encode())
    c = a ^ b
    return sum(c)


