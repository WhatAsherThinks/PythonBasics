# this is going to calculate area
# for circles and triangles
print("The area calculator is starting up")
name = raw_input("What's your name? ")
option = raw_input("Enter C for Circle and T for Triangle: ")
if option.lower() == "c":
    radius = float(raw_input("Enter radius: "))
    pi = 3.14159
    area = pi * (radius ** 2)
    print(str(area))
elif option.lower() == "t":
    base = float(raw_input("Enter the Base: "))
    height = float(raw_input("Enter the Height: "))
    area = (base * height) / 2
    print(str(area))
else:
    print("Invalid Shape")
print("program exiting")
