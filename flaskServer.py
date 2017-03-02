# d3Server.py
from flask import Flask, render_template, request, send_from_directory
import datetime, csv
app = Flask(__name__,static_url_path='')

# create library object


@app.route("/")
def hello():
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'title':'HELLO!',
		'time' : timestring
		}
	
	return render_template('main.html', **templateData)


@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)