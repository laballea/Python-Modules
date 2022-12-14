import pandas
from FileLoader import FileLoader


def proportion_by_sport(df: pandas.DataFrame, year: int, sport: str, gender: str):
    year = df["Year"] == year
    gender = df["Sex"] == gender
    sport = df["Sport"] == sport
    gender_year = df.where(year & gender)
    gender_year = gender_year[~gender_year["ID"].isna()]
    gender_year = gender_year.drop_duplicates(subset=['Name', 'Sport'])
    gender_year_sport = gender_year.where(sport)
    gender_year_sport = gender_year_sport[~gender_year_sport["ID"].isna()]

    return gender_year_sport.shape[0] / gender_year.shape[0]
