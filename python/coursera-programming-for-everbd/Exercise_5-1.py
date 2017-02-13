# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters
# "done". Once "done" is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

total = 0
count = 0
while True:
    inp = raw_input("Next number > ")
    if inp == "done": break
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    total = total + num
    count = count + 1
if count <> 0: avg = total / count
else:
    print "No input provided"
    exit()

print "Total =", total
print "Count =", count
print "Average =", avg