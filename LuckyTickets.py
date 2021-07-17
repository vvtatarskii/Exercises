import time
rpt = 200
print("------------------------ version 1 ------------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                s1 = i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        for i6 in range(10):
                            if s1 == i4+i5+i6:
                                num += 1
end = time.time()

print(num)
print((end-start)/rpt)
print("------------------------ version 2 ------------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                s1 = i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        for i6 in range(10):
                            if s1 == i4+i5+i6:
                                num += 1
                                break
end = time.time()

print(num)
print((end-start)/rpt)
print("------------------------ version 2a ------------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            s1_2 = i1 + i2
            for i3 in range(10):
                s1 = s1_2 + i3 # i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        for i6 in range(10):
                            if s1 == i4+i5+i6:
                                num += 1
                                break
end = time.time()

print(num)
print((end-start)/rpt)
print("------------------------ version 2b ------------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            s1_2 = i1 + i2
            for i3 in range(10):
                s1 = s1_2 + i3 # i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        s2_2 = i4 + i5
                        for i6 in range(10):
                            if s1 == s2_2 + i6: #i4+i5+i6:
                                num += 1
                                break
end = time.time()

print(num)
print((end-start)/rpt)
print("----------------------- version 3 ----------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                s1 = i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        diff= s1-(i4+i5)
                        if (diff >=0) and (diff <10):
                            num+=1
end = time.time()
print(num)
print((end-start)/rpt)

print("----------------------- version 3a ----------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            s1_2 = i1 + i2
            for i3 in range(10):
                s1 = s1_2 + i3 # i1+i2+i3
                for i4 in range(10):
                    for i5 in range(10):
                        diff= s1-(i4+i5)
                        if (diff >=0) and (diff <10):
                            num+=1
end = time.time()
print(num)
print((end-start)/rpt)
print("---------------------- version 4 ----------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                s1 = i1+i2+i3
                for i4 in range(10):
                    diff = s1 - i4
                    if (diff >= 0) and (diff <19):
                        for i5 in range(10):
                            diff= s1-(i4+i5)
                            if (diff >=0) and (diff <10):
                                num+=1
end = time.time()
print(num)
print((end-start)/rpt)
print("---------------------- version 4a ----------------------------")
start = time.time()
for count in range(rpt):
    num = 0
    for i1 in range(10):
        for i2 in range(10):
            s1_2 = i1 +i2
            for i3 in range(10):
                s1 = s1_2 + i3 # i1+i2+i3
                for i4 in range(10):
                    diff = s1 - i4
                    if (diff >= 0) and (diff <19):
                        for i5 in range(10):
                            diff= s1-(i4+i5)
                            if (diff >=0) and (diff <10):
                                num+=1
end = time.time()
print(num)
print((end-start)/rpt)
