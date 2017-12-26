'''
Merging two dicts in Python 3.5+
'''

dict1 = {'name': 'Ricardo', 'birth year': 1992}
dict2 = {'occupation': 'Developer', 'height': 1.8}

dict3 = {**dict1, **dict2}
