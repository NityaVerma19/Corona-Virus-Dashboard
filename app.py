
import pandas as pd
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc

from dash.dependencies import Input,Output

#external CSS stylesheets

external_stylesheets = [
     {
         'href' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
         'rel' : 'stylesheet',
         'integrity' : 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
         'crossorigin' : 'anonymous'

     }

]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


app.layout = html.Div([
    html.H1("Corona Virus Pandemic", style = {'color' : '#fff' , 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total cases" , className='text-light'), #for white text
                    html.H4('600', className= 'text-light')
                ], className= 'card-body')
            ] , className= 'card bg-danger')
        ] , className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active cases", className='text-light'),  # for white text
                    html.H4('634', className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ] , className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className='text-light'),  # for white text
                    html.H4('18', className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className='text-light'),  # for white text
                    html.H4('11', className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ] , className= 'col-md-3')
    ], className= 'row'),
    html.Div([],className= 'row'),
    html.Div([], className= 'row')
], className= 'container')                  #the outermost division

if __name__ == '__main__':
    app.run_server(debug = True , port = 5000)


