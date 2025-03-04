def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numbers = []
    for _ in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)
    
    total_sum = sum(numbers)
    print(f"The sum of the numbers is: {total_sum}")
    
    if is_prime(total_sum):
        print("The sum is a prime number.")
    else:
        print("The sum is not a prime number.")

if __name__ == "__main__":
    main()