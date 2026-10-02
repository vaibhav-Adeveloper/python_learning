import geopandas as gpd
import matplotlib.pyplot as plt

# Load India states shapefile (replace with your file path)
# Example: "gadm41_IND_1.shp" from gadm.org
india_states = gpd.read_file("gadm41_IND_1.shp")

# States/UTs to highlight
target_states = [
    "Ladakh", "Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", 
    "Chandigarh", "Haryana", "Punjab", "Delhi", 
    "Rajasthan", "Uttar Pradesh"
]

# Create a color map for highlighted states
colors = [
    "lightcoral", "skyblue", "lightgreen", "gold", 
    "violet", "orange", "turquoise", "pink", 
    "khaki", "lightseagreen"
]

# Plot all states (blank)
ax = india_states.boundary.plot(color="black", linewidth=0.6, figsize=(10,12))

# Plot highlighted states with colors
for state, color in zip(target_states, colors):
    india_states[india_states["NAME_1"] == state].plot(ax=ax, color=color, edgecolor="black")

plt.title("Highlighted States & UTs in India", fontsize=14, weight="bold")
plt.axis("off")
plt.show()