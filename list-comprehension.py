old_list = ['foo','bar']

print(old_list)

new_list = [k.upper() for k in old_list if k == "foo"]

print(new_list)

# anotherList = [5,6,2,9,7,2]

# print(anotherList[4])
# print(anotherList[4:])
# print(anotherList[6])
# print(anotherList[6:])


l = []

# for letter in "word":
# 	print letter

l = [letter for letter in "word"]	
print l

c = [0,1.5,2,2.3]

f = [(temp * (9/5) + 32 ) for temp in c]