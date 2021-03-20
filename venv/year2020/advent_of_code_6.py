#advent_of_code_6
'''For each of the people in their group, you write down the questions for
which they answer "yes", one per line a - z). For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes":
a, b, c, x, y, and z. (Duplicate answers to the same question don't count
extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected
answers from every group on the plane (your puzzle input). Each group's answers
are separated by a blank line, and within each group, each person's answers are
on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:
The first group contains one person who answered "yes" to 3 questions: a, b,
and c.
The second group contains three people; combined, they answered "yes" to 3
questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3
questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1
question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?'''

test = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

input = ''
with open("input_files/input_6") as file:
    input = file.read()

test = test.split('\n\n')
print(test)
# for t in range(len(test)):
#   test[t] = test[t].replace('\n', '')
print(test)

input = input.split('\n\n')
#for i in range(len(input)):
#  input[i] = input[i].replace('\n','')

def count_answers(input):

    total_yes = 0
    for batch in input:
        batch = batch.replace('\n','')
        yes = {}
        for question in batch:
            try:
                if yes[question] == 1:
                    continue
            except KeyError:
                yes[question] = 1
        total_yes += sum(yes.values())

    return total_yes
print("test answers:", count_answers(test))
print("input answers:", count_answers(input))

'''--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread 
one word in the instructions:
You don't need to identify the questions to which anyone answered "yes"; you 
need to identify the questions to which everyone answered "yes"!
Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:
In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, 
and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some 
people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". 
What is the sum of those counts?'''


def count_answers_v2(input):
    total_yes = 0
    for batch in input:
        batch = batch.split('\n')
        yes = {}
        for person in batch:
            l = len(batch)
            for question in person:
                try:
                    yes[question] += 1
                    if yes[question] == l:
                        total_yes += 1
                except KeyError:
                    yes[question] = 1
                    if yes[question] == l:
                        total_yes += 1

    return total_yes

print("test answers:", count_answers_v2(test))
print("input answers:", count_answers_v2(input))
