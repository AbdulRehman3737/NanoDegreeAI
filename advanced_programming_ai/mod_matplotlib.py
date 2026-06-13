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