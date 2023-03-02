from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
from datetime import date
import random

app = Dash(__name__)
names = ["Johan", "Jakob", "Katrine", "Malte","Maxime","Adam","Oliver","Baldur","Isabella","Emilia"]
count = [0,0,0,0,0,0,0,0,0,0,0]
lengths = [0,1,2,3,4,5,6,7,8,9,10]
nameLength = [len(names[0]),len(names[1]),len(names[2]),len(names[3])]

def nameCounter(names):
    for i in names:
        count[len(i)] += 1
    return count

def genLists():
    lst1 = []
    lst2 = []
    for i in range(1000):
        lst1.append(random.randint(0,10000))
        lst2.append(random.randint(0,10000))
        

    return lst1, lst2

lst1, lst2 = genLists()

ScatterPlotFig = px.scatter(x=lst1,y=lst2,title="Scatter plot of name lengths").update_layout(xaxis_title="Name length",yaxis_title="Name count")
PieChartFig = px.pie(values=[5,7,10], names=["Hej", "Hej2", "Hej3"], title="Piechart for data :)")

app.layout = html.Div(children=[
    html.Div(
        html.H1("Log anomaly dashboard"),
        id="TitleDIV"
    ),
    html.Div(
        html.P("Homepage / page / page")
    ),
    html.Div(children=[
        dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25),
        ),
        html.Div(id='output-container-date-picker-range',style={})
    ]),
    html.Div(children=[
        html.Div(children=[
            html.H3("Anomalies", style={"margin-left": "20px"}),
            html.H1(len(lst1), style={"margin-left": "20px"}),
            html.H2("00%", style={"margin-left": "20px"})],
            style={"margin":"60px","background-color":"#fff7e6","height":"200px","width":"300px","outline-color" :"#ffe7b3","outline-style" : "solid","border-radius":"25px"}
        ),
        html.Div(children=[
            html.H3("Logs", style={"margin-left": "20px"}),
            html.H1("0", style={"margin-left": "20px"}),
            html.H2("00%", style={"margin-left": "20px"})],
            style={"margin":"60px","background-color":"#fff7e6","height":"200px","width":"300px","outline-color" :"#ffe7b3","outline-style" : "solid","border-radius":"25px"}
        ),
        html.Div(children=[
            html.H3("False positives", style={"margin-left": "20px"}),
            html.H1("0", style={"margin-left": "20px"}),
            html.H2("00%", style={"margin-left": "20px"})],
            style={"margin":"60px","background-color":"#fff7e6","height":"200px","width":"300px","outline-color" :"#ffe7b3","outline-style" : "solid","border-radius":"25px"}
        ),
    ],style={"display": "flex","justify-content":"center"},className="row"),
    html.Div(
        html.Div(children=[
            dcc.Graph(
                figure=ScatterPlotFig,
                style={"width":"60vw"}
            ),
            dcc.Graph(
                figure=PieChartFig,
                style={"width":"30vw"}
            ),
        ],style={"display": "flex","justify-content":"center"},className="row"),
    )
])


@app.callback(
    Output('output-container-date-picker-range', 'children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix



if __name__ == "__main__":
    app.run(debug=True)