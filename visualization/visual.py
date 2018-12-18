# tutorial: https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html#google-maps-support

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

from classes.street import read_junc_coords
from visualization import read_coords
from greedy import greedy_routing

# setup
API_key = "AIzaSyAIF4BahfDRbG-T9lOziP7jtpyhiBPe6n8" # Google API key for GoogleMaps features
output_file("Paris_streets.html")
map_options = GMapOptions(lat=48.855, lng=2.345, map_type="roadmap", zoom=13)
p = gmap(API_key, map_options, title="Paris")
# colors = ['#932567', '#DC5039', '#FBA40A']
input_file = "../input_data.txt"


row_distribution = read_coords.get_info(input_file)
# coords = read_coords.get_lon_lat(input_file)       # get coords for junctions
# print(coords)


# Set coordinates of streets.
# street_lat, street_lon = read_coords.get_street_coords(input_file,
#                                                        row_distribution['junctions_num'],
#                                                        row_distribution['streets_num'])


# Plot junctions (points).
# source = ColumnDataSource(data=dict(lat=coords[0], lon=coords[1]))
# p.circle(x="lon", y="lat", size=3, fill_color="blue", fill_alpha=0.8, source=source)


# Plot streets.
# for i in range(0, len(street_lat), 2):
#     p.line(street_lon[i: i+2], street_lat[i: i+2], line_width=2, color="green")
#          [2.32, 2.35]        [48.86, 48.82]


# Plot routs.
route_coords = greedy_routing(9000, 0)


route_lat, route_lon = [read_junc_coords(el)[0] for el in route_coords], [read_junc_coords(el)[1] for el in route_coords]
p.line(route_lon, route_lat, line_width=4, color="orange")


# Plot the START point
start_lon, start_lat = read_junc_coords(route_coords[0])[0], read_junc_coords(route_coords[0])[1]
p.circle(x=[start_lat], y=[start_lon], size=10, fill_color="green", fill_alpha=0.8)

p.plot_height = 900
p.plot_width = 1800
show(p)

########################################################################################################################

# import chartify
# point degree from db -- lollipop vilualization -- https://github.com/spotify/chartify/blob/master/examples/Examples.ipynb

# map_types: roadmap, hybrid, sattelite, terrain
# GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, Select
# p.add_tools(PreviewSaveTool(), WheelZoomTool(),ResizeTool())

# {'junctions_num': 11348, 'cars_num': 8, 'timespan': 54000, 'streets_num': 17958, 'start_point': 4516}
