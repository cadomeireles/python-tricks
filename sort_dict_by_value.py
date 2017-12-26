'''
Sort a dict by value
'''

d = {'a': 79, 'b': 32, 'c': 22, 'd': 46, 'e': 2}

sorted(d.items(), key=lambda x: x[1])
