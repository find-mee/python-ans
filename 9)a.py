import pandas as pd
import matplotlib.pyplot as plt
# Read the data from CSV file
file_path = "train.csv" # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)
# Visualize the dataset using plot()
# Assuming you want to visualize the first few columns
df.iloc[:, :5].plot(x="PassengerId", kind="line")
plt.title("Visualization of First Few Columns")
plt.xlabel("Passenger ID")
plt.ylabel("Value")
plt.show()
# Draw a scatter plot for Age vs Fare
plt.scatter(df["Age"], df["Fare"], c=df["Survived"], cmap="coolwarm")
plt.title("Scatter Plot: Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.colorbar(label="Survived")
plt.show()
# Draw a histogram for Age
plt.hist(df["Age"].dropna(), bins=20, edgecolor="black")
plt.title("Age Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
