# tutorial: https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html#google-maps-support

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from visualization import read_coords

API_key = "" # Google API key for GoogleMaps features

output_file("Paris_streets.html")
map_options = GMapOptions(lat=48.855, lng=2.345, map_type="roadmap", zoom=13)
p = gmap(API_key, map_options, title="Paris")

input_file = "../input_data.txt"
row_nums = read_coords.get_info(input_file)
coords = read_coords.get_lon_lat(input_file)
street_lat, street_lon = read_coords.get_street_coords(input_file,
                                                       row_nums['junctions_num'],
                                                       row_nums['streets_num'])

# Plot junctions (points).
source = ColumnDataSource(data=dict(lat=coords[0],
                                    lon=coords[1]))

p.circle(x="lon", y="lat", size=3, fill_color="blue", fill_alpha=0.8, source=source)

for i in range(0, len(street_lat), 2):
    # Plot streets (edges).
    p.line(street_lon[i: i+2], street_lat[i: i+2], line_width=2, color="green")
    print(street_lon[i: i+2], street_lat[i: i+2])
# p.line([2.32, 2.35], [48.86, 48.82], line_width=2)

p.plot_height = 900
p.plot_width = 1800
print(street_lat)
show(p)

########################################################################################################################

# import chartify
 # point degree from db -- lollipop vilualization -- https://github.com/spotify/chartify/blob/master/examples/Examples.ipynb


# map_types: roadmap, hybrid, sattelite, terrain
# GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, Select
# p.add_tools(PreviewSaveTool(), WheelZoomTool(),ResizeTool())

# {'junctions_num': 11348, 'cars_num': 8, 'timespan': 54000, 'streets_num': 17958, 'start_point': 4516}
