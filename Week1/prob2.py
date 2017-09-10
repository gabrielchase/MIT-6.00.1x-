# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegghakl'

def bob_counter(input_string):
    bob_counter = 0
    for idx, char in enumerate(input_string):
        if char == 'o' and idx != len(input_string)-1 and idx > 0:
            if input_string[idx-1] == 'b' and input_string[idx+1] == 'b':
                bob_counter += 1
    return bob_counter

print('Statement: %s' % s)
print('Number of times bob occurs is: {}'.format(bob_counter(s)))

assert bob_counter(s) == 2
assert bob_counter('boobnobtzbobbbbobbobbbo') == 3
assert bob_counter('bobboboozaobooboboobobobjboobobyqobooxtbobbbo') == 7
assert bob_counter('obobbobobbobbobomoboobkbobdodoboojbobb') == 7
