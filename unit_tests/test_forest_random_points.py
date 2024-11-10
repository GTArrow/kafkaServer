import sys
from pathlib import Path

project_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_path))


import utils.forest_geo_helper as geo_helper
import utils.visualization_helper as geo_vis

#read coordination from forest boundary file
forest_file_name = 'Forest_Geo/BC_Examples.json' 
forest_name = 'Maternity Island' #use a bigger area to test
geometry = geo_helper.get_forest_geometry_by_name(forest_file_name, forest_name)
full_coordinations = geometry['coordinates'][0] #the output will be a list of coordinations in [longitude,latitude] format


#get N random points within the boundary
random_points = geo_helper.get_rand_points_within_boundary(full_coordinations, num_points=10)
# for eachPoint in random_points:
#     print(eachPoint)

#For testing, uncomment below the visualize the random points in map
#geo_vis.generate_html_map(full_coordinations, random_points, output_file='unit_tests/test_{0}.html'.format((forest_name).replace(" ","_")))

