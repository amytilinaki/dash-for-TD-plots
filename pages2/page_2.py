from dash import html
from navbar import create_navbar
from dash import Dash,html,dcc
from navbar import create_navbar
from processing import mean_std

def create_page_2():
    nav = create_navbar()
    layout=(
    html.Div(children=[  
    html.H1(children='Mean and Standard Deviation of ADC Values'),

   
    dcc.Graph(id="mean",figure=mean_std()[0]),

    dcc.Graph(id="std",figure=mean_std()[1])
    ]
))

    return nav,layout