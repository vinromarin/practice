# Exercise 6.1 Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.
str_inp = raw_input("Enter a string > ")
n = len(str_inp)
while (n > 0):
    print str_inp[n-1]
    n = n - 1