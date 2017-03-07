#Problem:
#Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
#I, II, III, IV, V, VI, VII, VIII, IX, and X.
#The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
#Symbol Value
#I 1 (unus)
#V 5 (quinque)
#X 10 (decem)
#L 50 (quinquaginta)
#C 100 (centum)
#D 500 (quingenti)
#M 1,000 (mille)
#More additional information about roman numerals can be found on the Wikipedia article.
#For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
#Input: A number as an integer.
#Output: The Roman numeral as a string.
#Precondition: 0 < number < 4000


def checkio(data):
    # Symbol    I	V	X	L	C	D	M
    # Value     1	5	10	50	100	500	1,000

    # Specific cases:
    # Number    4	9	40	90	400	900
    # Notation  IV	IX	XL	XC	CD	CM

    # X|XXX
    num1 = int(data / 1000)  # integer part
    s = num1 * 'M'
    num2 = int(data % 1000)  # remaining after div

    # X|XX
    if num2 >= 500 and num2 < 900:
        s += 'D'
        num2 = num2 % 500

    if num2 < 400:
        num1 = int(num2 / 100)
        s += num1 * 'C'
        num2 = num2 % 100
    elif num2 >= 400 and num2 < 500:
        s += 'CD'
        num2 = num2 % 400
    else:
        s += 'CM'
        num2 = num2 % 900

    # X|X
    if num2 >= 50 and num2 < 90:
        s += 'L'
        num2 = num2 % 50

    if num2 < 40:
        num1 = int(num2 / 10)
        s += num1 * 'X'
        num2 = num2 % 10
    elif num2 >= 40 and num2 < 50:
        s += 'XL'
        num2 = num2 % 40
    else:
        s += 'XC'
        num2 = num2 % 90

    # X
    if num2 >= 5 and num2 < 9:
        s += 'V'
        num2 = num2 % 5

    if num2 < 4:
        num1 = num2
        s += num1 * 'I'
    elif num2 == 4:
        s += 'IV'
    else:
        s += 'IX'

    return s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'