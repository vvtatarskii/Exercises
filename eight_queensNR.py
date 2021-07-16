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

field_size= 8
threats =[[0]*field_size for _ in range(field_size)] # [[0]*field_size]*field_size
queens = [[0]*field_size for _ in range(field_size)] # [[0]*field_size]*field_size
occupied = -1
start = time.time()
cnt = 0
for q1 in range(field_size):
    cb1=CheckerBoard(queens,threats)
    if cb1.placeQueen(0,q1):
        for q2 in range(field_size):
            cb2 = CheckerBoard(cb1.queens,cb1.threats)
            if cb2.placeQueen(1,q2):
                for q3 in range(field_size):
                    cb3 = CheckerBoard(cb2.queens,cb2.threats)
                    if cb3.placeQueen(2,q3):
                        for q4 in range(field_size):
                            cb4 = CheckerBoard(cb3.queens,cb3.threats)
                            if cb4.placeQueen(3,q4):
                                for q5 in range(field_size):
                                    cb5 = CheckerBoard(cb4.queens,cb4.threats)
                                    if cb5.placeQueen(4,q5):
                                        for q6 in range(field_size):
                                            cb6 = CheckerBoard(cb5.queens,cb5.threats)
                                            if cb6.placeQueen(5,q6):
                                                for q7 in range(field_size):
                                                    cb7 = CheckerBoard(cb6.queens,cb6.threats)
                                                    if cb7.placeQueen(6,q7):
                                                        for q8 in range(field_size):
                                                            cb8 = CheckerBoard(cb7.queens,cb7.threats)
                                                            if cb8.placeQueen(7,q8):
                                                                cnt += 1
                                                                cb8.printBoard("Success:"+str(cnt))
                                                            del cb8
                                                    del cb7
                                            del cb6
                                    del cb5
                            del cb4
                    del cb3
            del cb2
    del cb1
end = time.time()
diff = (end - start)
print('time='+str(diff))
print("Done number of positions: "+str(cnt))


