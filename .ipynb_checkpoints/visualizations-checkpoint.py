import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('raw_data.csv')

# Group the data by 'Artist Name' and count the number of songs per artist
songs_per_artist = df['Artist Name'].value_counts()

# Select the top 20 artists with the highest value counts
top_20_artists = songs_per_artist.head(20)

# Create a bar chart for the top 20 artists
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
top_20_artists.plot(kind='bar', color='skyblue')
plt.xlabel('Artist Name')
plt.ylabel('Number of Songs')
plt.title('Number of Songs per Artist (Top 20)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()