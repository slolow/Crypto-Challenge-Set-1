from functions import hamming_distance

def test_hamming_distance():
    distance = hamming_distance('this is a test', 'wokka wokka!!!')
    if distance == 37:
        print('test sucess')
    else:
        print(f'hamming_distance should be 37. Instead {distance} was calculated')

test_hamming_distance()
