def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    elif n == 2:
        print("Move disk 1 from rod", source, "to rod", auxiliary)
        print("Move disk 2 from rod", source, "to rod", destination)
        print("Move disk 1 from rod", auxiliary, "to rod", destination)
        return
    else :
        hanoi(n-1, source, auxiliary, destination)
        print("Move disk", n, "from rod", source, "to rod", destination)
        hanoi(n-1, auxiliary, destination, source)
def main():
    n = int(input("Enter the number of disks: "))
    hanoi(n, 'A', 'B', 'C')
if __name__ == "__main__":
    main()