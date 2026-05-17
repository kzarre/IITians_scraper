import pandas as pd


df = pd.read_excel("students/students2.xlsx")


print(df["company"].value_counts())