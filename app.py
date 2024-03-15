import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('assets/real_estate.csv', sep=';')

#filtro = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

#subconjunto = ds[ds['level5'].isin(filtro)]
#casas_mas_caras = subconjunto.loc[subconjunto.groupby('level5')['price'].idxmax()]
#for index, fila in casas_mas_caras.iterrows():
#    print(f"La casa más cara de {fila['level5']} es la casa en {fila['address']} con un precio de {fila['price']}.")
#print(subconjunto[['price', 'rooms', 'surface', 'bathrooms']].mean())
#print(subconjunto[['price', 'rooms', 'surface', 'bathrooms']].var())
print(ds.columns)
#nagencias=ds['realEstate_name'].nunique()
#agencias=ds['realEstate_name'].nunique()
#print(", ".join(agencias))
#casa_mas_cara = ds.loc[ds['price'].idxmax()]
#direccion = casa_mas_cara['address']
#precio = casa_mas_cara['price']
#print(f"The house with address '{direccion}' is the most expensive and its price is {precio} EUR.")
#casa_mas_barata = ds.loc[ds['price'].idxmin()]
#direccion = casa_mas_barata['address']
#precio = casa_mas_barata['price']
#print(f"The house with address '{direccion}' is the cheapest and its price is {precio} EUR.")
#casa_mas_grande = ds.loc[ds['surface'].idxmax()]
#casa_mas_pequeña = ds.loc[ds['surface'].idxmin()]
#direccion1 = casa_mas_grande['address']
#area1 = casa_mas_barata['surface']
#direccion2 = casa_mas_pequeña['address']
#area2 = casa_mas_pequeña['surface']
#print(f"The bigger house is located on '{direccion1}'  and its surface is {area1} meters.")
#print(f"The smaler house is located on '{direccion2}'  and its surface is {area2} meters.")
#poblaciones=ds['level5'].unique()
#print(', '.join(poblaciones))
#for index, row in ds.iterrows():
#    for columna in ds.columns:
#        valor = row[columna]
#        if pd.isna(valor):
#            print(f"True: Fila{index + 1}/Columna{columna}")
#        else:
#            print(f"False: Fila{index + 1}/Columna{columna}")
#ds_sin_nans = ds.dropna()
#print("Dimensiones del dataset original:", ds.shape)
#print("Dimensiones del dataset sin NaNs:", ds_sin_nans.shape)
#print(ds.columns[ds.isin(['Arroyomolinos (Madrid)']).any()])
#ds_Arroyomolinos = ds[ds['level5'] == 'Arroyomolinos (Madrid)']
#print(ds_Arroyomolinos['price'].mean())
#plt.figure(figsize = (10, 5))
#plt.hist(ds_Arroyomolinos['price'], bins = 30, alpha = 0.7)
#plt.title("Histogram")
#plt.show()
#ds['pps'] = ds['price'] / ds['surface']
#ds_Valdemorillo = ds[ds['level5'] == 'Valdemorillo']
#print(ds_Valdemorillo['price'].mean())
#ds_Galapagar = ds[ds['level5'] == 'Galapagar']
#print(ds_Galapagar['price'].mean())
#print(ds_Valdemorillo['pps'].mean())
#print(ds_Galapagar['pps'].mean())
