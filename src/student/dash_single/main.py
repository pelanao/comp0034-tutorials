from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc


# Create an instance of the Dash app

# Dash app constructor
app = Dash(__name__, use_pages=True)


app.layout = html.Div(
    [
        # main app framework
        html.Div("Djo no tickets left", style={'fontSize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)