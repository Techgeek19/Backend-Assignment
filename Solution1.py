def taskPrint(K, matrix):
    while K > 0:
        countEmpty = 0
        I, J = map(int, (input().split())) 
        for i in range(N):  #No local N, the value from the global N will be used
            matrix[i][J] = 'X'
        for j in range(N):
            matrix[I][j] = 'X'
        for i in range(N): 
            for j in range(N): 
                if(matrix[i][j] == ' '):
                    countEmpty = countEmpty + 1
        print(countEmpty)
        K -= 1
        if K == 0:
            break
    

if __name__ == "__main__":                    
    N, K = map(int, (input().split()))  #N is No. of Rows & Column of Matrix  # K is total number of task
    matrix = [ [ " " for i in range(N) ] for j in range(N) ]
    taskPrint(K, matrix) 