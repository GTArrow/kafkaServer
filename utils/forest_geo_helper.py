import json
import random
import shapely

from shapely.geometry import Polygon, Point


def get_forest_geometry(data, forest_name):

    for feature in data.get("features", []):
        # Check if the feature has the name we're looking for
        if feature["properties"].get("name") == forest_name:
            return feature.get("geometry")

    return None


def get_forest_geometry_by_name(file_name, forest_name):

    with open(file_name, "r") as f:
        data = json.load(f)

    return get_forest_geometry(data, forest_name)


def get_rand_points_within_boundary(coordinates, num_points=10):
    """
    Generate random points within a polygon boundary.

    Parameters:
    - coordinates (list): A list of coordinate pairs defining the polygon boundary in [longitude, latitude] format.
    - num_points (int): The number of random points to generate inside the polygon.

    Returns:
    - list: A list of randomly generated points within the polygon as (longitude, latitude) tuples.
    """
    # Create a Polygon object from the boundary coordinates
    polygon = Polygon(coordinates)

    # Get the bounds of the polygon (minx, miny, maxx, maxy)
    min_x, min_y, max_x, max_y = polygon.bounds

    # List to store random points
    random_points = []

    # Generate points until we have the desired number
    while len(random_points) < num_points:
        # Generate a random point within the bounding box
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))

        # Check if the point is within the polygon
        if polygon.contains(random_point):
            # If within, add to the list as (longitude, latitude)
            random_points.append([random_point.x, random_point.y])

    return random_points
