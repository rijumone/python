# excel_columns.py

__author__ = "Riju"

import math
import argparse

if __name__ == '__main__':

    # n = int(input())
    # print(n)

    parser = argparse.ArgumentParser(description='print excel columns upto n')
    parser.add_argument('--n', help='number of columns upto which to print')
    args = parser.parse_args()
    
    n = int(args.n)

    alphabet_tpl = (
        'A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z',
        )
    """
    print(alphabet_tpl)

    for _ in alphabet_tpl:
        print(_)
    for position in range(n):
        # print('{0}: {1}'.format(position, alphabet_tpl[position % len(alphabet_tpl)]))
        print('{0}: {1}{2}'.format(
          position, 
          alphabet_tpl[math.floor(position / len(alphabet_tpl))],
          alphabet_tpl[position % len(alphabet_tpl)], 
          )
        )
        # this_str = ""
        # for k in range(math.floor(position / len(alphabet_tpl)) + 1):
        #     this_str += alphabet_tpl[position % len(alphabet_tpl)] 
        # print(position % len(alphabet_tpl))
        # print(this_str)

        # print(math.floor(position / len(alphabet_tpl)))
    """

    # rev 2

    for _ in range(1, n + 1):
        # iterate over input integer
        divisor = _
        r_lst = []
        print('math.floor(divisor / len(alphabet_tpl))')
        print(math.floor(divisor / len(alphabet_tpl)))
        while math.floor(divisor / len(alphabet_tpl)) > len(alphabet_tpl):
            divisor = math.floor(divisor / len(alphabet_tpl))
            print('divisor')
            print(divisor)
            r_lst.append(divisor % len(alphabet_tpl))

        r_lst.append(math.floor(divisor / len(alphabet_tpl)))
        r = divisor % len(alphabet_tpl)
        
        print('r_lst')
        print(r_lst)
        # print(r)
        out_str = ''
        for q in r_lst:
            if q == -1:
                out_str += alphabet_tpl[0]
            else:
                out_str += alphabet_tpl[q - 1]
        out_str += alphabet_tpl[r - 1]
        print(out_str)
        # print('=====')