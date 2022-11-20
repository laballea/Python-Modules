from matplotlib import pyplot as plt
import pandas
import seaborn


class Komparator():
    def __init__(self, df: pandas.DataFrame):
        self.df = df

    def compare_box_plots(self, categorical_var: list, numerical_var: list):
        """
            displays a series of box plots to compare how the distribution of the numerical variable changes
            if we only consider the subpopulation which belongs to each category. There should
            be as many box plots as categories. For example, with Sex and Height, we would
            compare the height distributions of men vs. women with two box plots.
        """
        try:
            for categorie in categorical_var:
                for numeric in numerical_var:
                    plt.figure()
                    seaborn.boxplot(self.df, x=numeric, y=categorie)
        except Exception as inst:
            print("Something went wrong :/")
            print(inst)

    def density(self, categorical_var, numerical_var):
        """
            displays the density of the numerical variable. Each subpopulation should be represented by a separate curve
            on the graph.
        """
        try:
            for categorie in categorical_var:
                for numeric in numerical_var:
                    plt.figure()
                    seaborn.kdeplot(data=self.df, x=numeric, hue=categorie, common_norm=False)
        except Exception as inst:
            print("Something went wrong :/")
            print(inst)

    def compare_histograms(self, categorical_var, numerical_var):
        """
            plots the numerical variable in a separate histogram for each category. As an extra, you can
            use overlapping histograms with a color code
        """
        try:
            for categorie in categorical_var:
                for numeric in numerical_var:
                    plt.figure()
                    seaborn.histplot(data=self.df, x=numeric, hue=categorie, common_norm=False, element="poly")
        except Exception as inst:
            print("Something went wrong :/")
            print(inst)
