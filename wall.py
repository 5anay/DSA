import os
import time
import itertools

# Constants
FULL_BRICK = "░░░░"
HALF_BRICK = "░░"
BUILT_BRICK = "▓▓▓▓"
HALF_BUILT_BRICK = "▓▓"

WALL_WIDTH = 2300  # mm
WALL_HEIGHT = 2000  # mm

BRICK_LENGTH = 210  # mm (full brick)
HALF_BRICK_LENGTH = 100  # mm
BRICK_HEIGHT = 50  # mm
HEAD_JOINT = 10  # mm
BED_JOINT = 12.5  # mm
COURSE_HEIGHT = 62.5  # mm

grid_width = WALL_WIDTH // (BRICK_LENGTH + HEAD_JOINT)
grid_height = WALL_HEIGHT // int(COURSE_HEIGHT)

# Generate the Wall Grid
def generate_wall():
    wall = []
    for row in range(grid_height):
        is_even_row = row % 2 == 0
        row_pattern = []
        if is_even_row:
            for _ in range(grid_width):
                row_pattern.append(FULL_BRICK)
        else:
            row_pattern.append(HALF_BRICK)
            for _ in range(grid_width - 1):
                row_pattern.append(FULL_BRICK)
            row_pattern.append(HALF_BRICK)
        wall.append(row_pattern)
    return wall

# Display the Wall
def display_wall(wall, built_set):
    os.system("clear" if os.name == "posix" else "cls")
    for row_idx, row in enumerate(reversed(wall)):
        display_row = []
        for col_idx, brick in enumerate(row):
            if (row_idx, col_idx) in built_set:
                display_row.append(BUILT_BRICK if brick == FULL_BRICK else HALF_BUILT_BRICK)
            else:
                display_row.append(brick)
        print(" ".join(display_row))

# Interactive Building Process
def build_wall_interactive(wall):
    built_set = set()
    bricks_to_build = list(itertools.product(range(grid_height), range(grid_width)))
    for brick in bricks_to_build:
        input("Press ENTER to place a brick...")
        built_set.add(brick)
        display_wall(wall, built_set)
        time.sleep(0.1)

# Optimized Build Order
def optimized_build_order(wall):
    built_set = set()
    stride_id = 0
    for row_start in range(0, grid_height, 2):  # Lay down two rows at a time to minimize movement
        for col in range(grid_width):
            if row_start < grid_height:
                built_set.add((row_start, col))
            if row_start + 1 < grid_height:
                built_set.add((row_start + 1, col))
            display_wall(wall, built_set)
            print(f"Stride {stride_id}")
            stride_id += 1
            input("Press ENTER to continue...")
            time.sleep(0.1)

if __name__ == "__main__":
    wall = generate_wall()
    display_wall(wall, set())
    print("--- Starting Interactive Build ---")
    build_wall_interactive(wall)
    print("--- Optimized Build Process ---")
    optimized_build_order(wall)