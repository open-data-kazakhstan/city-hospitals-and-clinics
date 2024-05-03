import pandas as pd
import numpy as np

# loading the data
df = pd.read_excel('../archive/source.xls')

# cleaning and preparing the data
df = df.drop(df.index[0:6])
df = df.drop(df.index[-4:])
df.columns = df.iloc[0]
df = df[1:]
df = df.rename(columns={df.columns[0]: 'Region'})
df = df.iloc[:, [0, -4]]
df = df[pd.to_numeric(df['2022'], errors='coerce').notnull()]

# moving first row to the end of the dataframe
df = pd.concat([df.iloc[1:], df.iloc[0:1]], ignore_index=True)

# creating a dictionary for the region names mapping
cyrillic_to_english = {
    "Республика Казахстан": "The Republic of Kazakhstan",
    "Абай": "Abai Region",
    "Акмолинская": "Akmola Region",
    "Актюбинская": "Aktobe Region",
    "Алматинская": "Almaty Region",
    "Атырауская": "Atyrau Region",
    "Западно-Казахстанская": "West Kazakhstan Region",
    "Жамбылская": "Jambyl Region",
    "Жетісу": "Jetisu Region",
    "Карагандинская": "Karaganda Region",
    "Костанайская": "Kostanay Region",
    "Кызылординская": "Kyzylorda Region",
    "Мангистауская": "Mangystau Region",
    "Павлодарская": "Pavlodar Region",
    "Северо-Казахстанская": "North Kazakhstan Region",
    "Туркестанская": "Turkistan Region",
    "Ұлытау": "Ulytau Region",
    "Восточно-Казахстанская": "East Kazakhstan Region",
    "г.Астана": "Astana city",
    "г.Алматы": "Almaty city",
    "г.Шымкент": "Shymkent city"
}
df['Region'] = df['Region'].map(cyrillic_to_english)

# changin data types
df['Region'] = df['Region'].astype(str)
df['2022'] = df['2022'].astype(int)

# Saving the data
df.to_csv('../data/med_institutions.csv', index=False)