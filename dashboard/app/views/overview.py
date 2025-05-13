import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import panel as pn
import hvplot.pandas

# Cargar y preparar datos
df = pd.read_csv("student_data.csv")
features = ['edad', 'promedio', 'asistencia', 'actividad_extra', 'horas_estudio']
X = StandardScaler().fit_transform(df[features])


# Modelos y métricas
def run_models(X):
    results = {}

    # KMeans
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    labels_kmeans = kmeans.labels_
    results['KMeans'] = {
        'labels': labels_kmeans,
        'Silhouette': silhouette_score(X, labels_kmeans),
        'Calinski': calinski_harabasz_score(X, labels_kmeans),
        'Davies': davies_bouldin_score(X, labels_kmeans)
    }

    # DBSCAN
    dbscan = DBSCAN(eps=1.5, min_samples=5).fit(X)
    labels_dbscan = dbscan.labels_
    if len(set(labels_dbscan)) > 1:
        results['DBSCAN'] = {
            'labels': labels_dbscan,
            'Silhouette': silhouette_score(X, labels_dbscan),
            'Calinski': calinski_harabasz_score(X, labels_dbscan),
            'Davies': davies_bouldin_score(X, labels_dbscan)
        }

    # GMM
    gmm = GaussianMixture(n_components=3, random_state=42).fit(X)
    labels_gmm = gmm.predict(X)
    results['GMM'] = {
        'labels': labels_gmm,
        'Silhouette': silhouette_score(X, labels_gmm),
        'Calinski': calinski_harabasz_score(X, labels_gmm),
        'Davies': davies_bouldin_score(X, labels_gmm)
    }

    return results


results = run_models(X)
model_selector = pn.widgets.RadioButtonGroup(name='Modelo', options=list(results.keys()), button_type='success')


# Componente original
@pn.depends(model_selector)
def update_dashboard(model):
    df_plot = df.copy()
    df_plot['cluster'] = results[model]['labels']

    mean_values = df_plot.groupby('cluster')[features + ['desercion']].mean().round(2)
    table = mean_values.reset_index().rename(columns={'cluster': 'Grupo'})

    plot = df_plot.hvplot.scatter(
        x='promedio',
        y='asistencia',
        c='cluster',
        cmap='Category10',
        size=100,
        alpha=0.6,
        title=f'Clustering usando {model}'
    )

    metrics = results[model]
    metric_table = pn.pane.Markdown(f"""
    **Métricas de Evaluación:**
    - Silhouette Score: {metrics['Silhouette']:.2f}
    - Calinski-Harabasz Score: {metrics['Calinski']:.2f}
    - Davies-Bouldin Score: {metrics['Davies']:.2f}
    """)

    return pn.Column(metric_table, plot, pn.pane.DataFrame(table, width=800))


@pn.depends(model_selector)
def add_desertion_bar_plot(model):
    df_plot = df.copy()
    df_plot['cluster'] = results[model]['labels']
    deserction_rate = df_plot.groupby('cluster')['desercion'].mean().reset_index()
    bar_plot = deserction_rate.hvplot.bar(
        x='cluster',
        y='desercion',
        title=f'Tasa de Deserción por Grupo ({model})',
        ylim=(0, 1),
        color='cluster',
        cmap='Category10'
    )
    return bar_plot


@pn.depends(model_selector)
def add_correlation_heatmap(model):
    df_plot = df.copy()
    df_plot['cluster'] = results[model]['labels']
    cluster_corr = df_plot.groupby('cluster')[features + ['desercion']].corr().loc[:, 'desercion'].unstack(level=0)
    heatmap = cluster_corr.hvplot.heatmap(
        title=f'Correlación con Deserción por Grupo ({model})',
        cmap='coolwarm',
        clim=(-1, 1)
    )
    return heatmap


@pn.depends(model_selector)
def add_boxplots(model):
    df_plot = df.copy()
    df_plot['cluster'] = results[model]['labels']
    boxplots = pn.Row(*[
        df_plot.hvplot.box(
            y=feature,
            by='cluster',
            title=f'Distribución de {feature} por Grupo',
            width=300,
            height=300
        ) for feature in features
    ])
    return boxplots


@pn.depends(model_selector)
def add_summary_table(model):
    df_plot = df.copy()
    df_plot['cluster'] = results[model]['labels']
    summary = df_plot.groupby('cluster')[features + ['desercion']].agg(['mean', 'median', 'std']).round(2)
    return pn.pane.DataFrame(summary, width=1000)


# Dashboard extendido
extended_dashboard = pn.Column(
    "# Dashboard de Deserción Estudiantil",
    "Selecciona un modelo para visualizar los clústers generados y sus características:",
    model_selector,
    update_dashboard,
    pn.layout.Divider(),
    "## Análisis Detallado por Grupo",
    pn.Tabs(
        ("Tasa de Deserción", add_desertion_bar_plot),
        ("Correlación con Variables", add_correlation_heatmap),
        ("Distribución de Variables", add_boxplots),
        ("Estadísticas Descriptivas", add_summary_table)
    )
)


def view():
    return extended_dashboard


pn.extension()