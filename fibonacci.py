def fibonacci_series(n):
    a, b= 0,1
    for  i in range(n):
        print(a, end=" ")
        a, b= b, a+b    

def main():
    n= int(input("Enter the number of terms in the fibonacci series: "))
    fibonacci_series(n)

if __name__ == "__main__":
    main()