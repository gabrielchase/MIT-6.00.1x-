# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

def get_longest_substring(input_string):
    temp = []
    temp_strings = []
    for idx, char in enumerate(input_string):
        if idx < len(input_string)-1: 
            temp.append(char)
            if char > input_string[idx+1] :
                temp_string = ''.join(temp)
                temp_strings.append(temp_string)
                del temp[:]
            if idx == len(input_string)-2:
                if char < input_string[idx+1]:
                    temp.append(input_string[idx+1])
                    temp_string = ''.join(temp)
                    temp_strings.append(temp_string)
                    del temp[:]

    return max(temp_strings, key=len)

print('Statement: %s' % s)
print('Longest substring in alphabetical order is: {}'.format(get_longest_substring(s)))

assert get_longest_substring(s) == 'beggh'
assert get_longest_substring('abcbcd') == 'abc'
assert get_longest_substring('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'
assert get_longest_substring('wlkteoedrkbuekrz') == 'ekrz'
