a=[0,1,2,3]
try:
    #a=10/0
    #print(y)
    print(a[5])
except IndexError:
    print("Exception occured due to index out of bound")
except ZeroDivisionError:
    print("Exception occured due to division by zero")
except NameError:
    print("Exception occured due to undefined variable")
except:
    print("Exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")
