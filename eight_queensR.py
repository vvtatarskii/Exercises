import time

class CheckerBoard(object):
    def __init__(self,QMap, TMap):
        self.queens = [x.copy() for x in QMap]
        self.threats=[x.copy() for x in TMap]

    def placeQueen(self,i1,i2):
        result = False
        if self.threats[i1][i2] != 0:
            return result

        for x in range(field_size):
            if x!= i1:
                self.threats[x][i2] = 1

        for y in range(field_size):
            if y != i2:
                self.threats[i1][y] = 1

        for x in range(-field_size, field_size):
            xp = i1+x
            yp = i2+x
            if (xp == i1) and (yp == i2):
                pass
            else:
                if (xp >=0) and (xp < field_size) and (yp >=0) and (yp < field_size):
                    self.threats[xp][yp] = 1

        for x in range(-field_size, field_size):
            xp = i1+x
            yp = i2-x
            if (xp == i1) and (yp == i2):
                pass
            else:
                if (xp >=0) and (xp < field_size) and (yp >=0) and (yp < field_size):
                    self.threats[xp][yp] = 1

        result = True
        self.queens[i1][i2] = occupied
        return result


    def printBoard(self,s):
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


def fillBoard(cb):
    # find first empty column
    global cnt
    er = -1
    for x in range(field_size):
        if cb.queens[x].count(occupied) == 0:
            # this column is empty
            er = x
            break
    if er == -1:
        # all columns has a queen
        cnt += 1
        cb.printBoard('final:'+str(cnt))
    else:
        for y in range(field_size):
            if cb.threats[er][y] == 0:
                cbn = CheckerBoard(cb.queens,cb.threats)
                if cbn.placeQueen(er,y):
                    fillBoard(cbn)
                del cbn
    
field_size= 8
cnt = 0
occupied = -1
threats =[[0]*field_size for _ in range(field_size)] 
queens = [[0]*field_size for _ in range(field_size)] 
cb = CheckerBoard(queens,threats)
start = time.time()
fillBoard(cb)
end = time.time()
diff = (end - start)
print('time='+str(diff))
print("Done number of positions: "+str(cnt))


