def fibonacci_tabulation(n, table):
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]
t={0:0,1:1}
print(fibonacci_tabulation(10,t))