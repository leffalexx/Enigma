
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
    'z': 'a',
    ' ': ' '
    }
second_rotor = {
  'a': 'm',
  'b': 'g',
  'c': 'l',
  'd': 'p',
  'e': 'o', 
  'f': 'j',
  'g': 'u',
  'h': 'q',
  'i': 'k',
  'j': 'c',
  'k': 'n',
  'l': 'y',
  'm': 'z',
  'n': 'h',
  'o': 'w',
  'p': 'f',
  'q': 'a',
  'r': 'x',
  's': 'e',
  't': 'd',
  'u': 'r',
  'v': 'b',
  'w': 'i',
  'x': 't',
  'y': 'v',
  'z': 's',
  ' ': ' '
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
        
print(encode_string('hello world and all the loveley people out there this is a prototype enigmna code with just two rotors and no reflector or plugpanel', first_rotor, second_rotor))