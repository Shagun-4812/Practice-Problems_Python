def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    number = int(input("Enter a number: "))
    
    if is_prime(number):
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is Not a Prime Number")

if __name__ == "__main__":
    main()
