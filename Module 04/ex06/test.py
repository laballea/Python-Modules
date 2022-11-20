from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")
MyPlotLib.histogram(data, ["Weight", "Height", "Age"])
MyPlotLib.density(data, ["Weight", "Height", "Age"])
MyPlotLib.pair_plot(data, ["Weight", "Height", "Age"])
MyPlotLib.box_plot(data, ["Weight", "Height", "Age"])