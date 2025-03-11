def TowerOfHanoi(n, source, final, middle):
    if n == 0:
        return
    TowerOfHanoi(n-1, source, middle, final)
    print("Move disk", n, "from rod", source, "to rod", final)
    TowerOfHanoi(n-1, middle, final, source)



N = 5
TowerOfHanoi(N, 'A', 'C', 'B')


