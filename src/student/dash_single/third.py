# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc


# Define a variable that contains the meta tags
# the viewport is set to a responsive width with an initial scale of 1
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]


# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.CERULEAN]  # or another theme like DARKLY, CYBORG, etc.


# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)


# Wrap the layout in a Bootstrap container
# 12 column-layout
app.layout = dbc.Container([
    # Add the HTML layout components in here
    html.H1('Hola people'),
    html.H2('Hola mundo'),
    html.H3('bad bunny beibe'),
    dbc.Container("hombre que guay")
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8080)