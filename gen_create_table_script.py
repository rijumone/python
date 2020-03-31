""" just generate these pesky csv_sequences """
__author__ = "riju"

query_list = []

# foo = input()
while True:
    i = input()
    if not i:
        break
    # print("Your input:", i)
    query_list.append(i)

# print(query_list)
j = 0
for line in query_list:
    print('"{0}" {1}'.format(line.split(" ")[0], " ".join(line.split(" ")[1:])))
    j += 1
