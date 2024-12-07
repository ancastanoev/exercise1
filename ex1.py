import math
import turtle


def orientation(p, q, r):
    """Return the orientation of the triplet (p, q, r).
       >0 : p->q->r is a left turn
       <0 : p->q->r is a right turn
       =0 : p, q, r are collinear
    """
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def convex_hull(points):
    """Compute the convex hull of a set of 2D points using Andrew's monotone chain algorithm."""
    points = sorted(points)  # Sort by x, then by y
    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull
    # The last element of each list is the first element of the other list
    return lower[:-1] + upper[:-1]


def draw_points_and_hull(all_points, hull_points, title="Convex Hull"):
    screen = turtle.Screen()
    screen.title(title)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Determine suitable scaling
    xs = [p[0] for p in all_points]
    ys = [p[1] for p in all_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    offset = 20
    screen.setworldcoordinates(min_x - offset, min_y - offset, max_x + offset, max_y + offset)

    # Draw all points in black
    t.color("black")
    for p in all_points:
        t.penup()
        t.goto(p[0], p[1])
        t.dot(5, "black")

    # Draw hull in red
    if hull_points:
        t.color("red")
        t.penup()
        t.goto(hull_points[0][0], hull_points[0][1])
        t.pendown()
        for h in hull_points[1:]:
            t.goto(h[0], h[1])
        # close the hull
        t.goto(hull_points[0][0], hull_points[0][1])

    t.hideturtle()
    screen.mainloop()


# Part 1: Given points
points_part1 = [(30, 60), (15, 25), (0, 30), (70, 30), (50, 40), (50, 10), (20, 0), (55, 20)]
hull_part1 = convex_hull(points_part1)
draw_points_and_hull(points_part1, hull_part1, title="Convex Hull of Given Points")
