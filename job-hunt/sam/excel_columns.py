# excel_columns.py

__author__ = "Riju"

import math
import argparse
from dataclasses import dataclass

ALPHABET = (
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z',
)


@dataclass
class LinkedListNode:
    data: int
    next: None = None


@dataclass
class LinkedList:
    head: LinkedListNode


def main():
    # n = int(input())
    # print(n)

    parser = argparse.ArgumentParser(description='print excel columns upto n')
    parser.add_argument('--n', help='number of columns upto which to print')
    args = parser.parse_args()

    n = int(args.n)

    """
    print(ALPHABET)

    for _ in ALPHABET:
        print(_)
    for position in range(n):
        # print('{0}: {1}'.format(position, ALPHABET[position % len(ALPHABET)]))
        print('{0}: {1}{2}'.format(
          position, 
          ALPHABET[math.floor(position / len(ALPHABET))],
          ALPHABET[position % len(ALPHABET)], 
          )
        )
        # this_str = ""
        # for k in range(math.floor(position / len(ALPHABET)) + 1):
        #     this_str += ALPHABET[position % len(ALPHABET)] 
        # print(position % len(ALPHABET))
        # print(this_str)

        # print(math.floor(position / len(ALPHABET)))
    """

    # rev 2

    for _ in range(1, n + 1):
        # iterate over input integer
        divisor = _
        r_lst = []
        print('math.floor(divisor / len(ALPHABET))')
        print(math.floor(divisor / len(ALPHABET)))
        while math.floor(divisor / len(ALPHABET)) > len(ALPHABET):
            divisor = math.floor(divisor / len(ALPHABET))
            print('divisor')
            print(divisor)
            r_lst.append(divisor % len(ALPHABET))

        r_lst.append(math.floor(divisor / len(ALPHABET)))
        r = divisor % len(ALPHABET)

        print('r_lst')
        print(r_lst)
        # print(r)
        out_str = ''
        for q in r_lst:
            if q == -1:
                out_str += ALPHABET[0]
            else:
                out_str += ALPHABET[q - 1]
        out_str += ALPHABET[r - 1]
        print(out_str)
        # print('=====')


def main1():
    x = 52

    # add integer to a linked list

    lkd_lst = LinkedList(
        head=LinkedListNode(data=x,)
    )

    integer_above_26 = True

    # iterate over the linked list
    # if any integer above 26, replace it with quotient
    # add another node with remainder (incl 0)

    while integer_above_26:
        # import pdb;pdb.set_trace()
        current_item = lkd_lst.head
        if current_item.data < 26:
            break
        _q = current_item.data // 26
        _r = current_item.data % 26
        # print(_q, _r)
        if _q < 1:
            integer_above_26 = False

        current_item.data = _q

        new_item = LinkedListNode(data=_r, next=current_item.next)
        current_item.next = new_item

        while current_item.next is not None:
            current_item = current_item.next

    # print lkd_lst items
    current_item = lkd_lst.head
    while current_item is not None:
        print(current_item.data)
        current_item = current_item.next


    




if __name__ == '__main__':

    # main()
    main1()
