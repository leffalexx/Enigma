import json

filenames = ['first_rotor.json', 'second_rotor.json']
rotors = dict(map(lambda filename: (filename.split('.')[0], json.load(open(filename))), filenames))

first_rotor = rotors['first_rotor']
second_rotor = rotors['second_rotor']


def shift_rotor(rotor_state):
    new_position = {}
    keys = list(rotor_state.keys())
    values = list(rotor_state.values())
    
    for i in range(len(keys)):
        new_key = keys[i]
        new_value = values[(i+1) % len(keys)]
        new_position[new_key] = new_value
    
    return new_position



def encode_string(text, first_rotor, second_rotor):
    encoded = ''
    count = 0

    for char in text:
        first_rotor_output = first_rotor[char]
        encoded += second_rotor[first_rotor_output]
        first_rotor = shift_rotor(first_rotor)
        count +=1
        if count % 27 == 0:
            shift_rotor(second_rotor)
    return encoded
        
print(encode_string('artamun is a nice dog and artamun feasts on cats', first_rotor, second_rotor))

#print(rotors)