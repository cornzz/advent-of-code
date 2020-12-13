import math


def move(direction, v, waypoint):
    if not waypoint:
        pos[0] += v if direction == 'E' else -v if direction == 'W' else 0
        pos[1] += v if direction == 'N' else -v if direction == 'S' else 0
    else:
        pos_waypoint[0] += v if direction == 'E' else -v if direction == 'W' else 0
        pos_waypoint[1] += v if direction == 'N' else -v if direction == 'S' else 0


def move_forward(v, waypoint):
    if not waypoint:
        move(directions[current_dir], v, False)
    else:
        pos[0] += pos_waypoint[0] * v
        pos[1] += pos_waypoint[1] * v


def rotate(direction, v, waypoint):
    global current_dir, pos_waypoint
    if not waypoint:
        if direction == 'L':
            current_dir = int((current_dir - v / 90) % 4)
        elif direction == 'R':
            current_dir = int((current_dir + v / 90) % 4)
    else:
        v = math.radians(-v if direction == 'L' else v)
        new_waypoint_x = round(pos_waypoint[0] * math.cos(v) + pos_waypoint[1] * math.sin(v))
        new_waypoint_y = round(-pos_waypoint[0] * math.sin(v) + pos_waypoint[1] * math.cos(v))
        pos_waypoint = [new_waypoint_x, new_waypoint_y]


def run(waypoint=False):
    for line in data:
        action, value = line[0], int(line[1:])
        if action in directions:
            move(action, value, waypoint)
        elif action == 'F':
            move_forward(value, waypoint)
        elif action in ['L', 'R']:
            rotate(action, value, waypoint)


with open('input.txt') as f:
    data = f.read().splitlines()

# Part one
pos = [0, 0]  # x, y
directions = ['N', 'E', 'S', 'W']
current_dir = 1

run(False)
p1 = abs(pos[0]) + abs(pos[1])

# Part two
pos = [0, 0]
pos_waypoint = [10, 1]

run(True)
p2 = abs(pos[0]) + abs(pos[1])

print(f'Part one: {p1}, Part two: {p2}')
