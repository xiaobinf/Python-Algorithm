def MATRIX_CHAIN_ORDER(p):
    n = len(p)
    # s,m=matrix 7*7 init [0..0]
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[0 for j in range(n)] for i in range(n)]
    for l in range(2, n):           #l is the chain length   Mi与Mj的距离
        for i in range(1, n-l+1):
            j = i + l - 1
            # 1e9 = 1000000000
            m[i][j] = 1e9
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    PRINT_OPTIMAL_PARENS(s, 1, n-1)
    return m


def PRINT_OPTIMAL_PARENS(s, i, j):
    if i == j:
        print('A', end = '')
        print(i, end = '')
    else:
        print('(', end = '')
        PRINT_OPTIMAL_PARENS(s, i, s[i][j])
        PRINT_OPTIMAL_PARENS(s, s[i][j]+1, j)
        print(')', end = '')


if __name__ == "__main__":
    A = [30, 35, 15, 5, 10, 20,25]
    m = MATRIX_CHAIN_ORDER(A)
    print('\n','共计需要',m[1][6],'次相乘')
