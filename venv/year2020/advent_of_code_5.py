#advent of code 5
'''Instead of zones or groups, this airline uses binary space partitioning to
seat people. A seat might be specified like FBFBBFFRLR, where F means "front",
B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the
128 rows on the plane (numbered 0 through 127). Each letter tells you which
half of a region the given seat is in. Start with the whole list of rows; the
first letter indicates whether the seat is in the front (0 through 63) or the
back (64 through 127). The next letter indicates which half of that region the
seat is in, and so on until you're left with exactly one row.
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of
the 8 columns of seats on the plane (numbered 0 through 7). The same process as
above proceeds again, this time with only three steps. L means to keep the lower
half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the
column. In this example, the seat has ID 44 * 8 + 5 = 357.'''

input = []
with open('input_files/input_5') as file:
    for line in file.readlines():
        input.append(line.strip('\n'))

seats = list(range(128))

# helper functions
def binary(seats, half):
    mid = len(seats) // 2
    low = seats[:mid]
    up = seats[mid:]
    if half == 'F' or half == 'L':
        return low
    elif half == 'B' or half == 'R':
        return up


def find_seat(coords, seats):
    rows = coords[:-3]
    seat = coords[-3:]
    row_seats = list(range(8))
    for r in rows:
        seats = binary(seats, r)
    for s in seat:
        row_seats = binary(row_seats, s)
    row = seats[0]
    seat = row_seats[0]
    seat_id = row * 8 + seat
    return seat_id

test='''BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''
test=test.split('\n')

for code in test:
    print("test seats:", find_seat(code,seats))

max = 0
ids = []
for code in input:
    seat_id = find_seat(code, seats)
    ids.append(seat_id)
    if seat_id > max:
        max = seat_id
ids.sort()
for i in range(1, len(ids) - 1):
    prev_idx = i - 1
    next_idx = i + 1
    if ids[next_idx] != (ids[i] + 1):
        print(ids[i] + 1)
        break

print(max)