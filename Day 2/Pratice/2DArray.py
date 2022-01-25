#hourglasssum problem from Hacker rank

def hourglassSum(arr):
    m = -63
    for i in range(0,4):
        for j in range(0,4):
            s = (arr[i][j])+(arr[i][j+1])+(arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j])+(arr[i+2][j+1])+(arr[i+2][j+2])
            if s > m:
                m = s
            
    
    return m
matrix  = []
for i in range(6):          # A for loop for row entries

    arr =[]

    for j in range(6):      # A for loop for column entries

        arr.append(int(input()))

        matrix.append(arr)

print(hourglassSum(matrix))