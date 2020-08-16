def printTask(K, matrix):
    res = '' 
    row = []     # X placed row
    col = []     #X placed column
    while K > 0:
        i, j = map(int, (input().split()))
        if i not in row:
            row.append(i)
            matrix = matrix - (N - len(col))
        if j not in col:
            col.append(j)
            matrix = matrix - (N - len(row))
        res = res + f'{matrix}'+ ' '    
        K -= 1
        if K == 0:
            break
    print(res)

if __name__ == "__main__":
    N, K = map(int, (input().split()))  #N is No. of Rows & Column of Matrix  # K is total number of task
    matrix = N * N  
    printTask(K, matrix)