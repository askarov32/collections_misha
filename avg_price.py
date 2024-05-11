import numpy as np
import pandas as pd

def appendList(df, lst):
    for index, row in df.iterrows():
        price_string = row['price']
        if pd.notnull(price_string):
            try:
                price = float(price_string.replace(",", "."))
                lst.append(price)
            except ValueError:
                pass
    return lst

def getAvgPrice(lst):
    if len(lst) == 0:
        return np.nan
    arr = np.array(lst)
    avg = np.nanmean(arr)
    return avg

df = pd.read_csv("misha.csv")
prices = []

prices = appendList(df, prices)

print(len(prices))
print(getAvgPrice(prices))
