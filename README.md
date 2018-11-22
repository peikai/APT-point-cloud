# APT-point-cloud
Help to label coordinations with atomic types and colors in POS file, then generate a point-cloud graph with a HTML file. 

BTW, you can choose which kind of ions to be displayed by in your browser.

## apt2csv

To label .pos or .epos file with ions and colors via [APT-tools](https://github.com/oscarbranson/apt-tools) functions.

```
>>> python apt2csv.py -p ./data/voldata.pos -r ./data/rangefile.rrng -t pos
>>> python apt2csv.py -p ./data/voldata.epos -r ./data/rangefile.rrng -t epos
```

Labeled data is written in a csv file to read and plot, located in output folder.

### Arguments
'-p', '--pos-file', pos file path

'-r', '--rrng-file', rrng file path

'-t', '--input-type', pos or epos

## apt_ploter
Check elements from .rrng file, and type those need to be drawn.

```
>>> python apt_ploter.py -c output/voldata.csv -t cloud -p H O Ca Ga N C
```

What deserves a mention, each or couple of elements can be displayed separately, through clicking or double-clicking the corresponding legends in final web-based graph.

### Arguments
'-c', '--csv-file', csv file path

'-t', '--plot-type', 'cloud' or 'projection'

'-p', '--phases' elements, i.e. 'H' 'O' 'N'

## License
GNU General Public License v2.0

derived from https://github.com/oscarbranson/apt-tools

## Reference
https://plot.ly/python/

https://link.springer.com/content/pdf/bbm%3A978-1-4614-8721-0%2F1.pdf
