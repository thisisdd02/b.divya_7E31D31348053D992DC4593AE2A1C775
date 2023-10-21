"""
Challenge 2:check

Write a program that determines whether a year entered by the user is a leap 
year or not using ifelif-else statements.
"""

def isleap(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return True
	else:
		return False
year = int(input("Enter a year to find leapyear or not: "))

if(isleap(year)):
	print(year,"is a leap year")
else:
	print(year,"is not a leap year")
