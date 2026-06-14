import matplotlib.pyplot as plt

def plot_data(x, y):
    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of X vs Y')
    plt.grid()
    # to show lines connecting the points
    plt.plot(x, y, linestyle=':', color='red', marker='*', ms=10)  # linestyle can be solid, dashed, dotted, etc. marker can be circle, square, star, etc. ms is marker size
    plt.show()

plot_data([6, 4, 3, 1, 5], [2, 3, 5, 7, 11])

# if no axis values are provided, it will plot a line graph with default x values as 0, 1, 2, 3, 4

# Subplots
def plot_subplots(x, y1, y2):
    fig, axs = plt.subplots(2)  # creates a figure with 2 subplots
    axs[0].plot(x, y1, color='blue', marker='o')
    axs[0].set_title('Line Plot of Y1')
    axs[0].grid()
    
    axs[1].scatter(x, y2, color='green')
    axs[1].set_title('Scatter Plot of Y2')
    axs[1].grid()
    
    # super title for the entire figure
    fig.suptitle('Subplots Example', fontsize=16)
    plt.tight_layout()  # adjusts the spacing between subplots
    plt.show()
    
plot_subplots([0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

# Plot multiple scatter plots with lots of cars regarding models years and top speeds
def plot_multiple_scatter(x1, y1, x2, y2):
    # cmap can be used to specify a colormap for the scatter points, which can help differentiate between different datasets visually.
    # c is used to specify the color of the points, which can be a single color or an array of colors corresponding to each point. If you want to use a colormap, you can pass an array of values to c and specify the colormap with cmap.
    plt.scatter(x1, y1, label='Model Year vs Top Speed', c=y1, cmap='nipy_spectral')
    plt.scatter(x2, y2, label='Model Year vs Acceleration', c=y2, cmap='nipy_spectral')
    plt.xlabel('Model Year')
    plt.ylabel('Value')
    plt.title('Scatter Plot of Car Data')
    plt.colorbar()
    plt.legend()
    plt.grid()
    plt.show()
    
# Show 100s of cars 
plot_multiple_scatter([x*2 for x in range(10)], list(range(10)), [x*4 for x in range(10)], list(range(10)))

# Bar Plot
def plot_bar(categories, values):
    plt.bar(categories, values, color='orange', width=0.1)  # width can be adjusted to make bars wider or narrower
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Plot Example')
    plt.grid(axis='y')
    plt.show()
    
plot_bar(['A', 'B', 'C', 'D', 'E'], [5, 7, 3, 8, 6])

# histogram
def plot_histogram(data, bins):
    plt.hist(data, bins=bins, color='purple', edgecolor='black')  # edgecolor adds a border to the bars
    plt.xlabel('Value Ranges')
    plt.ylabel('Frequency')
    plt.title('Histogram Example')
    plt.grid(axis='y')
    plt.show()
    
plot_histogram([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], bins=4)

# Pie chart
def plot_pie(categories, values):
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)  # autopct adds percentage labels to the slices, startangle rotates the pie chart
    plt.title('Pie Chart Example')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    # legend can be added to the pie chart to provide a key for the colors used in the slices. It can be placed outside the pie chart for better visibility.
    plt.legend()
    plt.show()
    
plot_pie(['Category A', 'Category B', 'Category C', 'Category D'], [30, 45, 15, 10])

# Object orinted matplotlib
fig = plt.figure()  # creates a new figure
ax = fig.add_subplot(111)  # adds a subplot to the figure, 111
# Can also add axis via suplots and add_axes
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # adds an axis to the figure, [left, bottom, width, height] in figure coordinates (0 to 1)
# ax = fig.subplots()  # creates a single subplot in the figure and returns the axis object
# ax = fig.subplots(2, 2)  # creates a 2x2 grid of subplots in the figure and returns an array of axis objects
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='cyan', marker='x')  # plots a line on the subplot
ax.set_title('Object-Oriented Matplotlib Example')  # sets the title of the subplot
ax.set_xlabel('X-axis')  # sets the x-axis label
ax.set_ylabel('Y-axis')  # sets the y-axis label
ax.grid()  # adds a grid to the subplot
plt.show()  # displays the figure with the subplot

# Drawing a plot for a df
import pandas as pd
import numpy as np

# Read csv from a housing csv file
df = pd.read_csv('C:\\Work\\Nano\\advanced_programming_ai\\datasets\\housing.csv')
# Plotting the data
plt.scatter(df['median_income'], df['median_house_value'], color='magenta', alpha=0.5)  # alpha controls the transparency of the points
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Scatter Plot of Median Income vs Median House Value')
plt.grid()
plt.show()

# 3d scatter plot using plt.axes projection='3d'
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.scatter(df['median_income'], df['median_house_value'], df['housing_median_age'], color='teal', alpha=0.5)
ax3.set_xlabel('Median Income')
ax3.set_ylabel('Median House Value')
ax3.set_zlabel('Housing Median Age')
ax3.set_title('3D Scatter Plot of Housing Data')
plt.show()

# Seaborn starting here
import seaborn as sns
# import dataset into seaborn
# sns.load_dataset('housing')  # if the dataset is available in seaborn, you can load it directly using sns.load_dataset. However, if it's not available, you can read it using pandas and then use it with seaborn as shown below.
sns.set_theme(style='whitegrid')  # sets the style of the plots to whitegrid
sns.scatterplot(x='median_income', y='median_house_value', data=df, color='green', alpha=0.5)
sns.relplot(x='median_income', y='median_house_value', data=df, hue='housing_median_age', palette='viridis', alpha=0.5)  # hue adds color based on the values of housing_median_age, palette specifies the color scheme
# Should show without plt.show() because seaborn uses matplotlib under the hood and will display the plot automatically in most environments. However, if you're running this in a script or an environment that doesn't automatically display plots,
# you may need to call plt.show() to see the plot.
plt.title('Seaborn Scatter Plot of Median Income vs Median House Value')
plt.show()


