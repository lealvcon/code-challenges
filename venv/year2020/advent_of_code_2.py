# advent of code day 2
'''suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given
letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and
at most 3 times.

In the above example, 2 passwords are valid.
The middle password, cdefg, is not; it contains no instances of b, but needs
at least 1.
The first and third passwords are valid: they contain one a or nine c, both
within the limits of their respective policies.

How many passwords are valid according to their policies?'''

test = ['1-3 a: abcde', \
        '1-3 b: cdefg', \
        '2-9 c: ccccccccc']
input = []
with open('input_files/input_2') as file:
    for line in file.readlines():
        input.append(line)

def check_passwords(input):
    valid = 0
    for p in input:
        s = p.split(':')
        char = s[0].split(' ')[-1]
        pol = s[0].split(' ')[0].split('-')
        pol[0] = int(pol[0])
        pol[1] = int(pol[1])
        password = s[-1].strip()
        t = password.count(char)
        if t >= pol[0] and t <= pol[1]:
            valid += 1
    return valid


print("valid passwords in test:", check_passwords(test))
print("valid passwords in input:", check_passwords(input))

'''Each policy actually describes two positions in the password, where 1 means 
the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?'''


def check_passwords_v2(input):
    valid = 0
    for p in input:
        s = p.split(':')
        char = s[0].split(' ')[-1]
        pol = s[0].split(' ')[0].split('-')
        pol[0] = int(pol[0])
        pol[1] = int(pol[1])
        password = s[-1].strip()
        first = password[pol[0] - 1] == char
        second = password[pol[1] - 1] == char
        if first != second:
            valid += 1
    return valid

print("valid passwords in test:", check_passwords_v2(test))
print("valid passwords in input:", check_passwords_v2(input))

print(input)