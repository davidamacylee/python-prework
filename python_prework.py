# Python Prework Assignments for the
# Coding Temple Self-Paced course
# Amacy Lee

# Question 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
# The first line of code has been defined as below.

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name('davidamacylee')

# Question 2
# Write a python function, first_odds that prints
# the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list
# to return the max number of a given list.
# The first line of code has been defined as below.

def max_num_in_list(a_list):
    max_num = 0
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
another_list = [1, 10, 97, 4, 3, 888, 97, 16]

print(max_num_in_list(my_list))
print(max_num_in_list(another_list))

# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400.
# The return should be a boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
    
# The following test conditions should return False
print(is_leap_year(1993))
print(is_leap_year(2007))
print(is_leap_year(1900))
print(is_leap_year(1800))

# The following test conditions should return True
print(is_leap_year(1600))
print(is_leap_year(2000))
print(is_leap_year(1996))
print(is_leap_year(2004))

# Question 5
# Write a function to check to see if all
# the numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

# First solution attempt:
#
# def is_consecutive(a_list):
#     for i in a_list:
#         j = 1 + 1
#         if a_list[j]:
#             if a_list[i] + 1 == a_list[j]:
#                 continue
#             else:
#                 return False
#     return True

#Second solution attempt:

def is_consecutive(a_list):
    control = a_list[0] - 1
    for num in a_list:
        if num == control + 1:
            control += 1
        else:
            return False
    return True

# The following test conditions should return True
print(is_consecutive([1, 2, 3, 4, 5]))
print(is_consecutive([10, 11, 12, 13, 14, 15]))
print(is_consecutive([-10, -9, -8, -7, -6]))

# The following test conditions should return False
print(is_consecutive([1, 3, 4, 6, 9]))
print(is_consecutive([10, 12, 14, 16, 18]))
print(is_consecutive([-440, -2, 9, 86]))