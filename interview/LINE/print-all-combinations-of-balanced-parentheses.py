# Python3 program to
# Print all combinations
# of balanced parentheses


def printParenthesis(n):
    n = 3
    # generate empty lst to hold generated line
    _lst = [""] * 2 * n

    return_lst = []
    generate_parantheses(_lst, 0, n, 0, 0, return_lst)
    return sorted(return_lst)


def generate_parantheses(_lst, position, n,
                         open, close, return_lst):

    if(close == n):
        tmp_str = ''
        for i in _lst:
            tmp_str += i
        return_lst.append(tmp_str)
        return

    if(open > close):
        _lst[position] = ')'
        generate_parantheses(_lst, position + 1, n,
                             open, close + 1, return_lst)
    if(open < n):
        _lst[position] = '('
        generate_parantheses(_lst, position + 1, n,
                             open + 1, close, return_lst)


# Driver Code
print(printParenthesis(n=3))

# This Code is contributed
# by mits.
