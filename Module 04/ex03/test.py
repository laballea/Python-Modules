import pandas as pd
from HowManyMedals import how_many_medals
import os
from FileLoader import FileLoader


loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")

print(how_many_medals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(how_many_medals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"