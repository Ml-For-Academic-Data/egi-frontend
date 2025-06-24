from flask import Flask, render_template, redirect, jsonify

# Crear instancia de la aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    """Página principal con enlaces a las aplicaciones"""
    # Renderizar template HTML que actúa como hub central
    return render_template('index.html')

@app.route("/airflow")
def airflow_redirect():
    """Redirige a Airflow"""
    # Redirección directa al puerto de Airflow para acceso sin proxy
    return redirect("http://localhost:8080")

@app.route("/panel")
def panel_redirect():
    """Redirige a Panel Dashboard"""
    # Redirección directa al puerto de Panel para acceso sin proxy
    return redirect("http://localhost:5000")

@app.route("/health")
def health_check():
    """Health check para Docker"""
    # Endpoint estándar para verificar el estado del servicio
    return jsonify({
        "status": "healthy",
        "service": "egi-frontend",
        "message": "Frontend funcionando sin autenticación"
    })

@app.route("/info")
def info():
    """Información del sistema"""
    # Endpoint informativo que documenta los servicios disponibles
    return jsonify({
        "frontend": "EGI ML Platform",
        "version": "1.0",
        "apps_disponibles": {
            "airflow": "http://localhost:8080",
            "panel": "http://localhost:5000"
        },
        "autenticacion": "Deshabilitada (desarrollo)"
    })

if __name__ == "__main__":
    # Información de inicio mostrando estructura de la aplicación
    print("🚀 EGI ML Platform Frontend")
    print("📋 Aplicaciones disponibles:")
    print("   - Airflow: /airflow")
    print("   - Panel: /panel")
    print("🔍 Endpoints útiles:")
    print("   - Health: /health")
    print("   - Info: /info")

    # Ejecutar servidor Flask en modo desarrollo con acceso externo
    app.run(debug=True, host="0.0.0.0", port=3000)
