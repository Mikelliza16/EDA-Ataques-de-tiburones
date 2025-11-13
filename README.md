# 🦈 Análisis Exploratorio de Datos: Ataques de Tiburón en el Mundo

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre los ataques de tiburón registrados en todo el mundo.  
Su objetivo es identificar patrones en el tiempo, en las regiones costeras y en las actividades humanas más asociadas a estos incidentes.  
El análisis permite entender mejor cuándo y dónde se producen los ataques, así como su gravedad y frecuencia real.  
Los resultados sirven como base sencilla y fundamentada para mejorar la prevención y la información pública sobre este tipo de sucesos.

---

## 📖 Objetivo principal del análisis

El objetivo principal de este proyecto es **analizar los ataques de tiburón registrados en todo el mundo**, buscando entender **dónde, cuándo y por qué ocurren con mayor frecuencia**.  
A través de este análisis exploratorio de datos (EDA), se pretende descubrir patrones, tendencias y factores que ayuden a explicar este fenómeno y su relación con la actividad humana.

---

## 📊 Descripción y preparación del conjunto de datos

El conjunto de datos recoge información sobre ataques de tiburones ocurridos en distintas partes del mundo, con variables como:

- **Fecha del ataque**  
- **País y ubicación geográfica**  
- **Actividad de la víctima** (surf, natación, pesca, buceo, etc.)  
- **Tipo de ataque** (provocado, no provocado, fatal, no fatal)  
- **Sexo y edad de la víctima**  
- **Fuente o referencia del registro**

Durante la preparación de los datos se realizaron tareas de:

- Eliminación de registros duplicados o incompletos.  
- Limpieza de valores ausentes y corrección de errores.  
- Normalización de nombres de países, actividades y categorías.  
- Conversión de fechas para facilitar el análisis temporal.  

Este proceso garantiza que los datos sean **fiables y coherentes** antes de analizarlos.

---

## 🧠 Hipótesis del estudio

Una vez limpiado y preparado el conjunto de datos, se plantean las siguientes hipótesis para guiar el análisis:

1. **Los ataques de tiburón han aumentado en las últimas décadas.**  
2. **El surf y la natación muestran una incidencia de ataques superior a la de otras actividades.**  
3. **Los ataques afectan mayoritariamente a hombres.**  
4. **Las actividades de buceo o pesca submarina presentan una mayor tasa de mortalidad que otras actividades.**  
5. **En Australia los ataques fatales son más frecuentes que en el resto de países.**

---

## 🔍 Análisis exploratorio

El análisis se organiza en diferentes fases:

### 1. Análisis general
- Revisión del número total de ataques y su distribución por país, año y tipo de actividad.  
- Identificación de los valores más altos y posibles anomalías.  

### 2. Análisis temporal
- Evolución de los ataques a lo largo de los años.  
- Identificación de tendencias crecientes o cambios relevantes por décadas.  

### 3. Análisis geográfico
- Comparación por países y regiones.  
- Visualizaciones que muestran las zonas con mayor concentración de ataques.  

### 4. Análisis por actividad y tipo de ataque
- Relación entre la actividad realizada por la víctima y la probabilidad de ataque.  
- Comparación entre ataques fatales y no fatales.  

### 5. Análisis por características de la víctima
- Distribución por sexo y edad.  
- Relación entre estas variables y el tipo o gravedad del ataque.  

---

## 📈 Resultados principales

A partir del análisis realizado, se observan los siguientes hallazgos:

- Los países con más ataques registrados son **Australia, Estados Unidos y Sudáfrica**.  
- El número de ataques **ha aumentado con los años**, coincidiendo con un mayor turismo y actividades acuáticas.  
- Las **actividades recreativas**, especialmente el **surf y la natación**, presentan un mayor número de incidentes.  
- Los ataques afectan con mayor frecuencia a **hombres**, según la distribución por sexo.  
- Las actividades de **buceo y pesca submarina** muestran una proporción más elevada de ataques **fatales**.  

---

## 🧩 Conclusiones

El estudio muestra que los ataques de tiburón, aunque generan mucha atención mediática, **son poco frecuentes** en comparación con la cantidad de personas que realizan actividades en el mar.  
Aun así, los datos permiten ver ciertos patrones:

- Los ataques ocurren **con más frecuencia en zonas costeras turísticas** y en **épocas del año con mayor afluencia de bañistas**, como los meses de verano.  
- Se relacionan sobre todo con **actividades recreativas** como el surf o la natación.  
- La mayoría de los ataques **no son graves ni fatales**, lo que indica que estos sucesos siguen siendo excepcionales.  
- Las actividades como el **buceo o la pesca submarina** muestran una mayor proporción de casos fatales, posiblemente por las condiciones en las que se realizan.  
- En países como **Australia** se observa una mayor presencia relativa de ataques graves o fatales.

Estas conclusiones se fundamentan en los patrones visuales y numéricos del análisis, y ayudan a **entender mejor por qué y dónde se producen estos incidentes**.  
También pueden servir para **mejorar la prevención y la educación pública**, promoviendo una relación más segura y consciente entre las personas y el entorno marino.

---

## ⚙️ Tecnologías utilizadas

- **Python 3**  
- **Pandas** → limpieza y manipulación de datos  
- **Matplotlib** y **Seaborn** → visualización  
- **Jupyter Notebook** → desarrollo del análisis  

---

## 📚 Fuente de los datos

Los datos utilizados proceden del conjunto público **[Shark Attacks Dataset](https://www.kaggle.com/datasets/gauravkumar2525/shark-attacks/data)**, disponible en **Kaggle**, compartido por el usuario *Gaurav Kumar*.

---
