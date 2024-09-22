print("Love") #output

boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name:  ")
girl_age = int(input("Girl Age: "))

# single line comment
age_diff = abs(boy_age - girl_age)

'''
this
is a multline
comment
'''
print(boy_name + " loves " + girl_name + ". Age Difference is " + str(age_diff))

print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")