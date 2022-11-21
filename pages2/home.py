from dash import html
from navbar import create_navbar


def create_page_home():
    nav = create_navbar()

    header = html.H3('Welcome to the home page of the Trigger Data Plots!')
    sub= html.Div("You can navigate through the menu to produce your desired plot.")

    layout = html.Div([
        nav,
        header,
        sub
    ])
    return layout
