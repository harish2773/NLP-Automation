# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template

# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__, template_folder='templates', static_folder='static')

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
	return render_template('index.html')

@app.route('/result')
# ‘/’ URL is bound with hello_world() function.
def result():
	return render_template('result.html')


@app.route('/customnn')
# ‘/’ URL is bound with hello_world() function.
def customnn():
	return render_template('customnn.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['input-box']
    return text



# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
