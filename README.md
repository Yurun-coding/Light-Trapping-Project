# Light-Trapping-Project
This repo contains the code for my senior research project "_A Parameterization Method for Light Trapping in Silicon Solar Cells_", conducted under the supervision of Dr. Kleiman from Engineering Physics department.

The project focused on analyzing the escape light patterns of a 1550 nm laser during the internal reflection process in silicon solar cells. This analysis was conducted using Python and involved an InGaAs-based camera to capture the light patterns.

![Experiment Scheme Image]()

[ReadImage.py](ReadImage.py): This script retrieves the pixel values from the image, finds the centroid of the image (the brightest spot), and makes a histogram of intensity (pixel values) vs. radius.

[Simulation.py](Simulation.py): This script simulates light trapping in an ideal silicon solar cell for many iterations.

"ReadData_" files: These scripts read simulationn data and plot histograms of corresponding values vs. raius.
