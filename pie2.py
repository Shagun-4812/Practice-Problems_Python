def seriessum():
    n = int(input("Enter the number of terms: "))
    sum = 0
    c=1
    for i in range(1, n+1):
        if i%2==0:
            sum -= 1/c
        else:   
            sum += 1/c

        c+=2
    return sum  
    print("The sum of the series is", sum)

def main():
        print(seriessum())
        pie= 4*seriessum()
        print("The value of pie is", pie)

if __name__ == "__main__":  
        main()
