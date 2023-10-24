import matplotlib.pyplot as plt

# Sample data
def create_bar_graph(data_set1,data_set2,categories):
    # Set the width of the bars
    bar_width = 0.35

    # Generate x-axis values for the categories
    x = range(len(categories))

    # Create a wider figure (adjust the width and height as needed)
    plt.figure(figsize=(15, 6))  # Width: 10 inches, Height: 6 inches

    # Create the double bar graph
    plt.bar(x, data_set1, width=bar_width, color='yellow',label='Solar energy')
    plt.bar([i + bar_width for i in x], data_set2, width=bar_width, color='green',label='CFE')

    # Set the x-axis labels
    plt.xticks([i + bar_width / 2 for i in x], categories)

    # Add labels and a legend
    plt.xlabel('Bimestres')
    plt.ylabel('Produccion del sistema (kwh/bimestrales)')
    plt.title('Comparación de Producción')
    plt.legend()

    
    plt.axhline(y=data_set1[0], color='red', linestyle='--')
    # Display the value of data_set1[0] at the location of the target line
    plt.text(len(categories), data_set1[0], f'{data_set1[0]}', color='red', va='bottom')
    # Move the legend outside of the plot
    plt.legend(loc='lower left', bbox_to_anchor=(1, 1))
    # Save the plot as an image
    plt.savefig("plot.png", format='png')  # You can change 'png' to other formats like 'pdf', 'jpg', etc.

    # Optionally, you can also close the plot to free up memory
    plt.close()

# Sample data
# data_set1 = [990.0, 990.0, 990.0, 990.0, 990.0,990.0]
# data_set2 = [975.0, 992.0, 891.0, 699.0, 808.0,844.0]
# categories = ['A', 'B', 'C', 'D', 'E','F']

# create_bar_graph(data_set1, data_set2, categories)