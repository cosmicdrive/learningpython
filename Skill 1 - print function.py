Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Syntax for printing a string of text
print("I love Python now!")
I love Python now!


# Sytax for printing numeric values
print(360)
360
print(32*45)
1440


# Sytax for printing the value of a variable
value = 8+5
print(value)
13



# Multiplication, division, addition, and subtraction
print(3*8/2+5-1)
16.0
>>> 
>>> 
>>> # Exponents
>>> print(4**6)  # Syntax means 4 to the power of 6
4096
>>> 
>>> print(4**2) # To square a number
16
>>> print(4**3) # to cube a number
64
>>> 
>>> print(4**0.5)  # To find the square root of a number
2.0
>>> 
>>>  # To calcuate how many different possible combinations can be
...  
>>> # formed using a set of "x" character with each character in "x" having "y" numbe of possible
>>> # values, you will need to use an exponent for the calculation:
>>> x = 4
>>> y = 26
>>> print(y**x)
456976
>>> 456976
456976
>>> 
>>> # Assingment of values to the variables:
>>> year = 10
>>> weeks_in_a_year = 52
>>> # This variable is assigned an arithmetic calculation:
>>> weeks_in_a_decade = years * weeks_in_a_year
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    weeks_in_a_decade = years * weeks_in_a_year
NameError: name 'years' is not defined. Did you mean: 'year'?
>>> NameError: name 'years' is not defined. Did you mean: 'year'?year
SyntaxError: invalid syntax
>>> 
>>> 
>>> # Assignment of values to the variables:
>>> years = 10
>>> weeks_in_a_year = 52
>>> # This variable is assigned an arithmetic calculation:
>>> weeks_in_a_decade = years * weeks_in_a_year
>>> # Prints the calculation stored in the "weeks_in_a_decade variable:
>>> print(weeks_in_a_decade)
520
