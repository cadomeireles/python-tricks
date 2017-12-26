'''
Check different flags at once
'''
a = False
b = []
c = None
d = {}
e = 'content'

any((a, b, c, d, e))  # any is truly
all((a, b, c, d, e))  # all is truly
