class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def inc(self,e,k):
        for x in range(0,e):
            self.items[x] = self.items[x] + k



# N = int(raw_input())
commandList = []

# for x in range(0,N):
#     commandList.append(raw_input())    

commandList = ["push 4","pop","push 3","push 5","push 2","inc 3 1","pop","push 1","inc 2 2","push 4","pop","pop"]


stack = Stack()

for command in commandList:
    temp = command.split(" ")
    # print stack.size()    
    # print stack.isEmpty()
    if temp[0] == "push":
        stack.push(int(temp[1]))
    elif temp[0] == "pop" and not stack.isEmpty():
        stack.pop()
    else :
        stack.inc(int(temp[1]),int(temp[2]))
     
    if stack.isEmpty():
        print "EMPTY"
    else:
        print stack.peek()