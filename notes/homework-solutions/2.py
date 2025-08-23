##1:
# Declare the variables as a and b
a=5
b=7
# Printing the results of each operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

##2:
# With using a third variable:
print("With using a third variable:")
a,b=3,6
print("Before Swapping a and b: \na= ",a,"\nb= ",b)
temp=a
a=b
b=temp
print("After swapping with a third variable(temp): \na= ",a,"\nb= ",b)

#Without using a third variable
print("Without using a third variable:")

c,d=4,5
print("Before swapping:\nx= ",c,"\nd= ",d)
c,d=d,c
print("After swapping without a third variable: \nx= ",c,"\nd= ",d)