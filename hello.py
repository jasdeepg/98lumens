from flask import Flask
from flask import render_template
import Panel
import State
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

app = Flask(__name__)
panel1 = Panel.panel_production('Jim', 2, 2, 4)
CA = State.stateReg('California',15,5)

#initialize sample vars
panel1.setOCV(1)
panel1.setSCI(1)

def hey():
    return 'hey'

def makeChart():
    # Set the vertical range from 0 to 100
    max_y = 100
    
    # Chart size of 200x125 pixels and specifying the range for the Y axis
    chart = SimpleLineChart(400, 250, y_range=[0, max_y])
    
    # Add the chart data
    data = [
        32, 34, 34, 32, 34, 34, 32, 32, 32, 34, 34, 32, 29, 29, 34, 34, 34, 37,
        37, 39, 42, 47, 50, 54, 57, 60, 60, 60, 60, 60, 60, 60, 62, 62, 60, 55,
        55, 52, 47, 44, 44, 40, 40, 37, 34, 34, 32, 32, 32, 31, 32
    ]
    chart.add_data(data)
    
    # Set the line colour to blue
    chart.set_colours(['0000FF'])
    
    # Set the vertical stripes
    chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)
    
    # Set the horizontal dotted lines
    chart.set_grid(0, 25, 5, 5)
    
    # The Y axis labels contains 0 to 100 skipping every 25, but remove the
    # first number because it's obvious and gets in the way of the first X
    # label.
    left_axis = range(0, max_y + 1, 25)
    left_axis[0] = ''
    chart.set_axis_labels(Axis.LEFT, left_axis)
    
    # X axis labels
    chart.set_axis_labels(Axis.BOTTOM, \
        ['9 am', '6 pm', '12 am'])
        
    return chart

@app.route('/hello/')
#@app.route('/hello/<name>')
def hello_world(name='test'):
    panel_OCV = panel1.getOCV()
    panel_SCI = panel1.getSCI()
    panelWatt = panel_OCV*panel_SCI
    elecSell = CA.geteCost()
    tonsCoal = 15
    chart = makeChart()
    display = chart.get_url()
    return render_template('template.html', name=name, power=panelWatt,
                           sellAt=elecSell, tonsCoal = tonsCoal, chart = display)

if __name__ == '__main__':
    app.run(debug=True, port=31268)