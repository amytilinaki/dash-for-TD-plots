from dash import html, dcc
from dash.dependencies import Input, Output
from pages2.home import create_page_home
from pages2.page_2 import create_page_2
from pages2.page_3 import create_page_3
from pages2.page_4 import create_page_4
from app import app1
import sys
import settings

server = app1.server
app1.config.suppress_callback_exceptions = True

app1.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app1.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return create_page_2()
    if pathname == '/page-3':
        return create_page_3()
    if pathname == '/page-4':
        return create_page_4()
    else:
        return create_page_home()

if __name__ == '__main__':

    print(sys.argv)
    settings.data_path = sys.argv[1]
    
    app1.run_server(debug=True)