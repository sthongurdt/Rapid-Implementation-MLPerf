#Carbon Footprint (Operational) Comparison
#Make by Pablito, Carlitos, Osquitar and Fredcito

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the Edge Fog (SC3UIS) file
file_name = "testico2.xlsx - Test Edge Fog (SC3UIS).csv"
df = pd.read_csv(file_name)

# 2. Data Cleaning and Preparation
# Filter out rows where key columns are NaN
df_clean = df.dropna(subset=['Device', 'Model', 'Configuration', 'Carbon Footprint  (kg CO2eq)', 'Energy Consumed (kWh)']).copy()

# Rename columns and correct model names
df_clean.rename(columns={'Carbon Footprint  (kg CO2eq)': 'Carbon Footprint (kg CO2eq)'}, inplace=True)
df_clean['Model'] = df_clean['Model'].replace({'Mobilenet': 'MobileNet', 'Resnet': 'ResNet50'})

# Filter the data to exclude 'Laptop' (consistent with the last plot)
df_filtered = df_clean[df_clean['Device'] != 'Laptop'].copy()

# Create grouping columns
df_filtered['Test_Group'] = df_filtered['Model'] + ' - ' + df_filtered['Configuration']
df_filtered['Device_HW'] = df_filtered['Device'] + ' - ' + df_filtered['HW']

# 3. Calculate the mean for both metrics
df_mean = df_filtered.groupby(['Device_HW', 'Test_Group']).agg(
    {'Energy Consumed (kWh)': 'mean', 'Carbon Footprint (kg CO2eq)': 'mean'}
).reset_index()
df_mean.rename(columns={'Energy Consumed (kWh)': 'Mean Energy Consumption (kWh)',
                        'Carbon Footprint (kg CO2eq)': 'Mean Carbon Footprint (kg CO2eq)'}, inplace=True)

# Sort the data by Device_HW
df_mean.sort_values(by=['Device_HW'], ascending=True, inplace=True)

# 4. Generate the combined grouped bar plot (2 subplots)
fig, axes = plt.subplots(1, 2, figsize=(18, 8), sharex=True)
plt.suptitle('Mean Energy Consumption and Carbon Footprint for Edge Fog (SC3UIS)', fontsize=16, y=1.02)

# Define the GREEN-FOCUSED custom palette
palette = {
    'MobileNet - SS': '#3CB371',   # Medium Sea Green (Darker Green for SS)
    'MobileNet - MS': '#90EE90',   # Light Green (Lighter Green for MS)
    'ResNet50 - SS': '#6B8E23',    # Olive Drab (Darker Olive for SS)
    'ResNet50 - MS': '#9ACD32',    # Yellow Green (Lighter Olive/Yellow Green for MS)
}
hue_order = ['MobileNet - SS', 'MobileNet - MS', 'ResNet50 - SS', 'ResNet50 - MS']

# --- Subplot 1: Energy Consumption ---
sns.barplot(
    data=df_mean,
    x='Device_HW',
    y='Mean Energy Consumption (kWh)',
    hue='Test_Group',
    palette=palette,
    errorbar=None,
    hue_order=hue_order,
    ax=axes[0]
)
axes[0].set_title('Mean Energy Consumption (kWh)', fontsize=14)
axes[0].set_xlabel('Edge Fog Device', fontsize=12)
axes[0].set_ylabel('Mean Energy Consumption (kWh)', fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].tick_params(axis='x', rotation=0)

# Add value labels (HORIZONTAL)
for p in axes[0].patches:
    axes[0].annotate(f'{p.get_height():.5f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', fontsize=8, color='black', xytext=(0, 5),
                     textcoords='offset points', rotation=0)
axes[0].get_legend().remove() # Remove subplot legend

# --- Subplot 2: Carbon Footprint ---
sns.barplot(
    data=df_mean,
    x='Device_HW',
    y='Mean Carbon Footprint (kg CO2eq)',
    hue='Test_Group',
    palette=palette,
    errorbar=None,
    hue_order=hue_order,
    ax=axes[1]
)
axes[1].set_title('Mean Carbon Footprint (kg CO₂eq)', fontsize=14)
axes[1].set_xlabel('Edge Fog Device', fontsize=12)
axes[1].set_ylabel('Mean Carbon Footprint (kg CO₂eq)', fontsize=12)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)
axes[1].tick_params(axis='x', rotation=0)

# Add value labels (HORIZONTAL)
for p in axes[1].patches:
    axes[1].annotate(f'{p.get_height():.5f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', fontsize=8, color='black', xytext=(0, 5),
                     textcoords='offset points', rotation=0)

# Extract and place a single shared legend in the bottom right corner of the entire figure
handles, labels = axes[1].get_legend_handles_labels()
axes[1].get_legend().remove() # Remove subplot legend

fig.legend(handles, labels, title='Model - Configuration', loc='lower right', bbox_to_anchor=(1.0, 0.05), ncols=2)

plt.tight_layout(rect=[0, 0.05, 1, 1]) # Adjust layout to make space for the global legend

plt.savefig('3d_edge_fog_energy_carbon_comparison_green.png')
print("3d_edge_fog_energy_carbon_comparison_green.png")

