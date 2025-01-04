
import cv2
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

image_name = 'BothSide_110us_Least_2.png'
directory_path = r'C:\StudyMaterials\5th Year\MATLS 4K06\Optical Test\Calibrated\Calibration1\Various Integration Time'
file_path = os.path.join(directory_path, image_name)

ADU = cv2.imread(file_path, -1)
ADU = ADU.astype(np.int64)

max_val = np.max(ADU)


# Find the positions (y, x) of the max intensity value
max_pos_y, max_pos_x = np.where(ADU==max_val)
print(max_pos_y, max_pos_x)

# Ensure that there are more than two positions to remove the last two.
# The last two are always outlier (not in the center)
if len(max_pos_y) > 2 and len(max_pos_x) > 2:
    # Exclude the last two occurrences
    max_pos_y = max_pos_y[:-2]
    max_pos_x = max_pos_x[:-2]

    # Calculate the average of the remaining positions
    center_y = np.mean(max_pos_y).astype(int)
    center_x = np.mean(max_pos_x).astype(int)

    print(f'centroid: ({center_x+1}, {center_y+1})')
    # Plus one beacuse the array starts from [0,0] ends at [639,511]
else:
    print("Not enough points to remove the last two.")

grouped_data = {}

# Iterate over each pixel in the image
for y in range(ADU.shape[0]):
    for x in range(ADU.shape[1]):
        
        # Calculate the distance from the centroid  (9000 um/ 640 pixels)
        radius = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) * 9000 / 640    
        
        # bin width = 50 um, average bin vaule = distance_group (the value on represents each bin in the plot)
        distance_group = (int(radius // 50) * 50) + 25
        
        # subtracting each from 80 to reduce background noise
        intensity = ADU[y, x] - 80
        
        # If the group is not in the dictionary, add it
        if distance_group not in grouped_data:
            grouped_data[distance_group] = {'total_intensity': intensity, 'count': 1}
        else:
            # Otherwise, update the total intensity and count
            grouped_data[distance_group]['total_intensity'] += intensity
            grouped_data[distance_group]['count'] += 1

   
# Sort distances and get corresponding total intensities
radiuses = sorted(grouped_data.keys())
totals = [grouped_data[r]['total_intensity'] for r in radiuses]


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(radiuses, totals, color='blue', s = 10)
plt.title('Intensity vs. Radius')
plt.xlabel('Radius (um)')
plt.ylabel('Total Intensity of Each Bin')
plt.grid(True)
plt.show()


#Calculate the average intensity for each group
for group in grouped_data:
    grouped_data[group]['average_intensity'] = grouped_data[group]['total_intensity'] / grouped_data[group]['count']

# Sort distances and get average intensities
radiuses = sorted(grouped_data.keys())
averages = [grouped_data[r]['average_intensity'] for r in radiuses]
counts = [grouped_data[r]['count'] for r in radiuses]

# print(averages)

# plt.figure(figsize=(10, 6))
# plt.scatter(radiuses, averages, color='blue', s = 10)
# plt.title('Intensity vs. Radius')
# plt.xlabel('Radius (um)')
# plt.ylabel('Average Intensity of Each Bin')
# plt.grid(True)
# plt.show()

output_df = pd.DataFrame({'Radius': radiuses, 'Average Intensity': averages, 'Total Intensity': totals, 'Count': counts})

# Path to your Excel file
excel_path = "C:\\StudyMaterials\\5th Year\\MATLS 4K06\\Optical Test\\Calibrated\\Calibration1\\Various Integration Time\\output2.xlsx"


# Use ExcelWriter to append data
with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a', if_sheet_exists='new') as writer:
    output_df.to_excel(writer, sheet_name=image_name, index=False)
print("Data written to new sheet in the Excel file.")
