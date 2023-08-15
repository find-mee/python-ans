import pandas as pd
import matplotlib.pyplot as plt


file_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
data = pd.read_csv(file_path, names=column_names)
# Display first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())
# Display last 5 rows of the dataset
print("\nLast 5 rows of the dataset:")
print(data.tail())
# Display information about the dataset
print("\nInformation about the dataset:")
print(data.info())
# Display overview of the values of each column
print("\nOverview of the values of each column:")
print(data.describe())
# Visualize the dataset using plot()
data.plot()
plt.title("Iris Dataset Visualization")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()
