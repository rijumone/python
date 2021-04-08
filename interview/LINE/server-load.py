
t = 15
arr = ["0 A created",
       "1 B created",
       "10 A running",
       "12 B waiting",
       "13 B running",
       "14 A waiting",
       "17 B terminated",
       "18 A terminated"
       ]

# t = 15
# arr = [
#     '0 A created',
#     '1 B created',
#     '2 C created',
#     '3 D created',
#     '10 A running',
#     '11 A waiting',
#     '12 B waiting',
#     '13 B running',
#     '14 C running',
#     '17 B terminated',
#     '18 A terminated',
# ]


checker = {}


def print_result(checker):
    if len(checker) == 1:
        for name in checker.keys():
            print(name)
    else:
        print(-1)


def add_process(name, checker):
    if name not in checker.keys():
        checker[name] = 'running'


def remove_process(name, checker):
    if name in checker.keys():
        del(checker[name])


add_cond = ["running", "created"]
remove_cond = ["terminated", "waiting"]
for val in arr:
    tmp = val.split(" ")
    if t < int(tmp[0]):
        break
    if tmp[2] in add_cond:
        add_process(tmp[1], checker)
    else:
        remove_process(tmp[1], checker)
print_result(checker)
