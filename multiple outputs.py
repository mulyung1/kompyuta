from dash import Dash, dcc, html, callback, Output, Input

#import style
stail=['https://codepen.io/chriddyp/pen/bWLwgP.css']
#initialise app and incoporate css
app=Dash(__name__,external_stylesheets=stail)

#define app layout
app.layout=html.Div([
    dcc.Input(
        type='number',
        id='chatbox',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')])
    ]),
    
])
#callback decorator to connect the inputs and outputs. 
@callback(
    Output('square','children'),
    Output('cube','children'),
    Output('twos','children'),
    Output('threes','children'),
    Output('x^x','children'),
    Input('chatbox', 'value')
)

def updateApp(x):
    #computation happens here
    return x**2, x**3, 2**x, 3**x, x**x

#run the app
if __name__ == '__main__':
    app.run(debug=True)


