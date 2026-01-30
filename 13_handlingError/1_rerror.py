try:
    x=int(input("enter number:"))
    ans=10/x
except ZeroDivisionError:
    print("Divide by 0 not alllowed here!")
except ValueError:
    print("enter integer type:")
else:
    print(ans)

finally:
    print("run in anyCase")