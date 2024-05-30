# Analysis-on-Crop-Yield
In this project, a comprehensive statistical analysis was conducted on a dataset examining crop yield as influenced by different fertilizers and planting densities. The analysis began with reading the data from a CSV file and ensuring the proper classification of variables, with fertilizers, densities, and blocks treated as categorical factors and yield as a numeric variable. Summary statistics were computed to understand the basic structure and distribution of the data. Following this, a series of ANOVA (Analysis of Variance) tests were performed to explore the main effects of fertilizers and densities on crop yield, including one-way ANOVA to examine the effect of fertilizers alone, and two-way ANOVA to assess the individual and combined effects of fertilizers and planting densities.

Further analysis involved exploring interaction effects between fertilizers and planting densities. This was done by fitting an interaction model and conducting an ANOVA test to see if the interaction between these two factors significantly influenced crop yield. The project also accounted for blocking effects by including blocks as an additional factor in the ANOVA model. This helps to control for any variability that could be attributed to different experimental blocks, thereby isolating the effects of the primary factors of interest. A linear regression model was then fitted to the data, which included all three factors (fertilizers, densities, and blocks), and diagnostic plots were generated to assess the model fit and assumptions.

To delve deeper into the differences between specific groups, a post-hoc analysis using Tukey's Honest Significant Difference (HSD) test was conducted. This test helped identify which specific combinations of fertilizers and densities differed significantly from each other in terms of yield. The results were visualized through detailed plots that displayed mean yields, error bars, and group labels to indicate significant differences. The final plot provided a clear visual representation of how crop yields responded to different fertilizers and planting densities, highlighting significant groupings and aiding in the interpretation of the statistical findings.






