sum =int(input("Enter the sum of the numbers: "))
n = int(input("Enter the number of numbers: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter the number: ")))
for i in range(n):
    for j in range(i+1,n):
        if numbers[i] + numbers[j] <= sum:
            print(numbers[i],numbers[j])
            break
    else:
        continue
    break
else:
    print("No numbers found")   
    