"""Ques 1: Given Postorder and Inorder traversals, construct the tree.
Examples: 
Input: 
in[]   = {2, 1, 3}
post[] = {2, 3, 1}
Output: Root of below tree
      1
    /   \
   2     3 
Ques 2: Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 
Arr = [1,5,8,9,10,17,17,20]"""
def main(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(len_lst - i):
            print(lst[i], lst[j + i])
            print(i, j + 1)
            print('len: {}'.format(j + 1 - i))


if __name__ == '__main__':
    lst = [1,5,8,9,10,17,17,20]
    main(lst)