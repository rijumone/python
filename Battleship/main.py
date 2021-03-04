from pprint import pprint

LETTERS = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    ]

HORIZONTAL = 'h'
VERTICAL = 'v'

class Ship:
    width = 1

class AircraftCarrier(Ship):
    length = 5

class Battleship(Ship):
    length = 4

class Cruiser(Ship):
    length = 3

class Submarine(Ship):
    length = 3

class Destroyer(Ship):
    length = 2



class Board:
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        # self.board_raw = [['.' for _ in range(self.grid_size)]] * self.grid_size
        self.board_raw = [['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.']]

        pprint(self.board_raw)
    
    def __str__(self):
        _str = '    '
        for i in range(self.grid_size):
            _str += f'{LETTERS[i]} '
        _str += '\n'

        for row_idx in range(self.grid_size):
            _str += f'  {row_idx} '
            for col_idx in range(self.grid_size):
                _str += f'{self.board_raw[row_idx][col_idx]} '
            _str += '\n'

        return _str

    def place_ship(self, start, end, type):
        
        placement = None
        if start[0] == end[0]:
            placement = VERTICAL
        elif start[1] == end[1]:
            placement = HORIZONTAL
        else:
            raise ValueError('Can not place ships diagonally.')

        if isinstance(type, AircraftCarrier):
            symbol = 'A'
        elif isinstance(type, Battleship):
            symbol = 'B'
        
        target_idx = [_ for _ in range(
            len(LETTERS)) if LETTERS[_] == start[0]][0]

        if placement == VERTICAL:
            for row_idx in range(len(self.board_raw)):
                if row_idx < start[1] or row_idx > end[1]:
                    continue
                for col_idx in range(len(self.board_raw[row_idx])):    
                    if col_idx != target_idx:
                        continue
                    if self.board_raw[row_idx][col_idx] != '.':
                        raise ValueError('Space already occupied by another ship')
                    self.board_raw[row_idx][col_idx] = symbol
                    break
        else:
            import pdb;pdb.set_trace()
            for row_idx in range(len(self.board_raw)):
                if row_idx != target_idx:
                    continue
                for col_idx in range(len(self.board_raw[row_idx])):
                    if row_idx < start[1] or row_idx > end[1]:
                        continue
                    if self.board_raw[row_idx][col_idx] != '.':
                        raise ValueError(
                            'Space already occupied by another ship')
                    self.board_raw[row_idx][col_idx] = symbol
                    break




        
        # for row_idx in range(self.grid_size):







def main():
    board = Board(
        grid_size=8
    )
    print(board)
    
    board.place_ship(
        start=('B', 2),
        end=('B', 6),
        type=AircraftCarrier()
    )
    
    
    board.place_ship(
        start=('D', 2),
        end=('F', 2),
        type=Battleship()
    )

    print(board)

if __name__ == '__main__':
    main()
