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

# moving total row to the end
df = df.append(df.iloc[0]).iloc[1:]
df = df.reset_index(drop=True)

# creating a dictionary for the region names mapping
cyrillic_to_english = {
    'Абай': 'Abai Region',
    'Акмолинская': 'Akmolinskaya Region',
    'Актюбинская': 'Aktobe Region',
    'Алматинская': 'Almaty Region',
    'Атырауская': 'Atyrau Region',
    'Западно-Казахстанская': 'West Kazakhstan Region',
    'Жамбылская': 'Jambyl Region',
    'Жетісу': 'Jetisu Region',
    'Карагандинская': 'Karaganda Region',
    'Костанайская': 'Kostanay Region',
    'Кызылординская': 'Kyzylorda Region',
    'Мангистауская': 'Mangystau Region',
    'Северо-Казахстанская': 'North Kazakhstan Region',
    'Павлодарская': 'Pavlodar Region',
    'Туркестанская': 'Turkistan Region',
    'Ұлытау': 'Ulytau Region',
    'Восточно-Казахстанская': 'East Kazakhstan Region',
    'г.Астана': 'Astana',
    'г.Шымкент': 'Shymkent',
    'г.Алматы': 'Almaty',
    'Республика Казахстан': 'Total'
}
df['Region'] = df['Region'].map(cyrillic_to_english)

# changin data types
df['Region'] = df['Region'].astype(str)
df['2022'] = df['2022'].astype(int)

# Saving the data
df.to_csv('../data/med_institutions.csv', index=False)