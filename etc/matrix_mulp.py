
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    
    for l in range(2, n+1):
        for i in range(n-l+2):
            j = i + l - 1
            m[i-1][j-1] = float('inf')
            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k
    return m, s

def solution(matrix_sizes):
    answer = 0
    dp = [[0 for j in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]
    #print(dp)
    #print(len(dp))
    de = [matrix_sizes[0][0]] + [matrix_sizes[i][1] for i in range(len(matrix_sizes))]
    #print(de)
    m, s = matrix_chain_order(de)
    answer = m[0][-1]
    return answer

solution([[5,3],[3,10],[10,6]])