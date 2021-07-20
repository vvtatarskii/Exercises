# Attention: Kinght's Tour is not neccessary circle.
# For now - it looks tat I can start from some point (e.g. A1)
# and then if search will fail, choose free point with entry, but noe exit,
# and continue.
# Or, another possiblity - choose another charting point. In Wikipedia in the example
# they starting at the point E8.

import time

class ChessBoard(object):
    def __init__(self,KMap, BMap):
        self.knights = [x.copy() for x in KMap]
        
    def IsFreeCell(self,x,y):
        return self.knights[y][x] == 0
        
    def KnightJump(self,x,y,i):
        if   i == 1:
            xn = x + 2
            yn = y + 1
        elif i == 2:
            xn = x + 2
            yn = y - 1
        elif i == 3:
            xn = x + 1
            yn = y - 2
        elif i == 4:
            xn = x - 1
            yn = y - 2
        elif i == 5:
            xn = x - 2
            yn = y - 1            
        elif i == 6:
            xn = x - 2
            yn = y + 1
        elif i == 7:
            xn = x - 1
            yn = y + 2
        elif i == 8:
            xn = x + 1
            yn = y + 2
        else:
           print("Error in KnightJump. i = ",i)
        
        
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
print(cb.IsFreeCell(2,1))
print(cb.IsFreeCell(0,0))
print(cb.IsFreeCell(2,2))
print("Done")
