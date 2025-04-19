from random import randint, choice
from math import sqrt, atan2, degrees

iterations = 100

css = """
@keyframes bounce2 {
"""

# First point (start position)
first = (0, randint(0, 100))

css += "  0% {"
css += f" transform: translate({first[0]}vw, {first[1]}vh);"
css += " }\n"

last = first

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate angle between two points in degrees
def angle(x1, y1, x2, y2):
    return degrees(atan2(y2 - y1, x2 - x1))

for i in range(1, iterations):
    # Start with a random point
    x = randint(25, 80)
    y = randint(25, 80)

    # Ensure the bouncer moves according to edge-to-edge rules
    if last[0] == 0 or last[0] == 100:
        y = choice([0, 100])
    elif last[1] == 0 or last[1] == 100:
        x = choice([0, 100])

    # Check if the distance and angle criteria are met
    dist = distance(last[0], last[1], x, y)
    ang = abs(angle(last[0], last[1], x, y))

    while dist < 30 or ang < 30:
        # Keep generating new x and y until the distance and angle criteria are satisfied
        x = randint(25, 80)
        y = randint(25, 80)

        # Ensure edge-to-edge behavior
        if last[0] == 0 or last[0] == 100:
            y = choice([0, 100])
        elif last[1] == 0 or last[1] == 100:
            x = choice([0, 100])

        dist = distance(last[0], last[1], x, y)
        ang = abs(angle(last[0], last[1], x, y))

        print(f"dist: {dist}, angle: {ang}")

    # Add the keyframe at the current point
    css += f"  {i * (100 / iterations)}% {{ "
    css += f"transform: translate({x}vw, {y}vh);"
    css += " }\n"

    last = (x, y)

# Closing the loop for the last keyframe (return to the first position)
css += "  100% {"
css += f" transform: translate({first[0]}vw, {first[1]}vh);"
css += " }\n"

css += "\n}"

# Write the generated CSS to a file
with open("bounce2.css", "w") as f:
    f.write(css)
