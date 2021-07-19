import time

class ChessBoard(object):
    def __init__(self,QMap, TMap):
        self.knights = [x.copy() for x in QMap]
        
    def printBoard(self,s):
        # s - message/
        rows = ['A','B','C','D','E','F','G','H']
        print(s)
        print('  ------------------')
        for x in range(field_size):
            print(rows[7-x],"|",end=" ")
            for y in range(field_size):
                if self.queens[x][y] == occupied:
                    print("Q", end=" ")
                else:
                    print(".",end=" ")
            print('|')
        print('  ------------------')
        print('    1 2 3 4 5 6 7 8')

field_size = 0
