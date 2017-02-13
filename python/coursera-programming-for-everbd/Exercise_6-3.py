# Exercise 6.3 Encapsulate this code in a function named count, and generalize it
# so that it accepts the string and the letter as arguments.
def count(str, symbol):
    count = 0
    for letter in str:
        if letter == symbol:
            count = count + 1
    return count
str_inp = raw_input("Enter string:")
smb_inp = raw_input("Enter symbol to count:")
cnt = count(str_inp, smb_inp)
print cnt