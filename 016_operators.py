# Video alternative: https://vimeo.com/954334235/902b0b036d#t=606

# So far you've seen very simple computations.
# I'm going to show you how to perform more advanced ones.
# Before I do, let's break down `add_one` a bit further`.
# I'm going to give you some more terminology.

def add_one(num):
  return num + 1

# You may need to widen the panel or zoom out to see the table:

# | Code           | What is it?                                        |
# | -------------- | -------------------------------------------------- |
# | def            | `def` is a keyword that defines a new function     |
# | add_one        | `add_one` is the function name                     |
# | (num)          | `(num)` is the parameter list                      |
# | num            | `num` is a parameter                               |
# | :              | The `:` symbol indicates the body should start now |
# | return num + 1 | `return num + 1` is a statement                    |
# | num + 1        | `num + 1` is an expression                         |
# | num            | `num` here is a variable                           |
# | +              | `+` is an operator                                 |
# | 1              | `1` is a literal number                            |

# Don't worry about remembering all of that table, but pay
# attention now to three items: operators, statements, and
# expressions. We're going to look at all three next.

# First we'll look at operators.

# @TASK: To be a great programmer you will have to become a
# great researcher. Let's get started:
#
# 1. Search the web for "Python operators", to
# 2. Find and fill out the following list of operators.
#
# I've started it for you.

# Addition
added = 2 + 3
print(f"2 + 3 = {added} (should be 5)")

# Multiplication
multiplied = 2 * 3
print(f"2 * 3 = {multiplied} (should be 6)")



# @TASK: For each section below:
#
# 1. Uncomment the code by removing the `# `
# 2. Replace the `?` with the right operator
# 3. Check it by running `python 016_operators.py`


# == Subtraction ==

subtracted = 2 - 3
print(f"2 ? 3 = {subtracted} (should be -1)")

# == Division ==

divided = 2 / 3
print(f"2 / 3 = {divided} (should be 0.6666666666666666)")

# This kind of 'decimal point' number, 0.6666666666666666 is
# called a float, by the way, meaning 'floating point'.

# == Modulus ==
# Sometimes known as "remainder if we divide 3 by 2"

modulus = 3 % 2
print(f"3 % 2 = {modulus} (should be 1)")

# == Floor division ==
# Sometimes known as "division without remainder"

floor_divided = 2 // 3
print(f"2 // 3 = {floor_divided} (should be 0)")

# == Exponentiation ==
# Sometimes known as "2 to the power of 3"

expr = 2 ** 3
print(f"2 ** 3 = {expr} (should be 8)")

# There are many more operators in Python that you can
# research. You're very welcome to try out a few below:

# OPERATOR PLAYGROUND STARTS

# == Comparison Operators ==
equal = 2 == 2
print(f"2 ** 2 = {equal} (should be True)")

not_equal = 2 != 3
print(f"2 != 3 = {not_equal} (should be True)")

greater_than = 3 > 2
print(f"3 > 2 = {greater_than} (should be True)")

less_than = 2 < 3
print(f"2 < 3 = {less_than} (should be True)")

greater_than_or_equal = 3 >= 3
print(f"3 >= 3 = {greater_than_or_equal} (should be True)")

less_than_or_equal = 2 <= 3
print(f"2 <= 3 = {less_than_or_equal} (should be True)")

# == Logical Operators ==

and_operator = True and True
print(f"True and True = {and_operator} (should be True)")

or_operator = True or False
print(f"True or False = {or_operator} (should be True)")

not_operator = not True
print(f"not True = {not_operator} (should be False)")

# == Assignment Operators ==
assignment = 2
print(f"assignment = {assignment} (should be 2)")

assignment += 3
print(f"assignment += 3 = {assignment} (should be 5)")

assignment -= 3
print(f"assignment -= 3 = {assignment} (should be 2)")

assignment *= 3
print(f"assignment *= 3 = {assignment} (should be 6)")

assignment /= 3
print(f"assignment /= 3 = {assignment} (should be 2.0)")

assignment %= 3
print(f"assignment %= 3 = {assignment} (should be 2.0)")

assignment **= 3
print(f"assignment **= 3 = {assignment} (should be 8.0)")

assignment //= 3
print(f"assignment //= 3 = {assignment} (should be 2.0)")

#== Membership Operators ==

in_operator = 2 in [1, 2, 3]  
print(f"2 in [1, 2, 3] = {in_operator} (should be True)")

not_in_operator = 2 not in [1, 2, 3]
print(f"2 not in [1, 2, 3] = {not_in_operator} (should be False)")

# == Identity Operators ==

is_operator = 2 is 2
print(f"2 is 2 = {is_operator} (should be True)")

is_not_operator = 2 is not 3
print(f"2 is not 3 = {is_not_operator} (should be True)")

# == Ternanry Operators ==
x = 5
result = "Even" if x % 2 == 0 else "Odd" 
print(f"5 % 2 == 0 = {result} (should be Odd)")


# OPERATOR PLAYGROUND ENDS

# Happy? Move on to 017_expressions.py
