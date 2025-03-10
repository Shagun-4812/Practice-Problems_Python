def prodDigits():
    n = int(input("Enter a number: "))
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def main():
    print(prodDigits())

if __name__ == "__main__":
    main()