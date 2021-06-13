# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

# Solution:

# CREATE EMPTY LIST
l = []

# FOR LOOP WITH RANGE
for num in range(2000, 3200):
    # CHECK FOR DIVISIBILITY
    if (num % 7 == 0) and (num % 5 != 0):
        # IF PASSES => APPEND NUM AS STR
        l.append(str(num))

# PRINT SEPARATED BY COMMAS
print(",".join(l))
