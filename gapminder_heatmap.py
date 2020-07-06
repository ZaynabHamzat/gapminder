# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


#converting txt file into csv file
X = pd.read_csv("gapminder-FiveYearData.txt", delimiter= ",")
X.to_csv ("gapminder-FiveYearData.csv")


#importing dataset
Y = pd.read_csv("gapminder-FiveYearData.csv")


#creating a pivot table 
y= pd.pivot_table(Y, index="continent", columns="year", values="lifeExp")


#creating heatmap using seaborn
heat_map = sb.heatmap(y, cmap="YlGnBu", annot=True)
plt.show 
