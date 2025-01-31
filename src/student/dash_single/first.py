# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc


# CSS Stylesheet
# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.CERULEAN]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Add an HTML layout to the Dash app
# Wrap the layout in a Bootstrap container
app.layout = dbc.Container([
    # Add the HTML layout components in here
    html.H1(children='Hello World'),
    html.P('this is an incredible website with a lot of textr and amazing organisation'),
    html.Img(src='https://myexeed.com/wp-content/uploads/2023/10/11.webp', alt='Python logo', className="img-fluid"),
    html.H1('what a weird image'),
    html.H2('Heading 2 test'),
    html.H3('Heading 3 test'),
    html.H4('Heading 4 test'),
    html.H5('Heading 5 test'),
    html.Div(children= [
        html.H1('A second division heading'),
        html.P('A bit of text'),
        html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Coronavirus._SARS-CoV-2.png/1200px-Coronavirus._SARS-CoV-2.png', alt='Python logo', className="img-fluid")
        ])
])




# Run the app
if __name__ == '__main__':
    app.run(debug=True)