# Regular Expressions(regex) in python.
# it makes very easy to perform manupulations in string.

import re

# methods of RE.
# findall, sub, search, split, finditer...

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Direction: View map fass
vaibhav bhai lekin
bahut hi badiya aadmi haiaiin'''


# there are two sequences which are applied to the regex --> meta characters, special sequences.
# we will be using raw string (r)
# r will not escape the escape sequence characters.
# print("\n")
# print(r"\n")  # will literally interperate as a string

# pattern = re.compile(r"fass")
# matches = pattern.finditer(mystr)
# for match in matches:
#     print(match)
# this will return a Match object.
# what does this span means - agar aap string ko slice karogai in the range of
#     span, then you will get that string/pattern.
#     print(mystr[417:421])
# but this is a normal searching which can be done without help of regex.
# regex is used to do complex searching.


# pattern = re.compile(r".adm") # koi sa bhi character ho and then uskai just baad
# # adm likha ho.
# matches = pattern.finditer(mystr)
# for match in matches:
#     print(match)


# pattern = re.compile(r"^Tata")
# pattern = re.compile(r"iin$")
# pattern = re.compile(r"ai*") # means - a ho and then uskai baad i zero bhi ho sakta, yha zero sai zyada bhi ho sakta hai, matlb 1(ek) i ho a kai baad, 2 i ho a kai baad etc.
# pattern = re.compile(r"a*i*") # means - kitnai bhi a ho, zero ya ussai zyada ho a and then uskai baad i zero bhi ho sakta, yha zero sai zyada bhi ho sakta hai
# pattern = re.compile(r"ai+")    # kaam sai kaam ek i toh hona hi chaiyai a kai baad.
# pattern = re.compile(r"ai{2}")    # mujhe exactly aii chaiyai
# pattern = re.compile(r"(ai){2}")    # mujhe aiai chaiyai.
# pattern = re.compile(r"(ai){1}")    # mujhe ai chaiyai.
# pattern = re.compile(r"(ai){1}|t")    # mujhe yha toh ai chaiyai yha phir t chaiyai.
# pattern = re.compile(r"(ai){1}|Fax")    # mujhe yha toh ai chaiyai yha phir Fax chaiyai.
# matches = pattern.finditer(mystr)
# for match in matches:
#     print(match)


# In Python's regular expressions (regex), the caret ( ^ ) has two distinct meanings depending on its context.
# 1. Start of the string (or line): When ^ is used outside of a character set (square brackets []), it acts as an anchor and matches the
# beginning of the string that's being searched. This means the pattern following ^ must occur at the very beginning of the string
# to be considered a match.For example, ^hello would only match "hello" if it appears at the beginning of the input string.
# If the string was "hi hello", it wouldn't match "hello" because it's not at the very start.

# 2. Negating a character set: When ^ is placed inside a character set (inside square brackets []) as the first character,
# it negates the set. This means it will match any character except those listed within the brackets.For example, [^abc] would match
# any character except "a", "b", or "c".

# In Python's regular expressions (regex), the dollar sign ( $ ) is a metacharacter that serves
# as an anchor to indicate the end of the string or the end of a line.
# Here's a breakdown of its meaning:
# End of the string: When used at the end of a regex pattern, $ matches the position immediately
# after the last character in the string.


# Special Character.
# pattern = re.compile(r"\ATata")
# pattern = re.compile(r"\bFax")  # starting with Fax
# pattern = re.compile(r"27\b")  # ending with 27
#
# wants to search a string that contains 5 digit, then -, then 4 digits.
pattern = re.compile(r"\d{5}-\d{4}")
matches = pattern.finditer(mystr)
print(matches)
for match in matches:
    print(match)

# Task - using \b, get the 10 digits number from string.
# Given a string with a lot of indian phone numbers starting from +91.
# return a list containing all that numbers.


# if used finditer() -> matches is a iterable object.
# if used findall() -> matches is a list.


# link
# https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp


# Common special characters
# Here are some of the most common special characters in Python regex and their meanings:
# . (Dot): Matches any single character except for the newline character (\n).
# ^ (Caret): Matches the beginning of the string or the beginning of a line in multiline mode.
# $ (Dollar sign): Matches the end of the string or the end of a line in multiline mode.
# * (Asterisk): Matches zero or more occurrences of the preceding character or group.
# + (Plus sign): Matches one or more occurrences of the preceding character or group.
# ? (Question mark): Matches zero or one occurrence of the preceding character or group.
# [] (Square brackets): Define a character set.
# () (Parentheses): Group parts of the pattern and create capturing groups.
# | (Pipe): Acts as an OR operator.
# \ (Backslash): Used for escaping metacharacters to match them literally (e.g., \. matches a literal dot) and introducing special sequences. Some special sequences include:
# \d: Any digit.
# \s: Any whitespace character.
# \w: Any word character.
# \b: A word boundary.
# \A: Start of the string.
# \Z: End of the string.
