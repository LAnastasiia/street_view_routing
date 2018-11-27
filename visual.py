# by this tutprial: https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html#google-maps-support

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from read_coords import get_lon_lat
API_key = "###" # Google API key for GoogleMaps features

output_file("Paris_streets.html")
map_options = GMapOptions(lat=48.855, lng=2.345, map_type="roadmap", zoom=13)

p = gmap(API_key, map_options, title="Paris")

coords = get_lon_lat("input_data.txt")

source = ColumnDataSource(
    data=dict(lat=coords[0],
              lon=coords[1]))

p.circle(x="lon", y="lat", size=3, fill_color="blue", fill_alpha=0.8, source=source)

p.plot_height = 900
p.plot_width = 1800

show(p)


# map_types: roadmap, hybrid, sattelite, terrain
# GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, Select
# p.add_tools(PreviewSaveTool(), WheelZoomTool(),ResizeTool())
