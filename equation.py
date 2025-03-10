def quadratic_roots():
    a = int(input("Enter Coefficient a: "))
    b = int(input("Enter Coefficient b: "))
    c = int(input("Enter Coefficient c: "))
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        return root1, root2
    elif d == 0:
        root = -b / (2 * a)
        return root
    else:
        print("No real roots")
        return None
def main():
    print(quadratic_roots())
if __name__ == "__main__":  
    main()