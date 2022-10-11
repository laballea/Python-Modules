from FileLoader import FileLoader
import pandas


def how_many_medals(df: pandas.DataFrame, name: str):
    name_cond = df["Name"] == name
    athlete = df[name_cond]
    result = {}
    for year in athlete['Year']:
        result[year] = {
            "G": athlete[(athlete['Year'] == year) & (athlete['Medal'] == "Gold")].shape[0],
            "S": athlete[(athlete['Year'] == year) & (athlete['Medal'] == "Silver")].shape[0],
            "B": athlete[(athlete['Year'] == year) & (athlete['Medal'] == "Bronze")].shape[0]
        }
    return result


loader = FileLoader()
data = loader.load("../ressource/athlete_events.csv")
print(how_many_medals(data, "Kjetil Andr Aamodt"))
