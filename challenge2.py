import time
from functions import xor_hex, xor_hex_2


print()
hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'
print(hex1)
print(hex2)
print()
print('function 1:')
start = time.time()
print(xor_hex(hex1, hex2))
end = time.time()
print('time: ' + str(end - start))
print()
print('function 2:')
start = time.time()
print(xor_hex_2(hex1, hex2))
end = time.time()
print('time: ' + str(end - start))

