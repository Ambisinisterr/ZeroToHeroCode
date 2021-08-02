#Volume of Sphere
def vol(rad):
    import math
    return 4/3 * math.pi * rad ** 3
print(vol(2))

#Is number in range?
def ran_check(num,low,high):
    return num in range(low,high+1)

print(ran_check(5,2,7))

#calculate upper case and lower case letters in a string
s = "Hello Mr Rogers, how are you this fine Tuesday?"
def up_lows(s):
    import string
    ups = 0
    lows = 0
    s = s.replace(" ","")
    for char in s:
        if char not in string.ascii_letters:
            continue
        if char.isupper():
            ups += 1
        else:
            lows += 1
    return (ups,lows)
print(up_lows(s))

#Return a list with only unique values
def unique_list(lst):
    return list(set(lst))


nums = [1,1,1,2,2,2,3,3,3,4,5]
print(unique_list(nums))

#multiply all numers in a list
def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(multiply([1,2,3,-4]))

#Is palindrome?
def ispalindrome(s):
    import string
    s = s.lower()
    s = s.replace(" ", "")
    newstr = ""
    for char in s:
        if char in string.ascii_letters:
            newstr += char
    return newstr == newstr[::-1]

print(ispalindrome("Oozy rat in a sanitary zoo"))

#Is Pangram?
def ispangram(s):
    import string
    s = s.lower()
    s = s.replace(" ", "")
    
    s = set(s)
    alphabet = set(string.ascii_lowercase)
    return s == alphabet

str = "The quick brown fox jumps over the lazy dog"
print(ispangram(str))

