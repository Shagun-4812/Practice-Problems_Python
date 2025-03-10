def firstLetters():
    n = input("Enter a string: ")
    n=' '+n
    for i in range(len(n)):
        if n[i] == ' ':  
            if i + 1 < len(n):  
                print(n[i + 1])  

def main():
    firstLetters()

if __name__ == "__main__":
    main()

