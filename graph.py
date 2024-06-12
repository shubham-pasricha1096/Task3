import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
data = pd.read_csv("C:\\C tutorials\\Internship\\task 3\\householdtask3.csv")
print((data.head(10)))

#Scatter Plot with Year against own
plt.scatter(data['year'],data['own'])
#adding title to the plot
plt.title("Scatter Plot")
#setting the x and y lables 
plt.xlabel('year')
plt.ylabel('own')
#adding the legends
plt.show()

#Line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])
#adding title to the plot
plt.title("Line Chart")
#setting the x and y lables 
plt.xlabel('year')
plt.ylabel('own')
#adding the legends
plt.show()

#Bar chart or bar plot 
plt.bar(data['year'],data['own'])
#adding title to the Bar
plt.title("Bar Chart")
#setting the x and y lables 
plt.xlabel('year')
plt.ylabel('own')
plt.show()

#Histogram Bar Chart 
plt.hist(data['income'])

#adding title to the Histogram
plt.title("Bar Chart")
#setting the x and y lables 
plt.xlabel('year')
plt.ylabel('own')
plt.show()
