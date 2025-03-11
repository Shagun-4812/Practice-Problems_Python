def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def main():
    n= int(input("Enter a number for which the factorial is to be calculated: "))
    print(fact(n)) 


if __name__ == "__main__":
    main()
