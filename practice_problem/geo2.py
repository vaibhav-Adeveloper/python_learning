import geopandas as gpd
import matplotlib.pyplot as plt

# Load India states shapefile
india_states = gpd.read_file("gadm41_IND_shp/gadm41_IND_1.shp")

# Inspect actual state names in the shapefile
available_names = india_states["NAME_1"].unique()
print("Available state names in shapefile:")
print(sorted(available_names))

# output :- 

# Available state names in shapefile:
# ['Andaman and Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'NCT of Delhi', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

# Corrected list based on actual shapefile names
target_states = [
    "Ladakh", "Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", 
    "Chandigarh", "Haryana", "Punjab", "NCT of Delhi", 
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
    match = india_states[india_states["NAME_1"] == state]
    if not match.empty:
        match.plot(ax=ax, color=color, edgecolor="black")
    else:
        print(f"Missing or mismatched: {state}")

plt.title("Highlighted States & UTs in India", fontsize=14, weight="bold")
plt.axis("off")
plt.show()