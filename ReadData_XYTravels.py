import random
import math
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import os
import numpy as np
import pandas as pd

# The folder where your file is stored
folder_path = r'\StudyMaterials\5th Year\MATLS 4K06\Simulation'
# The full path to the file
file_path = os.path.join(folder_path, 'simulation_data_10M.csv')
xy_travels, counts, total_pathlengths = [],[],[]
# Reading from the CSV file
try:
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        # Optional: Read the header, if there is one
        header = next(reader)
        
        
        # Reading and printing each row
        for row in reader:
            
            xy_travels. append(float(row[0]))
            counts.append(float(row[1]))
            total_pathlengths.append(float(row[2]))

           

except FileNotFoundError:
    print(f"File not found: {file_path}")


# Print averages
print(len(xy_travels))
average_count = sum(counts)/ len(counts)
average_total_pathlength = sum(total_pathlengths)/ len(total_pathlengths)
average_radius = sum(xy_travels)/ len(xy_travels)
print(f"Average reflection count: {average_count}")
print(f"Average total pathlength: {round(average_total_pathlength,1)} um")
print(f"Radius: {round(average_radius,1)} um")


## Plotting
sns.histplot(xy_travels, bins=range(0, int(max(xy_travels)) + 101, 100), alpha=0.7, color='blue', edgecolor='black')

plt.title('Histogram of Radius')
plt.xlabel('Distance from Origin (um)')
plt.ylabel('Frequency')
plt.xlim(0,20000)
plt.show()



data = xy_travels

# Calculate histogram data
bin_edges = range(0, int(max(data)) + 101, 100)
hist, bin_edges = np.histogram(data, bins=bin_edges)

# Convert histogram data to a DataFrame
hist_data = {
    'Bin Edges Start': bin_edges[:-1],
    'Bin Edges End': bin_edges[1:],
    'Counts': hist
}
df = pd.DataFrame(hist_data)

# Define your Excel file path
excel_file_path = os.path.join(folder_path, 'histogram_data_10M_radius.xlsx')

# Export to Excel
df.to_excel(excel_file_path, index=False)

print(f"Histogram data exported successfully to {excel_file_path}")