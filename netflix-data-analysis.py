import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix.csv")

# Display first 5 rows
print(df.head())

# Count movies vs TV shows
type_count = df['type'].value_counts()
print(type_count)

# Plot chart
type_count.plot(kind='bar', title='Movies vs TV Shows on Netflix')
plt.xlabel("Type")
plt.ylabel("Count")

# Save graph
plt.savefig("netflix_chart.png")

plt.show()

# Top 10 countries producing content
top_countries = df['country'].value_counts().head(10)
print(top_countries)

top_countries.plot(kind='bar', title='Top Countries Producing Netflix Content')
plt.show()