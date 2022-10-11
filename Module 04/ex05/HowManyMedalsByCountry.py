
import pandas
from FileLoader import FileLoader


team_sports = ["Basketball", "Football", "Tug-Of-War", "Badminton",
               "Handball", "Water Polo", "Hockey", "Rowing", "Beach Volleyball",
               "Volleyball", "Synchronized Swimming", "Baseball",
               "Rugby", "Lacrosse", "Polo"]


def how_many_medals_by_country(df: pandas.DataFrame, country: str):
    result = {}
    team_cond = df["Team"] == country
    earn_medal_cond = df["Medal"].notna()
    country_df = df[team_cond & earn_medal_cond]
    years_list = country_df.drop_duplicates(subset="Year")["Year"].sort_values()
    for year in years_list:
        by_year = country_df[(country_df["Year"] == year)].drop_duplicates(subset=["Season", "City", "Sport", "Event", "Medal"])
        result[year] = {
            "G": by_year[(by_year['Medal'] == "Gold")].shape[0],
            "S": by_year[(by_year['Medal'] == "Silver")].shape[0],
            "B": by_year[(by_year['Medal'] == "Bronze")].shape[0]
        }
    return result


loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")
print(how_many_medals_by_country(data, "France"))
