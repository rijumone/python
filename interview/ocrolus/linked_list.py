# linked_list.py

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = Node(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def pop_node(self): 
        if self.head == None: 
            return None
        if self.head.next == None: 
            self.head = None
            return None
        second_to_last = self.head 
        while(second_to_last.next.next): 
            second_to_last = second_to_last.next
        second_to_last_data = second_to_last.next.data
        second_to_last.next = None
        return second_to_last_data 

    def delete_node(self, index):
        current_node = self.head
        for i in range(index):
            if i+1 == index:
                try:
                    current_node.next = current_node.next.next
                except AttributeError as e:
                    print('No element at index: {}'.format(index))
                    break
            current_node = current_node.next

        
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
    def __repr__(self):
        return 'Node(' + str(self.data) + ')'


if __name__ == '__main__':
    
    ll_obj = LinkedList()
    for item in ['a', 'b', 'c', 'd']:
        ll_obj.insert_node(item)

    # print(ll_obj.pop_node())
    ll_obj.delete_node(1)
    # ll_obj.delete_node(2)
    ll_obj.delete_node(-1)
    current_node_ll_obj = ll_obj.head
    while current_node_ll_obj is not None:
        print(current_node_ll_obj.data)
        current_node_ll_obj = current_node_ll_obj.next

    