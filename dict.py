
my_dict = {1: 20, 3: 40, 4: 50, 5: 60}

try:
    for i in range(1, 6):
        print(my_dict[i])   
except KeyError:
    print("Key not found")
else:
    print("No error")
finally:
    print(my_dict)




