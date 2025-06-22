from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system/modeling')
def modeling():
    return render_template('modeling system.html')

@app.route('/system/analysis')
def analysis():
    return render_template('system analysis.html')

@app.route('/control/pid')
def pid():
    return render_template('PID.html')

@app.route('/control/state-space')
def statespace():
    return render_template('State Space.html')

@app.route('/simulink/modeling')
def Smodeling():
    return render_template('Simulink Modeling.html')

@app.route('/simulink/control')
def control():
    return render_template('control.html')

@app.route('/simulink/simscape')
def simscape():
    return render_template('simscape.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)
