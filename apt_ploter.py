import argparse

import matplotlib.pyplot as plt
import pandas as pd
import plotly

from apt_importers import *


def csv2pos(data, element):
    initial = data.loc[element]
    pos = initial[['x','y','z']].values
    # a bug existed, when only one line contained in pos.
    color = initial['colour'].values[0]
    px, py, pz = (pos[:,0], pos[:,1], pos[:,2])
    return(px,py,pz,color)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv-file', dest='csv_file', required=True)
parser.add_argument('-t', '--plot-type', dest='plot_type', required=True)
parser.add_argument('-p', '--phases', nargs='+', type=str, action='append', dest='phases', required=True)
options = parser.parse_args()

csv_file = options.csv_file
plot_type = options.plot_type
phases = sum(options.phases,[])

data = pd.read_csv(csv_file, sep=',',usecols=['x','y','z','element', 'colour']).set_index("element")
filename = '_'.join(phases)

if plot_type == 'projection':
    ## plot static images with matplotlib.
    ax = plt.figure().add_subplot(111)
    for element in phases:
        px, py, pz, color = csv2pos(data, element)
        ax.scatter(py, pz, s=2, label=element)
    ax.xaxis.tick_top()
    ax.invert_yaxis()
    ax.set_xlabel('Y')
    ax.xaxis.set_label_position('top')
    ax.set_ylabel('Z')
    plt.legend()
    plt.savefig('output/{fn}.png'.format(fn=filename))

elif plot_type == 'cloud':
    # Adjust fig parameters in def_function.py
    plotly_data=list()
    for element in phases:
        px, py, pz, color = csv2pos(data, element)
        scatter = dict(
            mode = "markers",
            name = element,
            type = "scatter3d",    
            x = px, y = py, z = pz,
            opacity = 0.2,
            marker = dict(size=2, color=color)
        )
        plotly_data.append(scatter)

    layout = dict(
        title = 'APT point cloud',
        scene = dict(xaxis = dict(zeroline=False),
                    yaxis = dict(zeroline=False),
                    zaxis = dict(zeroline=False, autorange='reversed'))
    )
    fig = dict(data=plotly_data, layout=layout)
    plotly.offline.plot(fig, filename='output/{fn}.html'.format(fn=filename), show_link=False)

else:
    print("Plot type error!")
