import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read data
data_path = "C:\\Users\\91904\\Documents\\3rd Sem\\17MDC36 Business Statistics Lab using R\\CAT\\crop.data.csv"
data = pd.read_csv(data_path)

# Summary of the data
st.subheader("Summary of Data")
st.write(data.describe())

# ANOVA and Linear Model
st.subheader("Analysis of Variance (ANOVA) and Linear Model")
anova_results = ols('yield ~ C(fertilizer) * C(density)', data=data).fit()
st.write(anova_results.summary())

# Tukey's HSD Test
st.subheader("Tukey's HSD Test")
tukey_results = pairwise_tukeyhsd(data['yield'], data['fertilizer'] + data['density'])
st.write(tukey_results)

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(10, 6))

for (fertilizer, group) in data.groupby('fertilizer'):
    group_means = group.groupby('density')['yield'].mean()
    ax.plot(group_means.index, group_means.values, marker='o', linestyle='-', label=f'Fertilizer {fertilizer}')

ax.set_xlabel('Planting Density (1=Low, 2=High)')
ax.set_ylabel('Yield (Bushels per Acre)')
ax.set_title('Crop Yield in Response to Fertilizer Mix and Planting Density')
ax.legend()
st.pyplot(fig)
