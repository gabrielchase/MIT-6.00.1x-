# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
# your program should print `Number of vowels: 5`

s = 'azcbobobegghakl'
VOWELS = ['a', 'e', 'i', 'o', 'u']

def vowel_counter(input_string):
    vowel_count = 0
    for i in input_string.lower():    
        if i in VOWELS:
            vowel_count += 1
    return vowel_count

print('Statement: %s' % s)
print('Number of vowels: {}'.format(vowel_counter(s)))

assert vowel_counter(s) == 5
assert vowel_counter('sexysexy') == 2
assert vowel_counter('aeiou') == 5

