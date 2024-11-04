# error handling

x = input("Enter First number: ")
y = input("Enter Second number: ")
z = input("Enter Third number: ")

# converting to integers
try:
   x_num = int(x)
   y_num = int(y)
   z_num = int(z)
   print( x_num + y_num + z_num)
except:
    print("Please enter valid numbers")

