import asyncio
from reactpy import component, web, html, run
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material", fallback="")
Container = web.export(mui, "Container")
Grid = web.export(mui, "Grid")
Paper = web.export(mui, "Paper")
Box = web.export(mui, "Box")
Typography = web.export(mui, "Typography")
Rating = web.export(mui, "Rating")


def tarjetas():
    def tarjeta(producto):
        return Grid(
            {"item": True, "sm": 6, "md": 4, "lg": 3},
            Paper(
                {"elevation": 4},
                html.img(
                    {
                        "src": f"https://picsum.photos/id/{producto['id']}/400/100",
                        "className": "img-fluid",
                        "style": {
                            "width": "100%",
                            "height": "5rem",
                            "borderRadius": "8px",
                        },
                    }
                ),
            ),
            Box(
                {"sx": {"bgcolor": "background.paper"}},
                Typography(
                    {"variant": "h1"},
                    producto["nombre"],
                ),
                Rating(
                    {
                        "readOnly": True,
                        "name": "half-rating",
                        "precision": "0.5",
                        "value": producto["rating"],
                    },
                ),
                Typography(
                    {"variant": "body2"},
                    producto["descripcion"],
                ),
                Typography(
                    {"variant": "h5"},
                    producto["precio"],
                ),
            ),
        )

    return Grid(
        {"container": True, "spacing": "8"},
        *[tarjeta(producto) for producto in productos],
    )


@component
def App():
    return Container(
        {"maxWidth": "md"},
        Grid(
            {"container": True, "spacing": 2},
            tarjetas(),
        ),
    )


app = Flask(__name__)
configure(app, App)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # Ejecuta la aplicación Flask en el puerto 5000
