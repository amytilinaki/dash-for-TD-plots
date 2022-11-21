from dash import Dash,html,dcc,callback
from dash.dependencies import Input, Output
from navbar import create_navbar
import numpy as np
from processing import mult_graphs
import plotly.express as px


def create_page_3():
    nav = create_navbar()
    layout = html.Div(children=[ 
            html.H1(children='Wavefront and FFT of Different Channels'),

            
            html.Div(id='dd-output-container'),

            dcc.Checklist(
                    id="checklist",
                        options=[
                        {"label":"Baseline Reduction", "value":"Yes"}
                    
                        ],
                        labelStyle={"display": "block"},
                        value=["Yes"],
                    ),

            dcc.Dropdown(options=[{'label': "Channel %s" %i, 'value': i} for i in np.arange(0,2560)],multi=True,id='dropdown'),

            dcc.Graph(id="wavefront"),
            dcc.Graph(id="fft")   

            ]
        
        )

    return nav,layout


@callback(Output('wavefront', 'figure'),Output('fft','figure'),
                [Input(component_id='dropdown', component_property='value'),Input(component_id='checklist',component_property='value')])
    
def select_graph(dropdown,checklist):

    if dropdown==None:
        fig1=mult_graphs([],1)[0]
        fig2=mult_graphs([],1)[1]
        return fig1,fig2

    elif dropdown and checklist:
        fig=mult_graphs(dropdown,1)[0]
        fig2=mult_graphs(dropdown,1)[1]
        return fig,fig2

    else:
        fig=mult_graphs(dropdown,0)[0]
        fig2=mult_graphs(dropdown,0)[1]
        return fig,fig2
