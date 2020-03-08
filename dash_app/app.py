import os
from typing import List
import requests
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H2("Search Engine"),
                dcc.Input(id='search-input', type='search', className="u-full-width"),
                html.Button('Search', id='search-button')
            ],
            style={
                'textAlign': 'center'
            }
        ),
        html.Div(id='search-output')
    ]

)


@app.callback(
    Output(component_id='search-output', component_property='children'),
    [Input('search-button', 'n_clicks')],
    [State(component_id='search-input', component_property='value')]
)
def update_output_div(n_clicks, input_text) -> List:
    if not input_text:
        return []
    res = requests.get(url=os.environ['QUERIER_API_BASE_URL'] + '/query', params={"text": input_text})
    return querier_res_to_components(res.json())


style = {
    "border-radius": "10px",
    "padding": "10px",
    "margin-top": "10px",
    "box-shadow": "0px 0px 50px 0px rgba(250,250,250,1)"
}


def querier_res_to_components(res: List):
    results = []
    for result in res:
        results.append(
            html.Div(
                html.A(result['title'], href=result['url']),
                style=style
            )
        )

    return results


if __name__ == '__main__':
    app.run_server(debug=False,host= "0.0.0.0", port=8050)
