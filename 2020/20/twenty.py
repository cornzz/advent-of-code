import math
import re

import numpy as np
from fileinput import input


def get_rotations(t):
    yield t                                                         # Original
    yield np.array([r[::-1] for r in t])                            # Flipped horizontally
    yield t[::-1]                                                   # Flipped vertically
    yield np.array([r[::-1] for r in t[::-1]])                      # Rotated 180 deg
    yield np.array([t[:, c] for c in range(len(t[0]))])             # Flipped diagonally (l to r)
    yield np.array([t[:, c][::-1] for c in range(len(t[0]))])       # Rotated 90 deg
    yield np.array([t[:, -1 - c] for c in range(len(t[0]))])        # Rotated 270 deg
    yield np.array([t[:, -1 - c][::-1] for c in range(len(t[0]))])  # Flipped diagonally (r to l)


def get_edges(t):
    """ Returns [t, b, l, r, t rev, b rev, l rev, r rev] """
    return [''.join(x) for x in
            [t[0], t[-1], t[:, 0], t[:, -1], t[0, ::-1], t[-1, ::-1], t[:, 0][::-1], t[:, -1][::-1]]]


def fit_tile(t, e, e_pos):
    """ Rotates / flips tile t so it matches edge e at position e_pos """
    for r in get_rotations(t):
        if e == get_edges(r)[e_pos]:
            return r


def fuse_grid(grid, width):
    """ Fuses sub-rows of tile-rows into single lines """
    fused = []
    for t_row in range(0, len(grid), width):
        for row in range(8):
            fused.append([y for x in grid[t_row:t_row + width, row] for y in x])
    return np.array(fused)


def grid_to_str(grid):
    """ Creates single line string from grid """
    return ''.join([''.join(x) for x in grid])


data = [line.strip() for line in input('input.txt')]
tiles = dict()

for i in range(0, len(data), 12):
    tile_id = int(data[i][-5:-1])
    tiles[tile_id] = np.array([list(x) for x in data[i + 1:i + 11]])

# ------------------ Part 1 ------------------

tile_edges = dict((tile_id, get_edges(tile)) for (tile_id, tile) in tiles.items())
all_edges = [e for x in tile_edges.values() for e in x]

corner_tiles = []
for tile_id, tile in tiles.items():
    border_edge_count = 0
    for edge in tile_edges[tile_id]:
        if all_edges.count(edge) == 1:
            border_edge_count += 1
    # Border edges appear only twice (normal and reversed)
    # If a tile has two border edges it is a corner tile
    if border_edge_count == 4:
        corner_tiles.append(tile_id)

p1 = math.prod(corner_tiles)

# ------------------ Part 2 ------------------

# Tile grid is built by selecting a corner tile as top left corner, rotating it
# to the correct orientation and then appending matching tiles
tile_grid = []
w = int(math.sqrt(len(tiles)))

# Rotate / flip first corner tile to correct orientation
first_tile = corner_tiles[0]
for rot in get_rotations(tiles[first_tile]):
    edges = get_edges(rot)
    if all_edges.count(edges[0]) == 1 and all_edges.count(edges[2]) == 1:
        tile_grid.append(rot)
        del tiles[first_tile]
        break

# Append tiles row-wise
for i in range(w):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        if j == 0:  # Left edge tile, match next tile with bottom edge of first tile of last row
            t_last = tile_grid[-w]
            edge_to_match = get_edges(t_last)[1]
            edge_pos = 0
        else:       # Match next tile to right edge of last tile
            t_last = tile_grid[-1]
            edge_to_match = get_edges(t_last)[3]
            edge_pos = 2
        for tile_id, tile in tiles.items():
            if edge_to_match in tile_edges[tile_id]:
                t_new = fit_tile(tile, edge_to_match, edge_pos)
                tile_grid.append(t_new)
                del tiles[tile_id]
                break

# Strip borders
tile_grid = np.array([[x[1:9] for x in tile[1:9]] for tile in tile_grid])
# Fuse tiles
tile_grid_fused = fuse_grid(tile_grid, w)

monster = np.array(['..................#.', '#....##....##....###', '.#..#..#..#..#..#...'])
# Lookahead assertion allows for overlapping matches
m_rgx = f'(?=({monster[0]}.{{{w*8 - 20}}}{monster[1]}.{{{w*8 - 20}}}{monster[2]}))'

p2 = 0
for rot in get_rotations(tile_grid_fused):
    image = grid_to_str(rot)
    matches = re.findall(m_rgx, image)
    if matches:
        p2 = image.count('#') - len(matches) * 15
        break

print(f'Part one: {p1}, Part two: {p2}')
