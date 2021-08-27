"""Remarks see challenge3.py 
Result key is 53 --> '5' single character"""

from functions import single_char_xor, get_english_score

with open('input_for_challenge4.txt') as file:
    potential_messages = []
    for hexstring in file.readlines():
        ciphertext = bytes.fromhex(hexstring)
        for k in range(256):
            message = single_char_xor(k, ciphertext)
            score = get_english_score(message)
            data = {
                'ciphertext': ciphertext,
                'message': message, 
                'score': score, 
                'key': k
            }
            potential_messages.append(data)
    best_score = sorted(potential_messages, key= lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print(f'{item.title()}: {best_score[item]}')