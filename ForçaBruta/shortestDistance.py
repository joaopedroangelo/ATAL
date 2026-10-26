from math import sqrt

def dist(a, b):
    return sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

def shortestDistance(points):
    """
    A brute-force algorithm to find the shortest distance
    between any two points in a given list of points.

    Parameters:
    points (list): A list of tuples representing 
    the coordinates of the points.

    Returns:
    float: The shortest distance between any two points.
    """
    min_distance = float('inf')
    num_points = len(points)

    # Loop through each pair of points to calculate the distance
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = dist(points[i], points[j])
            if distance < min_distance:
                min_distance = distance

    return min_distance 