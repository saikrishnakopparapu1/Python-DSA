a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
list1 = [a, b, c]

m = min(a, b, c)
if a < b and a < c:
    print("b and c are greater than a")
elif b < a and b < c:
    print("a and c are greater than b")
elif c < a and c < b:
    print("a and b are greater than c")
else:
    print("All numbers are equal")