# ezvis3d

**ezvis3d** stands for easy vis.js/Graph3d.  
[vis.js Graph3d](http://visjs.org/graph3d_examples.html) is a popular, flexible, versatile, user friendly 3d visualisation javascript library.

**ezvis3d** is a wrapper that lets you transparently access the full configuration options of the library as described in their APIs, directly from the [Jupyter notebook](http://jupyter.org/).

You just need to store the data in a [pandas](http://pandas.pydata.org/) dataframe.
See the examples in these notebooks:
+ the [demo notebook](http://nbviewer.ipython.org/github/oscar6echo/ezvis3d/blob/master/demo_ezvisd3.ipynb).
+ a [Black and Scholes formula viewer](http://nbviewer.ipython.org/github/oscar6echo/ezvis3d/blob/master/BlackScholesViewer.ipynb).

To install run from command line:
```
pip install ezvis3d
```

<!-- pandoc --from=markdown --to=rst --output=README.rst README.md -->