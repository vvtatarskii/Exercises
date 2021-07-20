import time

class ChessBoard(object):
    def __init__(self,KMap, BMap):
        self.knights = [x.copy() for x in KMap]
        
    def printBoard(self,s):
        # s - message/
        rows = ['1','2','3','4','5','6','7','8']
        print(s)
        print('    -- -- -- -- -- -- -- --')
        for x in range(field_size):
            print(rows[7-x],"|",end=" ")
            for y in range(field_size):
                k = self.knights[7-x][y]
                if k != 0:
                    print("%2i" % k, end=" ")
                else:
                    print("  ",end=" ")
            print('|')
        print('    -- -- -- -- -- -- -- --')
        print('    A B C D E F G H')

field_size = 8
KMap = [[0]*field_size for _ in range(field_size)]
KMap[0][0] = 1
KMap[1][2] =2
BMap = [[0]*field_size for _ in range(field_size)] 
cb = ChessBoard(KMap,BMap)
cb.printBoard('')
print("Done")
