# advent of code 7
# description at https://adventofcode.com/2020/day/7

# Depth first search as a proposed solution
def dfs(graph, start):
    visited = [start]
    stack = [start]

    while stack:
        current_node = stack[-1]
        if current_node not in visited:
            visited.append(current_node)

        neighbors = [n[0] for n in graph[current_node] if n[0] not in visited]

        if not neighbors:
            stack.pop(-1)
            continue
        else:
            stack.append(neighbors[0])

    return visited
graph = {'A': [('B', 4), ('C', 2)], 'B': [('D', 2), ('E', 3), ('C', 2)],
         'C': [('E', 1)], 'D': [], 'E': [('D', 5)]}

bags = {
    'dotted black': [('dark olive', 4), ('vibrant plum', 6)],
    'faded blue': [('dark olive', 3), ('vibrant plum', 5),
                   ('muted yellow', 9)],
    'vibrant plum': [('shiny gold', 2)],
    'dark olive': [('shiny gold', 1)],
    'dark orange': [],
    'muted yellow': [('dark orange', 4), ('light red', 2)],
    'bright white': [('light red', 1), ('dark orange', 3)],
    'light red': [],
    'shiny gold': [('bright white', 1), ('muted yellow', 2)]}

rules = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

rules = rules.split('\n')
for i, r in enumerate(rules):
    rules[i] = r.split(' contain')
print(rules)

# parsing rules
for i in range(len(rules)):
    t = rules[i][0]
    t = t.replace('bags', '')
    t = t.replace('bag', '')
    t = t.strip('. ')
    rules[i][0] = t
    lst = rules[i][1].split(',')
    for j in range(len(lst)):
        s = lst[j]
        s = s.replace('bags', '')
        s = s.replace('bag', '')
        s = s.strip('. ')
        lst[j] = s
    rules[i][1] = lst

# [color, [contained color, contained color]]
test_graph = {}

# making graph
for row in rules:
    for info in row[1]:
        if info == 'no other':
            continue
        else:
            try:
                weight = int(info[0])
                color = info[2:]
                test_graph[color].append((row[0], weight))
            except KeyError:
                weight = int(info[0])
                color = info[2:]
                test_graph[color] = [(row[0], weight)]
print()

for row in rules:
    color = row[0]
    try:
        test_graph[color]
    except KeyError:
        test_graph[color] = []

input = ""
with open("input_files/input_7") as file:
    input = file.read()

print()
input = input.split('\n')
for i, r in enumerate(input):
    input[i] = r.split(' contain')
# parsing input rules
for i in range(len(input)):
    t = input[i][0]
    t = t.replace('bags', '')
    t = t.replace('bag', '')
    t = t.strip('. ')
    input[i][0] = t
    lst = input[i][1].split(',')
    for j in range(len(lst)):
        s = lst[j]
        s = s.replace('bags', '')
        s = s.replace('bag', '')
        s = s.strip('. ')
        lst[j] = s
    input[i][1] = lst

# [color, [contained color, contained color]]
input_graph = {}

# making graph
for row in input:
    for info in row[1]:
        if info == 'no other':
            continue
        else:
            try:
                weight = int(info[0])
                color = info[2:]
                input_graph[color].append((row[0], weight))
            except KeyError:
                weight = int(info[0])
                color = info[2:]
                input_graph[color] = [(row[0], weight)]
# bags that are not contained in any other
for row in input:
    color = row[0]
    try:
        input_graph[color]
    except KeyError:
        input_graph[color] = []


print(len(input_graph))

# example
answer_bags = dfs(test_graph, 'shiny gold')
print(answer_bags)
print("test answer:", len(answer_bags) - 1)

# input
answer_bags = dfs(input_graph, 'shiny gold')
print("input answer:", len(answer_bags) - 1)
