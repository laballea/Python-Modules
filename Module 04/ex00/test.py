from FileLoader import FileLoader
import os

f = FileLoader()

df = f.load("../ressource/athlete_events.csv")
f.display(df, 3)
f.display(df, -3)
f.display(df, 0)
f.display(df, "lol")