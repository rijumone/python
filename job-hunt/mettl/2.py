"""
generate caesar cipher
"""

a = [
'a','b','c','d','e',
'f','g','h','i','j',
'k','l','m','n','o',
'p','q','r','s','t',
'u','v','w','x','y',
'z'
]

# print(a)

str = 'xzczoiyoqbnjkb'

out_str = ''
for s in str:
	for i,_ in enumerate(a):
		if s == _:
			# calc offset
			offset = (i + 3) if i < (len(a) - 3) else 3 - (len(a) - i)
			out_str += a[offset]

print(out_str)