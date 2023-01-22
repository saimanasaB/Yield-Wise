library(ggplot2)
library(ggpubr)
library(tidyverse)
library(broom)
data<-read.csv("C:\\Users\\91904\\Documents\\3rd Sem\\17MDC36 Business Statistics Lab using R\\CAT\\crop.data.csv", header = TRUE, colClasses = c("factor", "factor", "factor", "numeric"))
summary(data)
oneWayAnova <- aov(yield ~ fertilizer, data = data) #ONE-WAY ANOVA
summary(oneWayAnova)
twoWayAnova <- aov(yield ~ fertilizer + density, data = data)#TWO-WAY ANOVA
summary(twoWayAnova)
interaction <- aov(yield ~ fertilizer*density, data = data)#INTERACTION
summary(interaction)
blocking <- aov(yield ~ fertilizer + density + block, data = data)#BLOCKING
summary(blocking)
relation <- lm(yield ~ fertilizer + density + block, data = data)
summary(relation)
plot(relation)
tukey.two.way<-TukeyHSD(twoWayAnova)
tukey.two.way
tukey.plot.aov<-aov(yield ~ fertilizer:density, data=data)#POST-HOC TEST
tukey.plot.test<-TukeyHSD(tukey.plot.aov)
plot(tukey.plot.test, las = 1)
mean.yield.data <- data %>%group_by(fertilizer, density) %>%summarise(yield = mean(yield))
mean.yield.data$group <- c("a","b","b","b","b","c")
mean.yield.data
two.way.plot <- ggplot(data, aes(x = density, y = yield, group=fertilizer)) +geom_point(cex = 1.5, pch = 1.0,position = position_jitter(w = 0.1, h = 0))
two.way.plot <- two.way.plot +stat_summary(fun.data = 'mean_se', geom = 'errorbar', width = 0.2)+stat_summary(fun.data = 'mean_se', geom = 'pointrange') +geom_point(data=mean.yield.data, aes(x=density, y=yield))
two.way.plot <- two.way.plot +geom_text(data=mean.yield.data, label=mean.yield.data$group, vjust = -8, size = 5) +facet_wrap(~ fertilizer)
two.way.plot <- two.way.plot +theme_classic2() +labs(title = "Crop yield in response to fertilizer mix and planting density",x = "Planting density (1=low density, 2=high density)",y = "Yield (bushels per acre)")
two.way.plot



