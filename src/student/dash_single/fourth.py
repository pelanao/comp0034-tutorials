# 12 column layout
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

# width is not necessary as it defaults to 12
row_one = dbc.Row([
    html.H1("Paralympics Data Analytics"),
    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida."),
])



# Dropdown component for Row 2
drop_down = dbc.Select(
    options=[
        {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events",  # The default selection
    id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
),

# Check boxes component in Row 2
check_boxes = html.Div(
    [
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],  # Values is a list as you can select 1 AND 2
            id="checklist-input",
        ),
    ]
)


# width is necessary as components are not evenly distributed
row_two = dbc.Row([
    dbc.Col(children=drop_down, width=4),
    dbc.Col(children=check_boxes, width={"size": 4, "offset": 2}), # 2 'empty' columns between this and the previous column
])



# Image object in Row 3
html.Img(src=app.get_asset_url('line-chart-placeholder.png'), alt='bar chart'),




# width is not necessary as it is evenly distributed between two components
row_three = dbc.Row([
    dbc.Col(children=['Line chart... now test the width of the column by adding a lot of text to see overflow']),
    dbc.Col(children=['Bar chart... now test the width of the column by adding a lot of text to see overflow'])
])

# width is necessary as components are not evenly distributed
row_four = dbc.Row([
    dbc.Col(children=['World map... now test the width of the column by adding a lot of text to see overflow and add a little more as the width of 8 is very wide'], width=8),
    dbc.Col(children=['Card with event info... now test the width of the column by adding a lot of text'], width=4),
])

row_five = dbc.Row([
    dbc.Col('1', width=1),
    dbc.Col('2', width=1),
    dbc.Col('3', width=1),
    dbc.Col('4', width=1),
    dbc.Col('5', width=1),
    dbc.Col('6', width=1),
    dbc.Col('7', width=1),
    dbc.Col('8', width=1),
    dbc.Col('9', width=1),
    dbc.Col('10', width=1),
    dbc.Col('11', width=1),
    dbc.Col('12', width=1),
    dbc.Col('13', width=1)
])

app.layout = dbc.Container([
    row_one,
    row_two,
    dbc.Row('.'),
    row_three,
    dbc.Row('.'),
    row_four,
    dbc.Row('.'),
    row_five,
    dbc.Row('.'),
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)