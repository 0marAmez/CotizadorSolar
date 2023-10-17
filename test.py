import matplotlib.pyplot as plt

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
data_set1 = [10, 15, 7, 12]
data_set2 = [8, 11, 9, 10]

# Set the width of the bars
bar_width = 0.35

# Generate x-axis values for the categories
x = range(len(categories))

# Create the double bar graph
plt.bar(x, data_set1, width=bar_width, label='Data Set 1')
plt.bar([i + bar_width for i in x], data_set2, width=bar_width, label='Data Set 2')

# Set the x-axis labels
plt.xticks([i + bar_width / 2 for i in x], categories)

# Add labels and a legend
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Double Bar Graph')
plt.legend()

# Display the plot
plt.show()
