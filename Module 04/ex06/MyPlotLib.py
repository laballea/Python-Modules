from matplotlib import pyplot as plt
import pandas
import seaborn


class MyPlotLib():
    def histogram(data: pandas.DataFrame, features: list):
        """
            plots one histogram for each numerical feature in
            the list
        """
        data[features].hist()
        plt.show()

    def density(data, features):
        """
            plots the density curve of each numerical feature in
            the list
        """
        data[features].plot.density()
        plt.show()

    def pair_plot(data, features):
        """
            plots a matrix of subplots (also called scatter plot
            matrix). On each subplot shows a scatter plot of one numerical variable against
            another one. The main diagonal of this matrix shows simple histograms
        """
        seaborn.pairplot(data[features])
        plt.show()

    def box_plot(data, features):
        """
            displays a box plot for each numerical variable in the
            dataset
        """
        seaborn.boxplot(data[features])
        plt.show()
