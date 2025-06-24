# 🎯 EGI ML Platform

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

Una plataforma completa de Machine Learning que integra orquestación de workflows, visualizaciones interactivas y gestión de datos para proyectos de ML/AI.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Arquitectura](#️-arquitectura)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Servicios](#-servicios)
- [Desarrollo](#-desarrollo)
- [API Reference](#-api-reference)

## ✨ Características

- **🔄 Orquestación de Workflows**: Integración con Apache Airflow para pipelines de ML
- **📊 Dashboards Interactivos**: Visualizaciones en tiempo real con Panel y Plotly
- **🐳 Arquitectura Dockerizada**: Despliegue fácil y escalable
- **🎨 Frontend Moderno**: Interfaz web responsive con Flask
- **📈 Análisis de Datos**: Herramientas integradas para exploración y visualización
- **⚡ Hot Reload**: Desarrollo ágil con recarga automática

## 🏗️ Arquitectura

```
EGI ML Platform/
├── 🌐 Frontend (Flask)     # Portal web principal
├── 📊 Panel App (Panel)    # Dashboards interactivos  
├── 🔄 Airflow             # Orquestación de workflows
└── 📁 Data Layer         # Almacenamiento de datos
```

### Componentes Principales

| Componente | Puerto | Descripción |
|------------|--------|-------------|
| **Frontend** | 3000 | Portal principal y autenticación |
| **Panel App** | 5000 | Dashboards y visualizaciones |
| **Airflow** | - | Orquestación de pipelines ML |

## 🚀 Instalación

### Prerrequisitos

- Docker y Docker Compose
- Python 3.8+
- Git

### Instalación Rápida

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/egi-ml-platform.git
cd egi-ml-platform
```

2. **Configurar el entorno**
```bash
# Copiar archivo de configuración
cp .env.example .env

# Editar variables de entorno
nano .env
```

3. **Levantar los servicios**
```bash
# Construir e iniciar todos los servicios
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f
```

4. **Verificar instalación**
```bash
# Health check
curl http://localhost:3000/health
```

### Instalación para Desarrollo

```bash
# Clonar con submódulos
git clone --recursive https://github.com/tu-usuario/egi-ml-platform.git

# Instalar dependencias locales
pip install -r requirements.txt

# Configurar pre-commit hooks
pre-commit install
```

## 💻 Uso

### Acceso a la Plataforma

1. **Portal Principal**: http://localhost:3000
   - Punto de entrada principal
   - Sistema de autenticación
   - Enlaces a aplicaciones

2. **Panel de Visualización**: http://localhost:5000
   - Dashboards interactivos
   - Análisis de datos en tiempo real
   - Visualizaciones personalizables

### Flujo de Trabajo Típico

```bash
# 1. Configurar pipeline en Airflow
# Acceder via portal web

# 2. Ejecutar análisis en Panel
# http://localhost:5000

# 3. Revisar resultados y métricas
```

## 🔧 Servicios

### Frontend (Puerto 3000)

Portal principal desarrollado en Flask que proporciona:

- **Autenticación y autorización**
- **Navegación entre servicios**
- **Health checks y monitoring**
- **Control de acceso basado en roles**

**Rutas principales:**
- `/` - Portal principal
- `/panel` - Redirección a dashboards
- `/airflow` - Acceso a Airflow
- `/health` - Estado del sistema

### Panel App (Puerto 5000)

Aplicación de visualización con Panel/Plotly:

- **Dashboards interactivos**
- **Análisis exploratorio de datos**
- **Visualizaciones personalizables**
- **Exportación de reportes**

**Características:**
- Widgets interactivos (sliders, selectors)
- Gráficos actualizables en tiempo real
- Soporte para múltiples tipos de datos
- Matriz de correlación automática

### Airflow Integration

Orquestación de workflows ML:

- **Pipelines ETL automatizados**
- **Entrenamiento de modelos**
- **Programación de tareas**
- **Monitoreo de ejecuciones**

## 🛠️ Desarrollo

### Estructura del Proyecto

```
egi-ml-platform/
├── docker-compose.yml          # Configuración de servicios
├── requirements.txt            # Dependencias Python
├── .gitignore                 # Archivos ignorados
├── templates/                 # Templates HTML
│   ├── index.html            # Portal principal
│   └── access_denied.html    # Página de error
├── visualization/            # Aplicación Panel
│   └── app.py               # Dashboard principal
└── README.md                # Este archivo
```

### Configuración de Desarrollo

1. **Variables de Entorno**
```bash
# .env
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=sqlite:///dev.db
```

2. **Hot Reload**
```bash
# Los cambios se reflejan automáticamente
docker-compose up -d
```

3. **Debugging**
```bash
# Ver logs específicos
docker-compose logs -f frontend
docker-compose logs -f panel-app

# Entrar al contenedor
docker-compose exec frontend bash
```

## 📡 API Reference

### Health Check Endpoints

```http
GET /health
```
Respuesta:
```json
{
  "status": "healthy",
  "timestamp": "2025-06-24T10:30:00Z",
  "services": {
    "frontend": "up",
    "panel": "up",
    "airflow": "up"
  }
}
```

### Authentication Endpoints

```http
POST /oauth2/sign_in
GET /oauth2/sign_out
GET /oauth2/callback
```

## 🐳 Docker

### Comandos Útiles

```bash
# Construir imágenes
docker-compose build

# Reiniciar servicios
docker-compose restart

# Ver estado
docker-compose ps

# Limpiar volúmenes
docker-compose down -v

# Logs específicos
docker-compose logs -f [servicio]
```

### Personalización

Para modificar la configuración:

1. Editar `docker-compose.yml`
2. Reconstruir: `docker-compose build`
3. Reiniciar: `docker-compose up -d`

## 📊 Monitoreo

### Health Checks

La plataforma incluye health checks automáticos:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### Logs

```bash
# Todos los servicios
docker-compose logs -f

# Servicio específico
docker-compose logs -f frontend

# Últimas 100 líneas
docker-compose logs --tail=100 panel-app
```

## 🤝 Contribución

1. **Fork** el proyecto
2. **Crear** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abrir** un Pull Request

## 🔧 Troubleshooting

### Problemas Comunes

**Puerto ocupado:**
```bash
# Verificar puertos en uso
netstat -tlnp | grep :3000

# Cambiar puerto en docker-compose.yml
ports:
  - "3001:3000"  # Puerto alternativo
```

**Volúmenes no compartidos:**
```bash
# Verificar montaje
docker-compose exec frontend ls -la /opt/airflow/data

# Recrear volúmenes
docker-compose down -v
docker-compose up -d
```

**Servicios no accesibles:**
```bash
# Verificar red
docker network ls
docker network inspect egi-ml-platform_internal_network
```
