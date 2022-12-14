from FileLoader import FileLoader
import pandas


def youngest_fellah(df: pandas.DataFrame, year: int):
    man = df["Sex"] == "M"
    women = df["Sex"] == "F"
    year = df["Year"] == year
    return {
        "f": df.where(year).where(women)['Age'].min(),
        "m": df.where(year).where(man)['Age'].min()
    }
