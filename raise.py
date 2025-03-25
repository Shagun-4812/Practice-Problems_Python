x=0
try:
    if x==0:
        raise ZeroDivisionError("Anything")
except ZeroDivisionError as err:
    print(err)