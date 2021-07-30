import csv
from numpy.lib.function_base import corrcoef
import pandas as pd
import plotly.express as ps
import numpy as np

with open("pro/correlation/data.csv") as dataFile:
    df = csv.DictReader(dataFile)
    fig = ps.scatter(df,x="Days Present",y = "Marks In Percentage")
    fig.show()

def getDataSource():
    marksInPercent = []
    daysPresent = []
    with open("pro/correlation/data.csv") as dataFile:
        df = csv.DictReader(dataFile)
        for row in df : 
            marksInPercent.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return{"x":marksInPercent,"y":daysPresent}

def findCorrelation(datacorr):
    correlation = np.corrcoef(datacorr["x"],datacorr["y"])
    print(" The Correlation Is "+str(correlation[0,1]))

def main():
    dataCorr = getDataSource()
    findCorrelation(dataCorr)

main()
