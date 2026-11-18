##1
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a>10 and b>10)
print(a==5 or b==5)
print(not(a>b))

##2

age=int(input("Enter your age:"))
if(age>=18):
    print("You are an adult!!")
if(age<18):
    print("You are a minor.")

##3

word = input("Enter a word:")
print("a" in word)
print("Python" not in word)

##4

a,b=10,12
print(a&b,a|b,a^b)
print(a<<2)
print(b>>1)
