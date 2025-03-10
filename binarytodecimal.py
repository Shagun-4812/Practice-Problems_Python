def binary():
    n = input("Enter a number in binary: ")
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** (len(n) - i - 1)
    return decimal      
def main():
    print(binary())     
if __name__ == "__main__":
    main()  
    
    