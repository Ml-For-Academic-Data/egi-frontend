from flask import Flask, redirect
import threading
import panel as pn
from app.main import serve_panel

app = Flask(__name__)

# Iniciar el servidor de Panel en segundo plano
def launch_panel():
    pn.serve(
        {'Dashboard': serve_panel},
        port=55265,      # Podés cambiar este puerto si está ocupado
        show=False,      # Evita abrir una pestaña del navegador automáticamente
        threaded=True
    )

# Lanzar el servidor Panel en un hilo separado
threading.Thread(target=launch_panel).start()

@app.route('/')
def index():
    return redirect('http://localhost:55265')

@app.route('/dashboard')
def dashboard_info():
    return "Dashboard corriendo en <a href='http://localhost:55265'>http://localhost:55265</a>"

if __name__ == '__main__':
    app.run()
