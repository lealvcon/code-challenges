# advent of code 3
'''Due to the local geology, trees in this area only grow on exact integer
coordinates in a grid. You make a map (your puzzle input) of the
open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving
arboreal genetics and biome stability, the same pattern repeats to the right many
times:
You start on the open square (.) in the top-left corner and need to reach the
bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model
that prefers rational numbers); start by counting all the trees you would encounter
for the slope right 3, down 1:'''

test = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

test = test.split('\n')
input = []
with open('input_files/input_3') as file:
    for line in file.readlines():
        input.append(line.strip('\n'))

def traverse(map, right, down):
    l = len(map[0])
    levels = len(map)
    x = 0
    y = 0
    trees = 0
    while y < levels:
        pos = map[y][x]
        if pos == '#':
            trees += 1
        x = (x + right) % l
        y += down
    return trees

print("trees found in test:", traverse(test, 3, 1))
print("trees found in input:", traverse(input, 3, 1))

'''Determine the number of trees you would encounter if, for each of the 
following slopes, you start at the top-left corner and traverse the map all the 
way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) 
respectively; multiplied together, these produce the answer 336.'''

psswd = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # slope [right, down]
for s in slopes:
    psswd *= traverse(test, s[0], s[1])
print("test password=", psswd)
psswd = 1
for s in slopes:
    psswd *= traverse(input, s[0], s[1])

print("password=", psswd)
