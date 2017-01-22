# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SelectField, SubmitField
#from wtforms.validators import Required, Length
import random, json
import plotly.plotly
import plotly.graph_objs as go
#import pandas as pd


import plotly.tools as tls
tls.set_credentials_file(username='nmamadeo', api_key='9eLPzUvSLGlWKczFs2ig')

app = Flask(__name__)
app._static_folder = '/template/static'
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

countsDct = {'Alabama': [84.3,23.5,11.8,11.9,18.5],
'Alaska': [92.1,28,8.1,16.4,10.3],
'Arizona': [86,27.5,8.2,12.8,17.4],
'Arkansas': [84.8,21.1,12.3,11.1,19.1],
'California': [81.8,31.4,6.8,9.7,15.3],
'Colorado': [90.7,38.1,7.2,9.2,11.5],
'Connecticut': [89.9,37.6,7.1,6.9,10.5],
'Delaware': [88.4,30,8.5,6.8,12.4],
'Florida': [86.9,27.3,8.5,16.2,15.7],
'Georgia': [85.4,28.8,8.8,15.7,17],
'Hawaii': [91,30.8,6.5,4.7,10.6],
'Idaho': [89.5,25.9,9,12.9,15.1],
'Illinois': [87.9,32.3,7.1,8.1,13.6],
'Indiana': [87.8,24.1,9.7,11.2,14.5],
'Iowa': [91.5,26.7,7.9,5.9,12.2],
'Kansas': [90.2,31,8.6,10.6,13],
'Kentucky': [84.2,22.3,12.9,7,18.5],
'Louisiana': [83.4,22.5,11,13.8,19.6],
'Maine': [91.6,29,11.9,10.3,13.4],
'Maryland': [89.4,37.9,7.1,7.5,9.7],
'Massachusetts': [89.8,40.5,7.9,3.3,11.5],
'Michigan': [89.6,26.9,10.3,7.1,15.8],
'Minnesota': [92.4,33.7,7.1,5.2,10.2],
'Mississippi': [82.3,20.7,11.9,14.8,22],
'Missouri': [88.4,27.1,10.4,11.4,14.8],
'Montana': [92.8,29.5,9.1,14,14.6],
'Nebraska': [90.7,29.3,7.3,9.5,12.6],
'Nevada': [85.1,23,9,14,14.7],
'New Hampshire': [92.3,34.9,8.5,7.5,8.2],
'New Jersey': [88.6,36.8,6.6,10,10.8],
'New Mexico': [84.2,26.3,10.1,12.8,20.4],
'New York': [85.6,34.2,7.4,8.1,15.4],
'North Carolina': [85.8,28.4,9.6,13.1,16.4],
'North Dakota': [91.7,27.7,6.8,8.9,11],
'Ohio': [89.1,26.1,9.9,7.6,14.8],
'Oklahoma': [86.9,24.1,11.3,16.2,16.1],
'Oregon': [89.8,30.8,10.2,8.3,15.4],
'Pennsylvania': [89.2,28.6,9.5,7.5,13.2],
'Rhode Island': [86.2,31.9,8.9,6.7,13.9],
'South Carolina': [85.6,25.8,10.3,12.9,16.6],
'South Dakota': [90.9,27,8.4,12,13.7],
'Tennessee': [85.5,24.9,11.2,12,16.7],
'Texas': [81.9,27.6,8.1,19.1,15.9],
'Utah': [91.2,31.1,6.6,11.5,11.3],
'Vermont': [91.8,36,10,4.6,10.2],
'Virginia': [88.3,36.3,7.7,10.5,11.2],
'Washington': [90.4,32.9,8.9,7.6,12.2],
'West Virginia': [85,19.2,14.4,7.2,17.9],
'Wyoming': [92.3,25.7,8.5,13.4,11.1],
'Wisconsin': [91,27.8,8.2,6.6,12.1]}

wage = {'Alabama': [	69.4,	76.2,	58.0,	55.8,	0,	0],
'Alaska': [	69.4,	73.9,	56.0,	0,	54.3,	55.5],
'Arizona': [	72.1,	80.5,	52.4,	68.3,	50.0,	0],
'Arkansas': [	71.1,	74.4,	61.8,	62.1,	46.2,	0],
'California': [	62.2,	74.8,	53.2,	64.0,	41.9,	69.8],
'Colorado': [	69.3,	74.1,	53.8,	59.5,	48.1,	66.3],
'Connecticut': [	70.0,	73.8,	53.4,	60.8,	44.4,	66.8],
'Delaware': [	72.5,	76.9,	62.3,	66.5,	49.9,	66.6],
'Florida': [	66.7,	73.0,	56.5,	58.3,	52.1,	68.9],
'Georgia': [	68.7,	75.5,	62.2,	62.4,	41.6,	72.8],
'Hawaii': [	63.9,	79.0,	61.6,	0,	57.8,	61.6],
'Idaho': [	70.2,	72.7,	56.3,	29.5,	49.9,	0],
'Illinois': [	69.3,	72.7,	63.3,	63.4,	51.4,	85.5],
'Indiana': [	71.4,	71.4,	63.0,	66.9,	45.7,	0],
'Iowa': [	76.2,	76.4,	57.6,	0,	55.2,	0],
'Kansas': [	75.0,	76.2,	65.6,	62.3,	65.0,	0],
'Kentucky': [	75.0,	75.3,	65.0,	69.3,	0,	0],
'Louisiana': [	63.0,	70.2,	51.4,	51.4,	0,	0],
'Maine': [	75.8,	76.5,	65.0,	0,	0,	0],
'Maryland': [	69.5,	75.6,	63.3,	64.5,	45.9,	68.0],
'Massachusetts': [	66.7,	71.1,	50.0,	56.2,	41.7,	64.5],
'Michigan': [	70.0,	70.0,	70.0,	69.2,	57.8,	76.4],
'Minnesota': [	74.7,	76.7,	60.2,	65.6,	48.0,	68.3],
'Mississippi': [	64.5,	74.4,	51.2,	51.2,	0,	0],
'Missouri': [	72.0,	73.1,	66.3,	0,	61.0,	0],
'Montana': [	69.1,	70.3,	52.6,	42.1,	0,	0],
'Nebraska': [	74.8,	76.4,	59.6,	67.3,	54.8,	0],
'Nevada': [	67.3,	76.2,	55.1,	60.7,	49.0,	71.4],
'New Hampshire': [	74.0,	74.2,	70.8,	0,	0,	0],
'New Jersey': [	66.4,	75.9,	52.0,	53.2,	41.7,	79.2],
'New Mexico': [	60.4,	69.5,	53.0,	0,	54.3,	0],
'New York': [	70.4,	80.0,	60.0,	64.0,	53.3,	66.0],
'North Carolina': [	73.4,	76.9,	62.7,	65.3,	46.6,	62.2],
'North Dakota': [	70,	70,	65,	0,	0,	0],
'Ohio': [	74.5,	75.8,	67.7,	67.7,	59.2,	0],
'Oklahoma': [	74.9,	77.4,	64.9,	75.0,	49.9,	0],
'Oregon': [	65.6,	68.4,	53.2,	0,	47.2,	66.7],
'Pennsylvania': [	71.7,	73.9,	64.9,	64.9,	60.5,	87.7],
'Rhode Island': [	71.1,	75.0,	51.2,	57.7,	41.0,	55.8],
'South Carolina': [	68.6,	71.5,	62.8,	62.0,	57.1,	0],
'South Dakota': [	76,	76,	67,	0,	0,	0],
'Tennessee': [	74.7,	74.7,	63.3,	67.8,	44.8,	0],
'Texas': [	63.9,	75.8,	51.2,	59.9,	46.7,	68.2],
'Utah': [	61.3,	65.2,	48.9,	0,	44.4,	56.2],
'Vermont': [	81.1,	81.2,	75.4,	0,	0,	0],
'Virginia': [	66.7,	75.0,	56.3,	56.2,	50.6,	63],
'Washington': [	68.9,	72.3,	57.7,	0,	55.7,	56.3],
'West Virginia': [	76.3,	76.3,	82.1,	0,	0,	0],
'Wyoming': [	71.7,	74.3,	58.7,	60.8,	58.5,	0],
'Wisconsin': [	57.1,	57.3,	54.1,	0,	53.1,	0]}

def make_bar_chart(choice, state):
    trace1 = go.Bar(
        x=['% over age 25 with HS diploma', '% with Bachelor\'s or higher', '% under 65 with a disability', '% without health insurance', '% in poverty'],
        y=countsDct[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['% over age 25 with HS diploma', '% with Bachelor\'s or higher', '% under 65 with a disability', '% without health insurance', '% in poverty'],
        y=countsDct[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group') )]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

def make_bar_wage_chart(choice, state):
    
    graphs = [
            dict(
                data = [
                        dict(
                            x=['All Women', 'White Women', 'All Minority Women', 'Black Women', 'Hispanic Women', 'Asian/NHPI Women'],
                            y=wage[choice],
                            mode='markers',
                            name=choice,
                            marker=dict(
                            color='rgba(156, 165, 196, 0.95)',
                            line=dict(
                            color='rgba(156, 165, 196, 1.0)',
                            width=1,
                            ),
                            symbol='circle',
                            size=16,
                            )
                           ,),
                           dict(
                            x=['All Women', 'White Women', 'All Minority Women', 'Black Women', 'Hispanic Women', 'Asian/NHPI Women'],
                                                y=wage[state],
                                                mode='markers',
                                                name=state,
                                                marker=dict(
                                                    color='rgba(204, 204, 204, 0.95)',
                                                    line=dict(
                                                        color='rgba(217, 217, 217, 1.0)',
                                                        width=1,
                                                    ),
                                                    symbol='circle',
                                                    size=16,
                                                    )
                                                ),
                        
                        ],
                layout =
                    go.Layout(
                        title="Women's Wage Gap",
                        titlefont=dict(
                                color='rgb(000, 000, 000)',
                                size = 15,
                            ),
                        xaxis=dict(
                            showgrid=False,
                            showline=True,
                            linecolor='rgb(102, 102, 102)',
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            tickfont=dict(
                                color='rgb(102, 102, 102)',
                            ),
                            autotick=False,
                            dtick=10,
                            ticks='outside',
                            tickcolor='rgb(102, 102, 102)',
                        ),
                        margin=dict(
                            l=50,
                            r=40,
                            b=50,
                            t=80
                        ),
                        yaxis = dict(
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            title='Cents on A Dollar Earned by White Men',
                        ),
                        legend=dict(
                            font=dict(
                                size=10,
                            ),
                            yanchor='middle',
                            xanchor='right',
                        ),
                        width=500,
                        height=400,
                        plot_bgcolor='rgb(255,255,240)',
                        hovermode='closest',
                        )
                )
        ]
    
    graphLine = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphLine)
    return graphLine

class ChoiceForm(Form):
    
    choice = SelectField(u'Your state', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho','Idaho'),
('Illinois','Illinois'),
('Indiana','Indiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('Montana','Montana'),
('Nebraska','Nebraska'),
('Nevada','Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('Pennsylvania','Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('West Virginia','West Virginia'),
('Wyoming','Wyoming'),
('Wisconsin','Wisconsin')])
    
    state = SelectField(u'States', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho','Idaho'),
('Illinois','Illinois'),
('Indiana','Indiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('Montana','Montana'),
('Nebraska','Nebraska'),
('Nevada','Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('Pennsylvania','Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('West Virginia','West Virginia'),
('Wyoming','Wyoming'),
('Wisconsin','Wisconsin')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    
    choice = None
    state = None
    ids = []
    id2 = []
    graphJSON = []
    graphJSON2 = []
#    graphLine = []
    #ruhlman_data = pd.read_excel('test.xlsx')
    form = ChoiceForm()
    if form.validate_on_submit():
        choice = form.choice.data
        state = form.state.data
        if choice != "blank":
            graphJSON = make_bar_wage_chart(choice, state)
            graphJSON2 = make_bar_chart(choice, state)
        #    graphLine = make_line_chart(choice, state)
            ids = ["Bar Chart for x"]
            id2 = ["Scatter Plot for y"]
        form.choice.data = ''
    return render_template('match.html', form=form, choice=choice, state = state,
                           graphJSON=graphJSON, graphJSON2 = graphJSON2,
                           ids=ids, id2 = id2)

if __name__ == '__main__':
    app.run(debug=True, port = 7000)
    #app.run(host='0.0.0.0', port = 1561, debug=True)
