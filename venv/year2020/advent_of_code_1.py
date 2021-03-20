# advent of code 1
# 1243800-20201209-336b634f
'''find the two entries that sum to 2020 and then multiply those two numbers together.
For example, suppose your expense report contained the following:
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579,
so the correct answer is 514579.'''

test = [1721, 979, 366, 299, 675, 1456]

my_input = []
with open('input_files/input_1') as file:
    for line in file.readlines():
        my_input.append(int(line))


def find_pair(input, sum):
    seen = {}
    for n in input:
        try:
            if seen[sum - n] == n:
                return n * (sum - n)
        except KeyError:
            seen[n] = sum - n
    return []

print("test result=", find_pair(test, 2020))
print("first result=", find_pair(my_input, 2020))

'''--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you
a starfish coin they had left over from a past vacation. They offer you a
second one if you can find three numbers in your expense report that meet the
same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.'''


def find_tuple(input):
    for n in input:
        left = 2020 - n
        res = n * find_pair(input, left)
        if res:
            return res


print("test tuple:", find_tuple(test))
print("result tuple:", find_tuple(my_input))
