import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from rpy2 import robjects as ro
from rpy2.robjects import pandas2ri

# Function to install and load R packages if not already installed
def install_load_r_packages(packages):
    for package in packages:
        if not ro.packages.isinstalled(package):
            ro.r(f"install.packages('{package}')")
        ro.r(f"library({package})")

# Install and load necessary R packages
install_load_r_packages(["ggplot2", "ggpubr", "tidyverse", "broom"])

# Function to run R code
def run_r_code(r_code):
    ro.r(r_code)

# Read the CSV file
@st.cache(persist=True)
def load_data():
    data = pd.read_csv("file.csv")
    return data

data = load_data()

# Convert pandas DataFrame to R DataFrame
pandas2ri.activate()
ro.globalenv['data'] = pandas2ri.py2rpy(data)

# Define R code to run
r_code = """
# Statistical Analysis and Visualization with ggplot2
# Example: Statistical Analysis
oneWayAnova <- aov(yield ~ fertilizer, data = data)
summary(oneWayAnova)

twoWayAnova <- aov(yield ~ fertilizer + density, data = data)
summary(twoWayAnova)

interaction <- aov(yield ~ fertilizer*density, data = data)
summary(interaction)

blocking <- aov(yield ~ fertilizer + density + block, data = data)
summary(blocking)

relation <- lm(yield ~ fertilizer + density + block, data = data)
summary(relation)

# Example: Tukey's HSD Test
tukey.two.way <- TukeyHSD(twoWayAnova)
tukey.two.way

# Example: Mean Yield Data
mean.yield.data <- data %>%
                   group_by(fertilizer, density) %>%
                   summarise(yield = mean(yield))
mean.yield.data$group <- c("a", "b", "b", "b", "b", "c")
mean.yield.data

# Example: Visualization with ggplot2
library(ggplot2)

# Plotting mean yield data
ggplot(mean.yield.data, aes(x = density, y = yield, group = fertilizer, color = fertilizer)) +
  geom_line() +
  geom_point() +
  labs(title = "Mean Crop Yield by Fertilizer and Density",
       x = "Planting Density",
       y = "Yield") +
  theme_minimal()
"""

# Execute R code
run_r_code(r_code)

# Display results using Streamlit
st.title("Crop Yield Analysis")
st.header("Summary of ANOVA and Linear Model")
st.write(ro.r("summary(oneWayAnova)"))  # Display ANOVA summary
st.write(ro.r("summary(twoWayAnova)"))  # Display Two-Way ANOVA summary
st.write(ro.r("summary(relation)"))     # Display Linear Model summary

st.header("Tukey's HSD Test")
st.write(ro.r("tukey.two.way"))        # Display Tukey's HSD results

# Example: Display mean yield data (converted to Python DataFrame)
mean_yield_data = ro.r("mean.yield.data")
st.subheader("Mean Yield Data")
st.write(mean_yield_data)

# Example: Display ggplot2 plot using matplotlib
plt.figure(figsize=(10, 6))
# Placeholder plot; adapt to display ggplot2 plot using reticulate or plotly if needed
plt.plot([1, 2, 3], [1, 4, 9])  # Replace with actual ggplot2 conversion if applicable
plt.title("Example Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
st.pyplot(plt)

