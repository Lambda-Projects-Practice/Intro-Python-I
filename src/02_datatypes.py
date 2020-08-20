"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
print(x + int(y))

# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
print(str(x) + y)


# assign 1 to "x"
# assign 2 to "y"

x, y = 1, 2
print(x, y)

# Create 2 lists called "x_list" and "y_list"
# make x_list contain 10 instances of "x"
# make y_list contain 10 instances of "y"

x_list = [x] * 10
y_list = [y] * 10

print(x_list)
print(y_list)

#create a list called "combined" that 
# contains 10 "x's" and 10 "y's" by concatinating
# x_list and y_list

combined = x_list + y_list
print(combined)