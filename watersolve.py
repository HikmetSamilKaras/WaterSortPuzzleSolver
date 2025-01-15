ans = []

def watersolve(arr, sol):
    global ans 
            
    if ans == []:
        if check(arr):
            ans = sol
    
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and canput(arr[i], arr[j]):
                    arr3 = [row[:] for row in arr]

                    copy1 = arr3[i][:]
                    copy2 = arr3[j][:]

                    put(arr3[i], arr3[j])

                    if arr3[i] != copy2 or arr3[j] != copy1:
                        sol2 = sol[:]
                        sol2.append([i, j])
                        watersolve(arr3, sol2)

def topvalue(arr):
    for val in arr:
        if val != 0:
            return val
    return 0

def topheight(arr):
    a = 0
    for val in arr:
        if val == topvalue(arr):
            a += 1
        elif val != 0:
            break
    return a

def canput(arr1, arr2):
    if not isempty(arr1):
        if topvalue(arr1) == topvalue(arr2) or isempty(arr2):
            return topheight(arr1) <= emptyspace(arr2)
        else:
            return False
    else:
        return False

def put(arr1, arr2):
    value = topvalue(arr1)
    height = topheight(arr1)

    index = firstnonzero(arr1)
    index2 = index + height - 1

    for i in range(index, index2 + 1):
        arr1[i] = 0

    index2 = lastzero(arr2)
    index = index2 + 1 - height

    for i in range(index, index2 + 1):
        arr2[i] = value

def firstnonzero(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return i
    return 0

def lastzero(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            return i
    return 0

def emptyspace(arr):
    a = 0
    for val in arr:
        if val == 0:
            a += 1
        else:
            break
    return a

def isempty(arr):
    return emptyspace(arr) == len(arr)

def check(arr):
    for ar in arr:
        if not all(val == ar[0] for val in ar):
            return False
    return True

def watersolver(arr):
    global ans
    ans = []
    k = []
    watersolve(arr, k)
    return ans