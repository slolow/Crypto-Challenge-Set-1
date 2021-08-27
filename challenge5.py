from functions import repeating_key_XOR

plain_text = 'Burning \'em, if you ain\'t quick and nimble\n\
I go crazy when I hear a cymbal'
key = 'ICE'
print('plain text: ' + plain_text)
output_bytes = repeating_key_XOR(plain_text.encode(), key)
cipher_text = output_bytes.hex()
print('cipher_text: ' + cipher_text)
reconstructed_plain_text = repeating_key_XOR(output_bytes, key).decode()
print('reconstructed plain text: \n' + reconstructed_plain_text)

if cipher_text == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343\
c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20\
283165286326302e27282f':
    print('challenge 5 mastered')
