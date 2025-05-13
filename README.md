# Dashboard de Análisis de Deserción Estudiantil

## 📌 Descripción
Este proyecto utiliza técnicas de clustering (KMeans, DBSCAN y GMM) para identificar grupos de estudiantes con riesgo de deserción basándose en:
- **Edad**
- **Promedio académico**
- **Asistencia**
- **Participación en actividades extracurriculares**
- **Horas de estudio**

## 🛠️ Instalación
1. **Requisitos**:
   ```bash
   pip install pandas numpy scikit-learn panel hvplot

## 🖥️ Uso del Dashboard

1. **Selección de modelo**:

    - ***Elige entre KMeans, DBSCAN o GMM usando los botones radiales***

2. **Visualizaciones principales**:

    - ***Gráfico de dispersión: Muestra la relación entre promedio y asistencia, coloreado por grupo***

    - ***Métricas de evaluación: Silhouette, Calinski-Harabasz y Davies-Bouldin***

3. **Análisis avanzado (pestañas inferiores)**:

- 📊 ***Tasa de deserción: Barras que muestran el % de deserción por grupo.***

- 🔥 ***Correlaciones: Heatmap de cómo cada variable se relaciona con la deserción en cada grupo.***

- 📦 ***Distribuciones: Boxplots comparativos de variables clave entre grupos.***

- 📋 ***Estadísticas: Medias, medianas y desviaciones estándar por grupo.***

## 🔍 Interpretación de Resultados

**Identificación de grupos de riesgo**

1. **Grupo de alto riesgo**:

- ***Alta tasa de deserción en el gráfico de barras.***

- ***Bajo promedio y asistencia en el scatter plot.***

- ***Correlaciones negativas fuertes con variables académicas en el heatmap.***

2. **Grupo de bajo riesgo**:

- ***Tasa de deserción cercana a 0.***

- ***Valores altos en promedio/asistencia.***

- ***Participación frecuente en actividades extracurriculares.***

## 🤖 Cómo contribuir

- **Reportar issues con datos o visualizaciones**

- **Sugerir nuevas variables predictivas**

- **Mejorar la documentación**