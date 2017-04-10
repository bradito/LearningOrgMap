#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    LearningOrgMap
    ~~~~~~~~~~~

    :copyright: Bradley Gordon, MD
    :license: TBD
"""

from flask import Flask, render_template, request, send_from_directory, send_file
import datetime, csv
import sys


app = Flask(__name__,static_url_path='',instance_relative_config=True)
app.config.from_object('LearningOrgMap.config.DevelopmentConfig')
app.config.from_pyfile('LearningOrgMap.cfg', silent=True)
local_map = None

try:
	local_map = app.open_instance_resource('map.json')
except:
	local_map = None
	pass

@app.route("/oldway")
def hello():
	now = datetime.datetime.now()
	timestring = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'title':'Learning Organization Map',
		'map':'defaultmap.json'
		}
	if 'TITLE_PREFIX' in app.config:
		templateData['title'] = '{}: {}'.format(app.config['TITLE_PREFIX'], templateData['title'])
	if local_map:
		templateData['map'] = 'local_map.json'
	
	return render_template('main.html', **templateData)

@app.route("/")
def collapsing():
	templateData = {
		'title':'Learning Organization Map, collapsing',
		'map':'defaultmap.json'
		}
	if local_map:
		templateData['map'] = 'local_map.json'

	return render_template('collapse.html', **templateData)


@app.route('/data/<path:path>')
def send_data(path):
	if path == 'local_map.json':
		return send_file(local_map, mimetype='application/json')
	else:
	    return send_from_directory('data', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

if __name__ == "__main__":
	app.run()