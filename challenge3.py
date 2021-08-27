"""
Found result at https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/

ASCII Table has 256 single characters mapped to integers from 0 to 255
XOR every single character from ASCII Table against every byte from cipertext
to get plain text

Result key is key 88 --> X
""" 

from functions import single_char_xor, get_english_score

hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ciphertext = bytes.fromhex(hexstring)
potential_messages = []
for k in range(256):
    message = single_char_xor(k, ciphertext)
    score = get_english_score(message)
    data = {
        'message': message, 
        'score': score, 
        'key': k
    }
    potential_messages.append(data)
best_score = sorted(potential_messages, key= lambda x: x['score'], reverse=True)[0]
for item in best_score:
    print(f'{item.title()}: {best_score[item]}')





