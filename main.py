import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
pd.set_option('display.max_rows', None)

for column in df.columns:
    print(column)
print("-------------")

diff_countries_amount = df["Country"].value_counts()
print(diff_countries_amount[diff_countries_amount >= 6])
print("----------")
data_gabon = df[df["Country"] == "Gabon"]
print(data_gabon)
