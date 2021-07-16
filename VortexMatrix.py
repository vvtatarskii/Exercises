def VortexPrint(x0,y0,len):
    if len < 1:
        pass
    else:
        #print top row
        for x in range(0,len):
            print(mat[y0][x0+x])

        #print right column
        for y in range(1,len):
            print(mat[y0+y][x0+len-1])

        #print bottom row
        for x in range(len-2,-1,-1):
            print(mat[y0+len-1][x0+x])

        #print left column
        for y in range(len-2,0,-1):
            print(mat[y0+y][x0])

        VortexPrint(x0+1,y0+1,len-2)

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

VortexPrint(0,0,4)
print('done')
