print ("moving on")

x=1
print x

if x==1:
	print("if")
else:
	print("else")


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append("string")
mylist.append("foo")

mylist[3] = "bar";

print(mylist)
print(mylist[1])

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]


numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


name = "riju"
age = 25
attrib = "twenty five"

print("%s is %d years old. %s!" % (name, age, attrib))

everyThingList = ["riju", 25, "twenty five"]
print("here is the everythinglist: %s" % everyThingList)

astring = "Hell, World!"
print(astring[1:3])
print(astring[1:10:2])
print(astring[::-1])
print(astring.upper())
print(astring.lower())
print(astring.startswith("He"))
print(astring.endswith("d!"))
print(astring.split(" "))

for x in range(5):
	print(x)

print("\n")
for x in range(3,6):
	print(x)

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


print("--------------------")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

print("---------------------")
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# print(numbers)
for i in numbers:
	if(i % 2):
		print(i)
	if(i==237):
		break

# your code goes here    


import urllib
dir(urllib)





def myfunc(param1):
    print("hello, %s" % param1)

myfunc("miu")