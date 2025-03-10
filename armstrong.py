def cubesum(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 3
        n //= 10
    return sum

def isArmstrong(n):
    return n == cubesum(n)

def main():   
    n = int(input("Enter a number: "))
    if isArmstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")

main()