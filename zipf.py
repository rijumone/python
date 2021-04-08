def str_key(_str):
    return ' ---\n'+f'| {_str} |\n'+' ---'

def print_banner():
    # print(str_key('Q'), str_key('W'), str_key('E'))
    print(' --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ', ' --- ', ' --- ', ' --- ', )
    print('| Q |', '| W |', '| E |', '| R |',
          '| T |', '| Y |', '| U |', '| I |', '| O |', '| P |', )
    print(' --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ', ' --- ', ' --- ', ' --- ', )

    print('   --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ', ' --- ', ' --- ',  )
    print('  | A |', '| S |', '| D |', '| F |',
          '| G |', '| H |', '| J |', '| K |', '| L |',)
    print('   --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ', ' --- ', ' --- ',)
    
    print('     --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ',)
    print('    | Z |', '| X |', '| C |', '| V |', '| B |', '| N |', '| M |',)
    print('     --- ', ' --- ', ' --- ', ' --- ',
          ' --- ', ' --- ', ' --- ',)


    print('       -------------------------------------------- ',)
    print('      |                                            | ')
    print('       -------------------------------------------- ',)

    

def main():
    print_banner()

if __name__ == '__main__':
    main()
