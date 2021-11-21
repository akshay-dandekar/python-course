
import math


###### Formatted strings

var0 = math.pi
var1 = 212.45 #math.pi * 2 


print("{1:07.2f},{0:d}".format( int(var0), var1))

age_years = 29
age_months = 10

print("My age is {} years {} months".format(age_years, age_months))

print("My age is " + str(age_years) + " years " + str(age_months) + " months")

print(f'My age is {age_years} years {age_months} months')