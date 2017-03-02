#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    LearningOrgMap
    ~~~~~~~~~~~

    :copyright: Bradley Gordon, MD
    :license: TBD
"""

from flask import Flask, render_template, request, send_from_directory
import datetime, csv
import sys

try: 
	import serverconfig
except: 
	sys.exit(
"""		

Missing Config!
You need to copy serverconfig_EXAMPLE.py to become serverconfig.py to run program with proper configuration
				
""")

app = Flask(__name__,static_url_path='')

@app.route("/")
def hello():
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'title':'Learning Organization Map',
		}
	
	return render_template('main.html', **templateData)

@app.route("/collapse")
def collapsing():
	templateData = {
		'title':'Learning Organization Map, collapsing',
		}
	return render_template('collapse.html', **templateData)


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
	app.run(host='0.0.0.0', port=serverconfig.server_port, debug=serverconfig.server_debug)