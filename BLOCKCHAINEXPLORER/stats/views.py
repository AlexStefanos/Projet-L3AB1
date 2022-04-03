from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from stats import draw

# Create your views here.

"""def stats_index(request):
    return render(request, 'stats/stats_index.html')"""

def stats_index(request):
    x_data = draw.drawEthChart()[0]
    y_data = draw.drawEthChart()[1]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='14D ETH CHART',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, 'stats/stats_index.html', context={'plot_div': plot_div})

