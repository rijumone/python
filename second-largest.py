thisIsList = [8,33,5,45,1,66,224]

numbers = thisIsList

if numbers[0]>numbers[1]:
	m, m2 = numbers[0], numbers[1]
else:
    m, m2 = numbers[1], numbers[0]

for x in numbers[2:]:
    if x>m2:
       if x>m:
          m2, m = m, x
       else:
          m2 = x


print m2