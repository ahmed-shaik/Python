import numpy as np
import math
# important components Function, Variable
# Python File Module
# Library = Multiple modules
# Package = Collection of multiple libraries


# User defined Library
# Numpy (Numerical Computation with Arrays)
# - Matplotlib ( Data Visualization)
# Pandas (Data Manipulation/ Data Preprocessing)

# Numpy Numerical Python
# Main object - Array

# Difference between List and Array(Numpy)
#1)arrays have Broadcasting
#2) arrays are faster

# a=[2,4,6,8,10]
# print (a)
# print (type(a))
# a/2 # give an error message

# import numpy as np
# a=np.array([2,4,6,8,10])
# print(a)
# print(type(a))
# print(a/2)

#Single Dimension Vector
# Two Dimension - Matrix
# Three or more dimension Tensor

# b=np.array([[2,4,5,6,7],
#             [1,2,3,4,5]])
# print(b.ndim)

#NUmpy methods:
# np.add()
# np.subtract()
# np.where()
# np.dot()
# np.ptp()
# np.sum()
# np.max()
# np.min()
# np.mean()
# np.median()

# x = np.array([3,4])
# y = np.array([7,6])
# # print(x+y)
# print(np.add(x,y))
# # print(x-y)
# print(np.subtract(x,y))

# print(np.sum(x))

# print(np.mean(x))
# print(np.median(x))
# print(np.min(x))
# print(np.max(x))

#Numpy Operations:
# Euclidean Distance
# Normalization using Min Max Scalar
# Matrix Multiplication (Dot Product)
# Mean Squared Error

# # Euclidean Distance
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[7, 8], [9, 10],[11, 12]])
# # print(math.sqrt((a[1]-a[0])*(a[1]-a[0])+(b[1]-b[0])*(b[1]-b[0])))
# print(np.sqrt(np.sum(np.square(np.subtract(a,b)))))

# Normalization using Min Max Scalar
# a = np.array([6,5,78,153,89])
# for i in a:
#     i = (i-np.min(a))/(np.max(a)-np.min(a))
#     print(i)
    
 
# #Matrix Multiplication (Dot Product)
# print(np.dot(a,b))

# # Mean Squared Error
# y_pred = np. array( [110, 220, 330] )
# y_real = np. array( [100, 200, 300] )

# error = np.subtract(y_pred, y_real)
# sq = np.square(error)
# mse = np.mean(sq)

# print('Mean Squared Error:', mse)

#Data Visualization using Matplotlib

# Graphs
# 1.Line PLot
# 2.Scatter Plot
# 3.Bar Graph
# 4.Pie Chart - Assignment
# 5.Histogram
# 6.Density Kernel

# import matplotlib.pyplot as plt
# x = np.array([322,34,25])
# y = np.array([6,83,130])
# plt.plot(x,y, c='red', ls="--", lw=2, marker="*", mfc=3)
# plt.xlim(0, 350) #graph starts from 0 to 350
# plt.ylim(0, 200)
# for i in range(len(x)):
#     plt.text(x[i], y[i], (x[i], y[i]))
#     i+=1
# plt.xlabel("x-label")
# plt.ylabel("y-axis")
# plt.title("Line Graph")
# plt.show()

#list of `.Line2D`
#     A list of lines representing the plotted data.

# Other Parameters
# ----------------
# scalex, scaley : bool, default: True
#     These parameters determine if the view limits are adapted to the
#     data limits. The values are passed on to
#     `~.axes.Axes.autoscale_view`.

# **kwargs : `.Line2D` properties, optional
#     *kwargs* are used to specify properties like a line label (for
#     auto legends), linewidth, antialiasing, marker face color.
#     Example::

#     >>> plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
#     >>> plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')

#     If you specify multiple lines with one plot call, the kwargs apply
#     to all those lines. In case the label object is iterable, each
#     element is used as labels for each set of data.

#     Here is a list of available `.Line2D` properties:

#     Properties:
#     agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image
#     alpha: scalar or None
#     animated: bool
#     antialiased or aa: bool
#     clip_box: `.Bbox`
#     clip_on: bool
#     clip_path: Patch or (Path, Transform) or None
#     color or c: color
#     dash_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
#     dash_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
#     dashes: sequence of floats (on/off ink in points) or (None, None)
#     data: (2, N) array or two 1D arrays
#     drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
#     figure: `.Figure`
#     fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
#     gapcolor: color or None
#     gid: str
#     in_layout: bool
#     label: object
#     linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
#     linewidth or lw: float
#     marker: marker style string, `~.path.Path` or `~.markers.MarkerStyle`
#     markeredgecolor or mec: color
#     markeredgewidth or mew: float
#     markerfacecolor or mfc: color
#     markerfacecoloralt or mfcalt: color
#     markersize or ms: float
#     markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool]
#     mouseover: bool
#     path_effects: `.AbstractPathEffect`
#     picker: float or callable[[Artist, Event], tuple[bool, dict]]
#     pickradius: unknown
#     rasterized: bool
#     sketch_params: (scale: float, length: float, randomness: float)
#     snap: bool or None
#     solid_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
#     solid_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
#     transform: unknown
#     url: str
#     visible: bool
#     xdata: 1D array
#     ydata: 1D array
#     zorder: float



#Line Plot is used ill Regression Analysis, Forecasting, Trend Analysis
# Scatter Plot: Line Plot with Marker but without a linel

import matplotlib.pyplot as plt
import numpy as np
# # x= np.arange(1,6)
# # z = np.power(x,3)
# # plt.scatter(x,z,color='g', marker='+', label='Cube')
# # plt.legend()
# plt.show()

# Bar Graph
# Create a Numpy array named person and put 4 people names in that
# Create another array with respective heights of those people

person= np.array(['a', 'b', 'c', 'd'])
height = np.array([142,154,134, 153])
width = np.array([45, 56, 35, 46])
plt.bar(person,height, width=0.4, align='edge')
plt.bar(person, width, width=-0.4, align='edge')
plt.xlabel( 'Person')
plt.ylabel( 'Height' )
plt.show()