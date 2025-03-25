x=0
y=1

try:
    y/x
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print("No error")
finally:
    print("Finally block")
    
