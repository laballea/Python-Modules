from numpy import array
import pandas
from FileLoader import FileLoader


class SpatioTemporalData():
    def __init__(self, df: pandas.DataFrame):
        self.df = df

    def when(self, location: str):
        """
            takes a location as an argument and returns a list containing the
            years where games were held in the given location
        """
        loc_cond = self.df["City"] == location
        result = self.df.where(loc_cond).drop_duplicates(subset=['Year'])['Year']

        return array(result.dropna())

    def where(self, date: int):
        """
            takes a date as an argument and returns the location where the
            Olympics took place in the given year
        """
        date_cond = self.df["Year"] == date
        result = self.df.where(date_cond).drop_duplicates(subset=['City'])['City']

        return array(result.dropna())


loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")
sp = SpatioTemporalData(data)
print(sp.where(1896))
print(sp.where(2016))
print(sp.when("Athina"))
print(sp.when("Paris"))
