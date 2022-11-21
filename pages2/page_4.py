from dash import Dash,html,dcc,callback
from dash.dependencies import Input, Output
from navbar import create_navbar
from processing import td_2d

def create_page_4():

    nav = create_navbar()
    layout = html.Div(children=[  
    html.H1(children='Channel vs Time with Overlayed TPs'),

    dcc.Checklist(
                    id="checklist",
                    options=[
                        {"label":"TPs", "value":"Yes"}
                
                    ],
                    labelStyle={"display": "block"},
                    value=["Yes"],
                ),

                dcc.Graph(id='graph'),
            ]
    )
    return nav,layout

@callback(Output("graph","figure"), Input("checklist","value"))

def change_values(value):

    if value:
        return td_2d()[1]
    if not value:
        return td_2d()[0]
    else: 
        []
    


