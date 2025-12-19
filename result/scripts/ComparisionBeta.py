import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the Lyon sheet
file_name = "testico2.xlsx - Test HPC Cloud (Lyon).csv"
df = pd.read_csv(file_name)
df_clean = df.dropna(subset=['Carbon Footprint (C) (kg CO2eq)']).copy()

# Rename columns to standard format
df_clean.rename(columns={'Carbon Footprint (C) (kg CO2eq)': 'Carbon Footprint (kg CO2eq)'}, inplace=True)

# 2. Create the combined grouping column (Model - Configuration)
df_clean['Test_Group'] = df_clean['Model'] + ' - ' + df_clean['Configuration']

# 3. Calculate the mean Carbon Footprint grouped by Device and Test_Group
df_mean = df_clean.groupby(['Device', 'Test_Group'])['Carbon Footprint (kg CO2eq)'].mean().reset_index()
df_mean.rename(columns={'Carbon Footprint (C) (kg CO2eq)': 'Mean Carbon Footprint (kg CO2eq)'}, inplace=True)

# Sort the data by Device and then by value for cleaner visualization
df_mean.sort_values(by=['Device', 'Mean Carbon Footprint (kg CO2eq)'], ascending=[True, False], inplace=True)

# 4. Generate the grouped bar plot
plt.figure(figsize=(12, 7))

# Define the GREEN-FOCUSED custom palette (as used in the previous SC3UIS figures)
palette = {
    'Mobilenet - SS': '#3CB371',   # Medium Sea Green (Darker Green for SS)
    'Mobilenet - MS': '#90EE90',   # Light Green (Lighter Green for MS)
    'ResNet50 - SS': '#6B8E23',    # Olive Drab (Darker Olive for SS)
    'ResNet50 - MS': '#9ACD32',    # Yellow Green (Lighter Olive/Yellow Green for MS)
}

# Ensure the order of hue variables
hue_order = ['Mobilenet - SS', 'Mobilenet - MS', 'ResNet50 - SS', 'ResNet50 - MS']

ax = sns.barplot(
    data=df_mean,
    x='Device',
    y='Mean Carbon Footprint (kg CO2eq)',
    hue='Test_Group',
    palette=palette,
    errorbar=None,
    hue_order=hue_order
)

# Add a grid in the background
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set labels and title
ax.set_title('Mean Carbon Footprint Comparison for HPC Cloud (Lyon)', pad=15, fontsize=16)
ax.set_xlabel('HPC Device', fontsize=14, color='black')
ax.set_ylabel('Mean Carbon Footprint (kg CO₂eq)', fontsize=14, color='black')

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
plt.savefig('2d_mean_carbon_footprint_hpc_lyon_green_style.png')
print("2d_mean_carbon_footprint_hpc_lyon_green_style.png")
