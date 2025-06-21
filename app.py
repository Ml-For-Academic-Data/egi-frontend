from flask import Flask, render_template, redirect, jsonify
import os

app = Flask(__name__)

# Obtener URLs de variables de entorno o usar valores por defecto para desarrollo
AIRFLOW_URL = os.getenv("AIRFLOW_URL", "http://localhost:8080")
PANEL_URL = os.getenv("PANEL_URL", "http://localhost:5000")

@app.route("/")
def home():
    """Página principal con enlaces a las aplicaciones"""
    return render_template('index.html')

@app.route("/airflow")
def airflow_redirect():
    """Redirige a Airflow"""
    # En desarrollo: redirige al puerto directo de Airflow
    return redirect(AIRFLOW_URL)

@app.route("/panel")
def panel_redirect():
    """Redirige a Panel Dashboard"""
    # En desarrollo: redirige al puerto directo de Panel
    return redirect(PANEL_URL)

@app.route("/health")
def health_check():
    """Health check para Docker"""
    return jsonify({
        "status": "healthy",
        "service": "egi-frontend",
        "message": "Frontend funcionando sin autenticación"
    })

@app.route("/info")
def info():
    """Información del sistema"""
    return jsonify({
        "frontend": "EGI ML Platform",
        "version": "1.0",
        "apps_disponibles": {
            "airflow": AIRFLOW_URL,
            "panel": PANEL_URL
        },
        "autenticacion": "Deshabilitada (desarrollo)"
    })

if __name__ == "__main__":
    print("🚀 EGI ML Platform Frontend")
    print("📋 Aplicaciones disponibles:")
    print(f"   - Airflow: {AIRFLOW_URL}")
    print(f"   - Panel: {PANEL_URL}")
    print("🔍 Endpoints útiles:")
    print("   - Health: /health")
    print("   - Info: /info")
    app.run(debug=True, host="0.0.0.0", port=3000)