# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc


# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]


# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.CERULEAN]  # or another theme like DARKLY, CYBORG, etc.


# Pass the stylesheet and meta_tag variables to the Dash app constructor
# Create an instance of the Dash app with the stylesheet and meta tag
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)


# Wrap the layout in a Bootstrap container
app.layout = dbc.Card([
    # Add the HTML layout components in here
    dbc.CardFooter([
        html.Div(children=[
            html.H1('A first heading'),
            html.H3("The page's subheading"),
            html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), alt='bar chart'),
            html.H4('Heading 4 test')
        ])
    ]),

    dbc.Row([
        dbc.Col(html.H3('This is a column'), width=4),
        dbc.Col(html.H5('This is another column'), width=8),
    ])
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)