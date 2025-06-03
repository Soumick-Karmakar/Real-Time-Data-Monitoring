import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container([
        # dbc.Row(
        #     html.H1("Interactive Data Visualization Dashboard", className="text-center", style={"color": "white"})
        # ),
        html.Div([
            dbc.Col([
                # Tab for displaying the company name logo and Welcome message
                html.Div(
                    [
                        html.Div([
                            html.Img(src="assets/C_logo.png", style={"width": "10%", "height": "10%"}),
                            html.Img(src="assets/C_Name.png", style={"width": "40%", "height": "40%"})
                        ]),
                        html.Div([
                            html.Div([
                                html.Img(
                                    src="assets/profile_pic.jpg",  # Put your image in the `assets` folder
                                    style={
                                        "height": "150px",
                                        "width": "150px",
                                        "borderRadius": "50%",  # Makes the image circular
                                        "objectFit": "cover",   # Ensures the image fills the circle without distortion
                                        "border": "3px solid #ccc",  # Optional border
                                    }
                                ),
                                html.H3("Soumick")
                            ], style={"textAlign": "center", "padding": "20px"}),

                            html.Div([
                                html.P("Welcome Back!", style={"fontSize": "40px", "color": "#1e223a", "fontWeight": "bold"}),
                            ])
                        ], style ={"display":"flex", "flexDirection": "row", "alignItems": "center"})
                    ]
                )
            ], className="tab"
            ),

            # Options to click on Home and Parameters
            dbc.Col([
                dbc.Button([
                    html.Img(src="assets/home.svg", style={"marginLeft": "30px", "width": "30px", "height": "30px"}),
                    html.P("Home", style={"marginLeft": "40px", "fontSize": "20px", "marginTop": "15px"})
                ], id="home", className="btn", style ={"display":"flex", "flexDirection": "row", "alignItems": "center"}),
                dbc.Button([
                    html.Img(src="assets/parameter.svg", style={"marginLeft": "30px", "width": "30px", "height": "30px"}),
                    html.P("Parameters", style={"marginLeft": "40px", "fontSize": "20px", "marginTop": "15px"})
                ], id="parameter", className="btn", style ={"display":"flex", "flexDirection": "row", "alignItems": "center"}),
                dbc.Button([
                    html.Img(src="assets/level.svg", style={"marginLeft": "30px", "width": "30px", "height": "30px"}),
                    html.P("Set Levels", style={"marginLeft": "40px", "fontSize": "20px", "marginTop": "15px"})
                ], id="level", className="btn", style ={"display":"flex", "flexDirection": "row", "alignItems": "center"})
            ], 
            className="tab"
            ),
        ], style={"width":"40%"}),

        # Variable section
        dbc.Col([
            html.Div([
                dbc.Label("Select Variable:", style={"fontSize": "20px", "fontWeight": "bold"}),
                dcc.Dropdown(
                    id='variable-dropdown',
                    options=[
                        {'label': 'Variable 1', 'value': 'var1'},
                        {'label': 'Variable 2', 'value': 'var2'},
                        {'label': 'Variable 3', 'value': 'var3'}
                    ],
                    value='var1',
                    style={"width": "100%"}
                ),
            ], style={"margin": "10px 0"})
        ]),

        # Alert section
        dbc.Col([
            html.Div([
                dbc.Alert("This is an alert message!", color="primary", style={"margin": "10px 0"}),
                dbc.Alert("This is another alert message!", color="secondary", style={"margin": "10px 0"}),
            ], style={"width": "100%", "padding": "20px"})
        ]),
    ], style ={"display":"flex", "flexDirection": "row", "alignItems": "center", "gap": "20px"}),
],style={"margin": "0 auto", "maxWidth": "1200px", "padding": "50px"})


if __name__ == '__main__':
    app.run(debug=True, port=3000)