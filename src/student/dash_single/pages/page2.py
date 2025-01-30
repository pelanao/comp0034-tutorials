
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

dash.register_page(__name__)


# Image object row 4
djo = html.Img(src='https://external-preview.redd.it/LGnb1tF60_4GoE6xQnHW2h73h_ps-zhH5__0eeq7uoY.jpg?width=640&crop=smart&auto=webp&s=05ef0aa3d17d7e9691ebdccfc3a2732cae81381a', 
               alt='joekeery',
               className="img-fluid")

even_w = 6 # when an evenly distributed width is required
row_two = dbc.Row([
    dbc.Col([   # column 1
        html.H1('Column 1:2'),
        djo,
        ],
        width = even_w
    ),
        dbc.Col([   # column 1
        html.H1('Column 2:2'),
        djo,
        ],
        width = even_w
    ),
])



layout = dbc.Container(
    [
    row_two,
    ]
)
