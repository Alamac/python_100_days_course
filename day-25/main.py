import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data.groupby("Primary Fur Color")["Primary Fur Color"].count().reset_index(name='count')

colors.to_csv("squirrel_colors.csv")
