# Web Library Imports 
from flask import Flask, request, url_for

# My Helper Function Import
from helper_module import getLargestNumberStatic

# Create A Web App
app = Flask(__name__)

#Define Route and Route Handling Method
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return 'Please use GET route'
    else:
        return '''
        <form action="/calculate" method="POST">
            <h3>How many numbers do you want to compare:</h3>
            <input type="text" name="theData" />
            <br />
            <br />
            <input type="submit" value="Submit" />
        </form>'''

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        data = int(request.form['theData'])

        the_new_form = '<h3>Comparing {} Numbers</h3>'.format(data)

        the_new_form = the_new_form + '<form action="/output" method="POST">'

        for i in range(data):
            the_new_form = the_new_form + '<p>Number {}</p><input type="number" name="number_{}" /><br />'.format(i,i)

        the_new_form = the_new_form + '<br /><input type="submit" value="Submit" />'

        the_new_form = the_new_form + '</form>'

        return the_new_form
    else:
        return 'Please Use POST Route'

@app.route('/output', methods=['GET', 'POST'])
def output():
    data_cache = []

    for i in request.form:
        data_cache.append(int(request.form[i]))

    theGreatestNumber = max(data_cache)

    the_output = '<h3>The Greatest Number Is {}</h3>'.format(theGreatestNumber)

    return the_output

# Execution Starts Here - ENTRY POINT
if __name__ == '__main__':
    app.run()