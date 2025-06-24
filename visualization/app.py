import pandas as pd
import panel as pn
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Habilitar extensión de Plotly en Panel para gráficos interactivos
pn.extension('plotly')

# Cargar dataset procesado
df = pd.read_csv('/opt/airflow/data/processed/cleaned_data.csv')

# Definir columnas categóricas disponibles para análisis
categorical_columns = [
    'Marital status', 'Application mode', 'Course', 'Gender', 'Target'
]

# Obtener rango completo de edades para el slider
min_age, max_age = df['Age at enrollment'].min(), df['Age at enrollment'].max()

# Crear widgets interactivos para controlar las visualizaciones
var_select = pn.widgets.Select(name='Variable categórica', options=categorical_columns, value=categorical_columns[0])
age_slider = pn.widgets.IntRangeSlider(name='Rango de edad', start=min_age, end=max_age, value=(min_age, max_age))

# Función reactiva que genera histograma basado en selecciones del usuario
@pn.depends(var_select, age_slider)
def plot_histogram(variable, age_range):
    # Filtrar datos según rango de edad seleccionado
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    # Crear histograma agrupado por variable Target
    fig = px.histogram(dff, x=variable, color='Target', barmode='group', title=f'Histograma de {variable} por Target')
    return fig

# Función reactiva para boxplot de edad vs variable categórica
@pn.depends(var_select, age_slider)
def plot_boxplot(variable, age_range):
    # Filtrar datos por rango de edad
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    plt.figure(figsize=(8,4))
    # Crear boxplot para mostrar distribución de edad por categoría
    sns.boxplot(x=variable, y='Age at enrollment', data=dff)
    plt.title(f'Boxplot de Edad según {variable}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.close()
    # Convertir figura matplotlib a componente Panel
    return pn.pane.Matplotlib(plt.gcf(), dpi=144)

# Función reactiva para matriz de correlación de variables numéricas
@pn.depends(age_slider)
def plot_corr_matrix(age_range):
    # Filtrar datos por edad
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    # Seleccionar solo columnas numéricas para correlación
    numeric_cols = dff.select_dtypes(include='number').columns
    corr = dff[numeric_cols].corr()
    plt.figure(figsize=(7,7))
    # Crear heatmap de correlaciones con valores anotados
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title('Matriz de Correlación (variables numéricas)')
    plt.tight_layout()
    plt.close()
    return pn.pane.Matplotlib(plt.gcf(), dpi=144)

# Estructura del dashboard: título, controles y gráficos organizados
dashboard = pn.Column(
    "# Dashboard Interactivo de Dataset",
    pn.Row(
        # Panel izquierdo con controles
        pn.Column(var_select, age_slider, width=300),
        # Panel derecho con gráficos que responden a los controles
        pn.Column(plot_histogram, plot_boxplot)
    ),
    # Matriz de correlación en la parte inferior
    plot_corr_matrix
)

# Hacer el dashboard servible como aplicación web
dashboard.servable()
