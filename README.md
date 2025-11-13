# 🦈 Análisis Exploratorio de Datos: Ataques de Tiburón en el Mundo

## 📖 Objetivo principal del análisis

El objetivo principal de este proyecto es **analizar los ataques de tiburón registrados en todo el mundo**, buscando entender **dónde, cuándo y por qué ocurren con mayor frecuencia**.  
A través de este análisis exploratorio de datos (EDA), se pretende descubrir patrones, tendencias y factores que expliquen mejor este fenómeno natural y su relación con la actividad humana.

---

## 📊 Descripción y preparación del conjunto de datos

El conjunto de datos recoge información sobre ataques de tiburones ocurridos en distintas partes del mundo, con variables como:

- **Fecha del ataque**  
- **País y ubicación geográfica**  
- **Actividad de la víctima** (surf, natación, pesca, buceo, etc.)  
- **Tipo de ataque** (provocado, no provocado, fatal, no fatal)  
- **Especie de tiburón involucrada**  
- **Sexo y edad de la víctima**  
- **Fuente o referencia del registro**

Durante la preparación de los datos se realizaron tareas de:
- Eliminación de registros duplicados o incompletos.  
- Limpieza de valores ausentes y corrección de errores.  
- Normalización de nombres de países, actividades y especies.  
- Conversión de fechas para facilitar el análisis temporal.  

Este proceso garantiza que los datos sean **fiables y coherentes** antes de analizarlos.

---

## 🧠 Hipótesis del estudio

Después de revisar y limpiar los datos, se plantean las siguientes hipótesis para guiar el análisis:

1. Los ataques de tiburón se concentran principalmente en **zonas costeras con gran actividad acuática**, como Australia, Estados Unidos y Sudáfrica.  
2. El número de ataques ha **aumentado con el paso de los años**, en parte por el crecimiento del turismo y los deportes acuáticos.  
3. Actividades como el **surf y la natación** presentan un **mayor riesgo de ataque** que la pesca o el buceo.  
4. Las especies **tiburón blanco, tigre y toro** son las más implicadas en los incidentes registrados.  
5. La mayoría de los ataques **no son fatales**, aunque su gravedad puede variar según la actividad y la región.

---

## 🔍 Análisis exploratorio

El análisis se organiza en diferentes fases:

### 1. Análisis general
- Revisión del número total de ataques y su distribución por país, año y tipo de actividad.  
- Identificación de los valores más altos y posibles anomalías.  

### 2. Análisis temporal
- Evolución de los ataques a lo largo de los años.  
- Detección de posibles aumentos en determinadas décadas o meses del año.  

### 3. Análisis geográfico
- Comparación por regiones y países.  
- Mapas o gráficos que muestran las zonas con mayor concentración de ataques.  

### 4. Análisis por actividad y tipo de ataque
- Relación entre el tipo de actividad y el número de incidentes.  
- Diferencias entre ataques fatales y no fatales.  

### 5. Análisis por especie
- Frecuencia de ataques según especie de tiburón.  
- Comparación entre especies y tipo de ataque.  

---

## 📈 Resultados principales

A partir de los análisis realizados, se observan los siguientes resultados:

- Los **países con más ataques** registrados son **Australia, Estados Unidos y Sudáfrica**.  
- El número de ataques **ha ido aumentando con los años**, probablemente por una mayor exposición y mejor registro de los incidentes.  
- Las **actividades acuáticas recreativas**, especialmente el **surf y la natación**, son las más relacionadas con los ataques.  
- Las especies **tiburón blanco, tigre y toro** son las que más aparecen en los registros.  
- La mayoría de los ataques **no resultan fatales**.  

---

## 🧩 Conclusiones

El estudio muestra que los ataques de tiburón, aunque llaman mucho la atención en los medios, **son poco frecuentes** si los comparamos con la cantidad de personas que realizan actividades en el mar.  
Aun así, el análisis de los datos permite ver algunos patrones claros:

- Los ataques ocurren **con más frecuencia en zonas costeras turísticas** y en **épocas del año con más bañistas o surfistas**, como los meses de verano.  
- Están relacionados sobre todo con **algunas especies de tiburones**, como el **blanco, el tigre y el toro**, y con **actividades recreativas** como el surf o la natación.  
- La mayoría de los ataques **no son graves ni fatales**, lo que muestra que estos incidentes son excepcionales.

Estas conclusiones se basan en lo que muestran los gráficos y las cifras del análisis: las zonas, las especies y las actividades con más registros de ataques.

En resumen, los resultados ayudan a **entender mejor por qué y dónde se producen estos incidentes** y pueden servir para **mejorar la prevención y la educación pública**, promoviendo una relación más segura y consciente entre las personas y los tiburones.

---

## ⚙️ Tecnologías utilizadas

- **Python 3**  
- **Pandas** → Limpieza y manipulación de datos  
- **Matplotlib** y **Seaborn** → Visualización de datos  
- **Jupyter Notebook** → Desarrollo del análisis y documentación  

---

## 📚 Fuente de los datos

Los datos utilizados proceden del conjunto público **[Shark Attacks Dataset](https://www.kaggle.com/datasets/gauravkumar2525/shark-attacks/data)**, disponible en **Kaggle**, creado y compartido por el usuario *Gaurav Kumar*.
