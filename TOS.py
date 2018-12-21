import numpy as np

# init table----------------------------------------------------
h = 6
w = 5
table = [[0 for x in range(w)] for y in range(h)] 
tmpTable = [[0 for x in range(w)] for y in range(h)]
# rand value
for i in range(0,h):
    for j in range(0,w):
        if(j==2):
            table[i][j] = 1
        else:
            table[i][j] = np.random.randint(0,6)
table[0][0]=2
table[0][1]=2
table[0][3]=2
table[0][4]=2
print('org table')
for i in range(0,h):
    print(table[i])

while(1):
    # delete row--------------------------------------
    h = len(table)     # update h
    w = len(table[0])  # update w
    
    tmpTable = [[0 for x in range(w)] for y in range(h)] #update tmpTable
    for row in range(0,h):
        tmpQ = []
        for col in range(0,w-1):
            tmp = table[row][col]
            tmpQ.append(col)
            testh = len(table)     # test h
            testw = len(table[0])  # test w
            print('h,w',testh,testw)
            print('row,col+1',row,col+1)
            if table[row][col+1] == tmp:
                tmpQ.append(col+1)
            else:
                tmpQ = []
            if(len(tmpQ) >= 3):
                for idx in tmpQ:
                    tmpTable[row][idx] = -1
    
    # delete col--------------------------------------
    for col in range(0,w):
        tmpQ = []
        for row in range(0,h-1):
            tmp = table[row][col]
            tmpQ.append(row)
            if table[row+1][col] == tmp:
                tmpQ.append(row+1)
            else:
                tmpQ = []
            if(len(tmpQ) >= 3):
                for idx in tmpQ:
                    tmpTable[idx][col] = -1
    
    print('delete done')
    print('tmpTable')
    for row in range(0,h):
        print(tmpTable[row])
    
    # update new table
    newT = []
    flag = 0
    for row in range(0,h):
        newL = []
        for col in range(0,w):
            if tmpTable[row][col] == -1:
                flag = 1
                continue
            else:
                newL.append(table[row][col])
        newT.append(newL)
    if flag:# update new table 
        table = newT
    
    print('table')
    for row in range(0,h):
        print(table[row])
    
    if flag:
        print('loop')
        print('---------------------------')
        continue
    else:
        break
        
print('====================================')
print('done')
print('====================================')