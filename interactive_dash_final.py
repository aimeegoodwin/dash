# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:13:18 2021

@author: bozen
"""

import pandas as pd     #(version 1.0.0)
#import plotly           #(version 4.5.4) pip install plotly==4.5.4
import plotly.express as px

import dash             #(version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

 
df1 = pd.read_csv('education_ED.csv')

df2 = pd.read_csv('economic_status_ED.csv')

df3 = pd.read_csv('social_class_ED.csv')


df = df1.merge(df2).merge(df3)
#merge.set_index('ED_NAME', inplace = True)



df = df.groupby(['COUNTY']).mean()
df.reset_index(inplace=True)

dff=df
#education = dff[['Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2006', 'Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2011']]
#---------------------------------------------------------------
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Unemployment factors ']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ceased education after primary', 'value': 'A'},
                     {'label': 'Unskilled Population', 'value': 'B'},
                     {'label': 'Unemployed', 'value': 'C'}, 
                     {'label': 'Comparision', 'value': 'D'} 
            ],
            value='A',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])


def customLegend(chart, nameSwap):
    for i, dat in enumerate(chart.data):
        for elem in dat:
            if elem == 'name':
                chart.data[i].name = nameSwap[chart.data[i].name]
    return (chart)

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)


#function how executed
def update_graph(my_dropdown):
   # dff = df
  if my_dropdown == 'A':
    
    chart= px.bar(dff, 
                  x="COUNTY", 
                  y=["Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2006", "Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2011"], 
                  barmode="group")
    
    
    chart.update_layout(clickmode='event+select')
    
    
    chart = customLegend(chart=chart, nameSwap = {'Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2006': '2006', 'Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2011':'2011'})

    chart.update_layout(
       title="No secondary education",
       xaxis_title="Irish Constituencies",
       yaxis_title="Percentage ",
       legend_title="Census Year",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
          
        
    )
)
    
    chart.show()

    app.layout = html.Div([
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ceased education after primary', 'value': 'A'},
                     {'label': 'Unskilled Population', 'value': 'B'},
                     {'label': 'Unemployed', 'value': 'C'}, 
                     {'label': 'Comparision', 'value': 'D'} 
            ],
            value='A',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
        dcc.Graph(
            id='the_graph',
            figure = chart
        ),
    
        html.Div(className='row', children=[
            html.Div([
                dcc.Markdown(),
                html.Pre(id='hover-data')
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='click-data'),
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='selected-data'),
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='relayout-data'),
            ], className='three columns')
        ])
    ])





  elif my_dropdown == 'B':
         
     chart= px.bar(dff, 
                  x="COUNTY", 
                  y=["Perc_Pop_By_Social_Class_Unskilled_2006", "Perc_Pop_By_Social_Class_Unskilled_2011"],
                  barmode="group")
     
     chart.update_layout(clickmode='event+select')
     
     chart = customLegend(chart=chart, nameSwap = {'Perc_Pop_By_Social_Class_Unskilled_2006': '2006', 'Perc_Pop_By_Social_Class_Unskilled_2011':'2011'})

     chart.update_layout(
       title="Percentage population unskilled",
       xaxis_title="Irish Constituencies",
       yaxis_title="Percentage ",
       legend_title="Census Year",
       font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
     
     
     chart.show()

     app.layout = html.Div([
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ceased education after primary', 'value': 'A'},
                     {'label': 'Unskilled Population', 'value': 'B'},
                     {'label': 'Unemployed', 'value': 'C'}, 
                     {'label': 'Comparision', 'value': 'D'} 
            ],
            value='A',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
        dcc.Graph(
            id='the_graph',
            figure = chart
        ),
    
        html.Div(className='row', children=[
            html.Div([
                dcc.Markdown(),
                html.Pre(id='hover-data')
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='click-data'),
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='selected-data'),
            ], className='three columns'),
    
            html.Div([
                dcc.Markdown(),
                html.Pre(id='relayout-data'),
            ], className='three columns')
        ])
    ])

     
     
  elif my_dropdown == 'C':
         
         chart= px.bar(dff, 
                      x="COUNTY", 
                      y=["Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2006", "Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2011"], 
                      barmode="group")
         
         chart.update_layout(clickmode='event+select')
         
         chart = customLegend(chart=chart, nameSwap = {'Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2006': '2006', 'Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2011':'2011'})
    
         chart.update_layout(
           title="Percentage population unemployed",
           xaxis_title="Irish Constituencies",
           yaxis_title="Percentage ",
           legend_title="Census Year",
           font=dict(
            family="Courier New, monospace",
            size=18,
            color="Black"
        )
)
         
         
         chart.show()

         app.layout = html.Div([
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ceased education after primary', 'value': 'A'},
                     {'label': 'Unskilled Population', 'value': 'B'},
                     {'label': 'Unemployed', 'value': 'C'}, 
                     {'label': 'Comparision', 'value': 'D'} 
            ],
            value='A',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
            dcc.Graph(
                id='the_graph',
                figure = chart
            ),
        
            html.Div(className='row', children=[
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='hover-data')
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='click-data'),
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='selected-data'),
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='relayout-data'),
                ], className='three columns')
            ])
        ])

         
         
  else:
         
         chart= px.bar(dff, 
                      x="COUNTY", 
                      y=[ "Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2011","Perc_Pop_By_Social_Class_Unskilled_2011", "Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2011"], 
                      barmode="group")
         
         chart.update_layout(clickmode='event+select')
         
         chart = customLegend(chart=chart, nameSwap = {'Perc_Persons_15_Plus_By_Highest_Level_Of_Edu_Primary_2011': 'No secondary education' ,'Perc_Pop_By_Social_Class_Unskilled_2011': 'Unskilled', 'Perc_Persons_Aged_15_And_Over_By_Principal_Economic_Status_Unemployed_2011':'Unemployed'})
    
         chart.update_layout(
           title="Unemployment compared with level of education and skillset",
           xaxis_title="Irish Constituencies",
           yaxis_title="Percentage ",
           font=dict(
            family="Courier New, monospace",
            size=18,
            color="Black"
        )
)
         
         
         chart.show()

         app.layout = html.Div([
            dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Ceased education after primary', 'value': 'A'},
                     {'label': 'Unskilled Population', 'value': 'B'},
                     {'label': 'Unemployed', 'value': 'C'}, 
                     {'label': 'Comparision', 'value': 'D'} 
            ],
            value='A',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
            dcc.Graph(
                id='the_graph',
                figure = chart
            ),
        
            html.Div(className='row', children=[
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='hover-data')
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='click-data'),
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='selected-data'),
                ], className='three columns'),
        
                html.Div([
                    dcc.Markdown(),
                    html.Pre(id='relayout-data'),
                ], className='three columns')
            ])
        ])
         



  return (chart)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
