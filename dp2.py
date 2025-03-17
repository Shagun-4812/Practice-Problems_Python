def fibonacci_topDown(n, table):
    if n not in table:
        table[n] = fibonacci_topDown(n - 1, table) + fibonacci_topDown(n - 2, table)
    return table[n] 
t={0:0,1:1}
print(fibonacci_topDown(10,t))