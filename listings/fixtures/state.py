codes = open('codes.txt', 'r').readlines()
n_codes = [code[1:3] for code in codes]

names = open('names.txt', 'r').readlines()
n_names = [name[1:-2] for name in names]

states = []
for i in range(51):
    state = {
        'model': 'listings.state',
        'pk': i + 1,
        'fields': {
            'code': n_codes[i],
            'name': n_names[i]
        }
    }
    states.append(state)
    
import json

with open('states.json', 'w') as output_file:
    json.dump(states, output_file)
