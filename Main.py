import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.getcwd()

print("Archivos en la carpeta actual:")
print(os.listdir())

df = pd.read_csv("global_shark_attacks.csv")
df.head

df.info()

df = df.drop(["species", "age", "time", "name"], axis = 1, errors = 'ignore')

df.info()

df['date'] = pd.to_datetime(df['date'], errors = 'coerce') 
df['year'] = df['year'].fillna(df['date'].dt.year) 
df = df.dropna(subset = ['year'])
df['year'] = df['year'].astype(int) 

df[['type', 'country', 'area', 'location', 'activity', 'sex']] = df[['type', 'country', 'area', 'location', 'activity', 'sex']].fillna('Unknown')

df['type'] = df['type'].str.title().str.strip()
df['country'] = df['country'].str.title().str.strip()
df['area'] = df['area'].str.title().str.strip()
df['location'] = df['location'].str.title().str.strip()
df['activity'] = df['activity'].str.title().str.strip() 

df['fatal_y_n'] = df['fatal_y_n'].str.upper().str.strip() 
df['fatal_y_n'] = df['fatal_y_n'].replace({'Y': 'Fatal', 'N': 'Non-fatal'})

print("Valores nulos por columna:\n", df.isnull().sum())
print("Ejemplo de datos limpios:\n", df.sample(20)) 
df.to_csv("global_shark_attacks_nuevo.csv", index=False) 
print("Dataset limpio guardado como 'global_shark_attacks_nuevo.csv'")

df.head(15)
df.info()
df.shape
df.describe(include='all')

pd.set_option('display.max_rows', None)
ataques_por_año = df.groupby('year').size().sort_index()
print(ataques_por_año)

df_filtrado = df[df['year'] >= 1800]
ataques_por_año = df_filtrado.groupby('year').size().sort_index()
print(ataques_por_año)

df['decada'] = (df['year'] // 10) * 10
df_filtrado = df[df['year'] >= 1800].copy()

print("Columnas disponibles:", df_filtrado.columns)
ataques_por_decada = (df_filtrado.groupby('decada').size().reset_index(name='n_ataques').sort_values('decada'))
print("\nAtaques por década:")
print(ataques_por_decada.head(10))

# --- GUARDAR GRÁFICA 1 ---
plt.plot(ataques_por_año.index, ataques_por_año.values)
plt.title('Ataques de tiburón por año (desde 1800)')
plt.xlabel('Año')
plt.ylabel('Número de ataques')
plt.savefig("ataques_por_año.png", dpi=300, bbox_inches='tight')
plt.show()

top_actividades = df['activity'].value_counts().head(15)

# --- GUARDAR GRÁFICA 2 ---
plt.figure(figsize=(10,6))
sns.barplot(y = top_actividades.index, x = top_actividades.values, palette = 'crest')
plt.title('Top 15 actividades con más ataques')
plt.xlabel('Número de ataques')
plt.ylabel('Actividad')
plt.savefig("top_actividades.png", dpi=300, bbox_inches='tight')
plt.show()

print("\nTop 10 actividades con más ataques:")
print(top_actividades)

# --- GUARDAR GRÁFICA 3 ---
plt.figure(figsize=(6,5))
df['sex'].value_counts().plot.pie(autopct='%1.1f%%', colors = ["#95c988", '#f4a582', '#cccccc'])
plt.title('Distribución de ataques por sexo')
plt.xlabel('')
plt.ylabel('')
plt.savefig("ataques_por_sexo_1.png", dpi=300, bbox_inches='tight')
plt.show()

print("\nDistribución por sexo (%):")
print(round(df['sex'].value_counts(normalize=True)*100, 2))

df['sex'] = df['sex'].str.upper().str.strip()
df['sex'] = df['sex'].replace({'M X 2': 'M','N': 'UNKNOWN','.': 'UNKNOWN','LLI': 'UNKNOWN','': 'UNKNOWN',np.nan: 'UNKNOWN'})

# --- GUARDAR GRÁFICA 4 ---
plt.figure(figsize=(6,5))
df['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors = ['#88c999', '#f4a582', '#cccccc'])
plt.title('Distribución de ataques por sexo')
plt.xlabel('')
plt.ylabel('')
plt.savefig("ataques_por_sexo_2.png", dpi=300, bbox_inches='tight')
plt.show()

print("\nDistribución por sexo (%):")
print(round(df['sex'].value_counts(normalize=True)*100, 2))

# Mortalidad por actividad
df["fatal_num"] = (df["fatal_y_n"] == "Fatal").astype(int)
mortalidad_por_actividad = (
    df.groupby("activity")["fatal_num"]
      .mean()
      .sort_values(ascending=False))

actividades_con_suficientes_casos = df['activity'].value_counts()
mortalidad_filtrada = mortalidad_por_actividad[actividades_con_suficientes_casos >= 10]

# --- GUARDAR GRÁFICA 5 ---
plt.figure(figsize=(10,6))
mortalidad_filtrada.head(15).plot(kind='barh', color='crimson')
plt.title('Actividades con mayor tasa de ataques fatales')
plt.xlabel('Proporción de ataques fatales')
plt.ylabel('Actividad')
plt.savefig("mortalidad_por_actividad.png", dpi=300, bbox_inches='tight')
plt.show()


# Mortalidad por país
fatal_counts = (
    df.assign(fatal_bin = df['fatal_y_n'].replace({'F':'Fatal'}).eq('Fatal'))
      .groupby('country')['fatal_bin']
      .sum()                       # total de ataques fatales por país
      .sort_values(ascending=False)
      .head(15))


# --- GUARDAR GRÁFICA 6 ---
plt.figure(figsize=(10,6))
fatal_counts.plot(kind='barh', color='tomato')
plt.title('Top 15 países con mayor número de ataques fatales')
plt.xlabel('Número de ataques fatales')
plt.ylabel('País')
plt.savefig("hipotesis5_paises_mas_fatales.png", dpi=300, bbox_inches='tight')
plt.show()  






