
first_rotor = {
    'a': 'z',
    'b': 'y', 
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a'
    }

def shift_rotor(rotor_state):
    new_position = {}
    keys = list(rotor_state.keys())
    values = list(rotor_state.values())
    
    for i in range(len(keys)):
        new_key = keys[i]
        new_value = values[(i+1) % len(keys)]
        new_position[new_key] = new_value
    
    return new_position



def encode_string(text, first_rotor):
    encoded = ''
    for char in text:
        encoded += first_rotor[char]
        first_rotor = shift_rotor(first_rotor)
    return encoded
        
print(encode_string('aaaaa', first_rotor))