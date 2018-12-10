from visualization.read_coords import get_info
from greedy import greedy_routing

def compare_Max_Len__min_Time():
    # Saves comparison chart to the greedy_time_len_comparison.html file.
    results = {"time": [], "len": []}
    general_info = get_info("input_data.txt")
    for START in range(0, general_info["junctions_num"], 1000):
        rooting_len = greedy_routing()
        print(rooting_len)
        results["len"].append(rooting_len[0])
        results["time"].append(rooting_len[1])

    import holoviews as hv
    import hvplot
    import hvplot.pandas
    import pandas as pd
    hv.extension('bokeh')

    df = pd.DataFrame({'Length':range(0, general_info["junctions_num"], 1000),
       ' ': results["len"],'  ':results["time"]})
    hv.renderer('bokeh').save(df.hvplot.bar('Length', color=["#980f4d", "#e47127"]),'greedy_time_len_comparison')
