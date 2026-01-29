x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))
z = int(input("Enter third number (z): "))
print("Before swapping: x =", x, ", y =", y, ", z =", z)

t = x
x = y
w = z
y = w
z = t
print("After swapping: x =", x, ", y =", y, ", z =", z)