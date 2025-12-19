#Comparsion of Operational Carboon FootPrint for Edge Devices
#Made by Pablito, Carlitos, Osquitar y Fredericto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the Edge Fog (SC3UIS) file
file_name = "testico2.xlsx - Test Edge Fog (SC3UIS).csv"
df = pd.read_csv(file_name)

# 2. Data Cleaning and Preparation
# Filter out rows where key columns are NaN
df_clean = df.dropna(subset=['Device', 'Model', 'Configuration', 'Carbon Footprint  (kg CO2eq)']).copy()

# Rename the Carbon Footprint column for simplicity and fix capitalization of models
df_clean.rename(columns={'Carbon Footprint  (kg CO2eq)': 'Carbon Footprint (kg CO2eq)'}, inplace=True)
df_clean['Model'] = df_clean['Model'].replace({'Mobilenet': 'MobileNet', 'Resnet': 'ResNet50'})

# Filter the data to exclude 'Laptop' (keeping the data consistent with the previous visual)
df_filtered = df_clean[df_clean['Device'] != 'Laptop'].copy()

# Create the combined grouping column (Model - Configuration)
df_filtered['Test_Group'] = df_filtered['Model'] + ' - ' + df_filtered['Configuration']

# Create the combined device column (Device - HW) for the x-axis
df_filtered['Device_HW'] = df_filtered['Device'] + ' - ' + df_filtered['HW']

# 3. Calculate the mean Carbon Footprint grouped by Device_HW and Test_Group
df_mean = df_filtered.groupby(['Device_HW', 'Test_Group'])['Carbon Footprint (kg CO2eq)'].mean().reset_index()
df_mean.rename(columns={'Carbon Footprint (kg CO2eq)': 'Mean Carbon Footprint (kg CO2eq)'}, inplace=True)

# Sort the data by Device_HW and then by value for cleaner visualization
df_mean.sort_values(by=['Device_HW', 'Mean Carbon Footprint (kg CO2eq)'], ascending=[True, False], inplace=True)

# 4. Generate the grouped bar plot with the green-focused scheme
plt.figure(figsize=(14, 8))

# Define the GREEN-FOCUSED custom palette (same as last successful plot)
palette = {
    'MobileNet - SS': '#3CB371',   # Medium Sea Green (Darker Green for SS)
    'MobileNet - MS': '#90EE90',   # Light Green (Lighter Green for MS)
    'ResNet50 - SS': '#6B8E23',    # Olive Drab (Darker Olive for SS)
    'ResNet50 - MS': '#9ACD32',    # Yellow Green (Lighter Olive/Yellow Green for MS)
}

# Ensure the order of hue variables
hue_order = ['MobileNet - SS', 'MobileNet - MS', 'ResNet50 - SS', 'ResNet50 - MS']

ax = sns.barplot(
    data=df_mean,
    x='Device_HW',
    y='Mean Carbon Footprint (kg CO2eq)',
    hue='Test_Group',
    palette=palette,
    errorbar=None,
    hue_order=hue_order
)

# Add a grid in the background
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set labels and title (MODIFIED TO REMOVE "EXCLUDING LAPTOP")
ax.set_title('Mean Carbon Footprint Comparison for Edge Fog (SC3UIS)', pad=15, fontsize=16)
ax.set_xlabel('Edge Fog Device', fontsize=14, color='black') # MODIFIED TO REMOVE "EXCLUDING LAPTOP"

# Set x-axis labels to horizontal (rotation=0)
plt.xticks(rotation=0, ha='center', fontsize=10)

# Adjust legend position and title to the BOTTOM RIGHT corner
plt.legend(title='Model - Configuration', loc='lower right', bbox_to_anchor=(1.0, 0.05))

# Add value labels on top of the bars (HORIZONTAL)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.5f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=8, color='black', xytext=(0, 5),
                textcoords='offset points', rotation=0)

plt.tight_layout()
plt.savefig('2d_mean_carbon_footprint_edge_fog_sc3uis_no_laptop_clean_labels.png')
print("2d_mean_carbon_footprint_edge_fog_sc3uis_no_laptop_clean_labels.png")


