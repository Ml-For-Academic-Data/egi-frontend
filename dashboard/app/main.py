# app/main.py
from panel.template import FastListTemplate
import panel as pn
from app.views import overview

theme_toggle = pn.widgets.Toggle(name='Modo Oscuro')

pn.extension()

def serve_panel():
    theme = "dark" if theme_toggle.value else "default"

    template = FastListTemplate(
        title="Dashboard de Deserción Estudiantil",
        theme=theme,
        sidebar=[
            pn.pane.Markdown("## Menú"),
            pn.widgets.Button(name="Actualizar"),
        ],
        main=[overview.view()],
    )

    return template.servable()