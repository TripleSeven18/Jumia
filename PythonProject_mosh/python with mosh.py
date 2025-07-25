from operator import is_not, truediv

print(10 + 3)
print(10**3) #exponent/power (**)

x = 10
x = x + 3 #same as below
print(x)

x = 10
x += 3
print(x) #augmented assignment operator/enhancement of the assignment operator

x = 10
x -= 3 #subtracting 3 from x
print(x)

x = 10 + 3 * 2 ** 2 #operator precedence
print(x)

x = (2 +3) * 10 - 3 #operator precedence
print(x)

x = 2.9
print(round(x)) #round of

x = 2.9
print(abs(-2.9)) #abs-absolute function_returns the positive function

import math

print(math.ceil(2.5))

print(math.floor(2.5))

#if statement
is_hot = False #can change the boolean(True/False)
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear heavy clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

#logical operators Nb: wit "and" operator, both conditions_be True, with "or" operator, at least one condition must be true
has_high_income = False
has_good_credit = True

if has_good_credit and has_high_income:
    print("Eligible for a loan")

else:
    print("Not eligible for a loan")

has_high_income = True
has_good_credit = False

if has_good_credit or has_high_income:
    print("Eligible for a loan")

else:
    print("Not eligible for a loan")

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")

