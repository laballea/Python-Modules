from FileLoader import FileLoader
from YoungestFellah import youngest_fellah


loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")


print(youngest_fellah(data, 1992))
# output is: "{'f': 12.0, 'm': 11.0}"

print(youngest_fellah(data, 2004))
# output is: "{'f': 13.0, 'm': 14.0}"

print(youngest_fellah(data, 2010))
# output is: "{'f': 15.0, 'm': 15.0}"

print(youngest_fellah(data, 2003))
# output is: "{'f': nan, 'm': nan}"