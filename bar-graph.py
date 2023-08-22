# In this script i will be drawing a Bar Graph using matplotlib.
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
# It can be installed using pip: "pip install matplotlib"
# I will create a bar graph of an analysis of the most common programming languages in 2023

import matplotlib.pyplot as pyplot
# Setting up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 3, 5, 6, 8)
sizes = [50, 20, 30, 40, 45]
# drawing the barchart
pyplot.bar(index, sizes, tick_label=labels)

# Configuring the layout
pyplot.ylabel('Usage in 2023')
pyplot.xlabel('Programming Languages')

# Displaying the chart
pyplot.show()