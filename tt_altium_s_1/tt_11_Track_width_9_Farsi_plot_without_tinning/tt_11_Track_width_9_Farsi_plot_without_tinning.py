import matplotlib.pyplot as plt
from matplotlib import font_manager
import arabic_reshaper
from bidi.algorithm import get_display
import os
import warnings

# Suppress warnings (optional)
# This is used to ignore UserWarnings that may arise during execution.
warnings.filterwarnings("ignore", category=UserWarning)

# Define the font path
# Specify the path to the font file that supports Farsi (Persian) characters.
font_path = "C:/Windows/Fonts/Vazir-Bold.ttf"  # Updated to the correct font path

# Ensure the font exists
# Check if the font file exists at the specified path. If not, raise an error.
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font not found at {font_path}. Please check the path!")

# Set font properties
# Create a FontProperties object using the specified font file.
font = font_manager.FontProperties(fname=font_path)

# Function to fix Farsi text display
# This function reshapes and applies the bidirectional algorithm to Farsi text for proper display.
def fix_farsi_text(text):
    reshaped_text = arabic_reshaper.reshape(text)  # Reshape for correct letter joining
    bidi_text = get_display(reshaped_text)  # Apply bidi (right-to-left) algorithm
    return bidi_text

# Example data for currents and widths
# Define sample data for currents and corresponding widths for FR4 and miscellaneous materials.
currents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
width_fr4_mm = [0.254, 0.800, 1.300, 2.000, 2.800, 3.800, 4.500, 5.600, 6.600, 7.600]
width_misc_mm = [0.356, 1.120, 1.820, 2.800, 3.920, 5.320, 6.300, 7.840, 9.240, 10.640]

# Farsi labels and title
# Prepare the title and axis labels in Farsi using the fix_farsi_text function.
title_text = f"{fix_farsi_text('مقایسه پهنای مسیر استاندارد بُردهای FR4 و متفرقه در جریان‌های مختلف')}"
xlabel_text = fix_farsi_text("جریان (آمپر)")
ylabel_text = fix_farsi_text("پهنای مسیر (میلی‌متر)")
legend_fr4 = f"{fix_farsi_text('(mm) ')} FR4 {fix_farsi_text('پهنای')} "
legend_misc = f"{fix_farsi_text('(mm) ')} {fix_farsi_text('پهنای متفرقه')}"

# Create the plot
# Initialize a figure with a specific size for the plot.
plt.figure(figsize=(10, 6))

# Plot the data for FR4 and miscellaneous materials with markers and labels.
plt.plot(currents, width_fr4_mm, marker='o', label=legend_fr4)
plt.plot(currents, width_misc_mm, marker='s', label=legend_misc)

# Add the title and labels
# Set the title and axis labels using the Farsi font.
plt.title(title_text, fontproperties=font, fontsize=14)
plt.xlabel(xlabel_text, fontproperties=font, fontsize=12)
plt.ylabel(ylabel_text, fontproperties=font, fontsize=12)

# Set the legend with the unified font
# Add a legend to the plot using the Farsi font.
plt.legend(prop=font, fontsize=12)

# Add custom annotations for FR4 and Misc
# Position FR4 annotation at the last data point of FR4 with blue color.
plt.text(currents[5], width_fr4_mm[4], "FR4", color='blue', fontsize=12, ha='center', va='bottom')

# Apply arabic_reshaper to the "متفرقه" text and add it above the Misc curve in the center.
misc_text = fix_farsi_text('متفرقه')
plt.text(currents[len(currents)//2], width_misc_mm[len(width_misc_mm)//2] + 1, misc_text, color='red', fontsize=12, ha='center', va='bottom')

# Improve plot layout
# Add a grid for better readability and adjust the layout to avoid clipping.
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
# Display the plot.
plt.show()
