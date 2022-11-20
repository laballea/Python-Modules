from FileLoader import FileLoader
from matplotlib import pyplot as plt
from Komparator import Komparator

loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")
komp = Komparator(data)
komp.compare_box_plots(["Medal"], ["Age"])
komp.density(["Medal"], ["Weight"])
komp.compare_histograms(["Medal"], ["Weight"])
plt.show()
