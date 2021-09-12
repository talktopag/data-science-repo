import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import plotly_express as px

conn = create_engine('sqlite:///assets/operations.db')
raw_materials = pd.read_sql('SELECT * FROM raw_materials', conn)
qc_test = pd.read_sql('SELECT * FROM qc_test', conn)

app = dash.Dash(__name__)


fig = px.line(x = [1,2,3,4], y = [1,2,3,4])

app.layout = html.Div(children = [
    html.H1('OMG! It\'s a Dash app.'),
    dcc.Graph(figure = fig, id = 'line-plot')
])

if __name__ == '__main__':
    app.run_server(debug = True)