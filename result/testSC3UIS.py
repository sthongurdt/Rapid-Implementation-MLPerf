#Comparison of Energy Consumation during operation only in the Edge devices exluding laptop measures.
#Make by Pablito, Osquitar, Fredcito 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the Edge Fog (SC3UIS) file
file_name = "testico2.xlsx - Test Edge Fog (SC3UIS).csv"
df = pd.read_csv(file_name)

# 2. Data Cleaning and Preparation
# Filter out rows where key columns are NaN
df_clean = df.dropna(subset=['Device', 'Model', 'Configuration', 'Energy Consumed (kWh)']).copy()

# Rename columns and fix capitalization of models
df_clean['Model'] = df_clean['Model'].replace({'Mobilenet': 'MobileNet', 'Resnet': 'ResNet50'})

# Filter the data to exclude 'Laptop'
df_filtered = df_clean[df_clean['Device'] != 'Laptop'].copy()

# Create the combined grouping column (Model - Configuration)
df_filtered['Test_Group'] = df_filtered['Model'] + ' - ' + df_filtered['Configuration']

# Create the combined device column (Device - HW) for the x-axis
df_filtered['Device_HW'] = df_filtered['Device'] + ' - ' + df_filtered['HW']

# 3. Calculate the mean for Energy Consumed
df_mean = df_filtered.groupby(['Device_HW', 'Test_Group'])['Energy Consumed (kWh)'].mean().reset_index()
df_mean.rename(columns={'Energy Consumed (kWh)': 'Mean Energy Consumed (kWh)'}, inplace=True)

# Sort the data by Device_HW and then by Energy Consumed value for cleaner visualization
df_mean_sorted = df_mean.sort_values(
    by=['Device_HW', 'Mean Energy Consumed (kWh)'], ascending=[True, False]
)

# 4. Define the plotting parameters
palette = {
    'MobileNet - SS': '#3CB371',   # Medium Sea Green (Darker Green for SS)
    'MobileNet - MS': '#90EE90',   # Light Green (Lighter Green for MS)
    'ResNet50 - SS': '#6B8E23',    # Olive Drab (Darker Olive for SS)
    'ResNet50 - MS': '#9ACD32',    # Yellow Green (Lighter Olive/Yellow Green for MS)
}
hue_order = ['MobileNet - SS', 'MobileNet - MS', 'ResNet50 - SS', 'ResNet50 - MS']
x_order = df_mean_sorted['Device_HW'].unique()

# 5. Create a single figure for Energy Consumed
plt.figure(figsize=(10, 7))

ax = sns.barplot(
    data=df_mean_sorted,
    x='Device_HW',
    y='Mean Energy Consumed (kWh)',
    hue='Test_Group',
    palette=palette,
    errorbar=None,
    hue_order=hue_order,
    order=x_order
)

# Set labels and title
ax.set_title('Mean Energy Consumption Comparison for Edge Fog (SC3UIS)', pad=15, fontsize=16)
ax.set_xlabel('Edge Fog Device', fontsize=14, color='black')
ax.set_ylabel('Mean Energy Consumed (kWh)', fontsize=14, color='black')
ax.grid(axis='y', linestyle='--', alpha=0.7)

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
plt.savefig('2d_mean_energy_edge_fog_sc3uis.png')
print("2d_mean_energy_edge_fog_sc3uis.png")
