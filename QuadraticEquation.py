a = int(input("Given a: "))
b = int(input("Given b: "))
c = int(input("Given c: "))

root1 = 0
root2 = 0
d = (b**2) - 4*a*c
root1 = (-b + (d**(0.5)))/2*a
root1 = (-b - (d**(0.5)))/2*a
print(f"Roots:,({root1},{root2})")
