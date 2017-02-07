# -*- coding: UTF-8 -*-
from flask import render_template
from app import app
from functions import *

profile = 'bp-core'
region = 'sa-east-1'

@app.route('/')
def home():
    allInstances = listInstances(profile, region)
    return render_template('index.html', instances=allInstances)

@app.route('/poweron/<instanceid>')
def poweron(instanceid):
    return render_template('poweron.html', instance=instanceid)

@app.route('/poweroff/<instanceid>')
def poweroff(instanceid):
    return render_template('poweroff.html', instance=instanceid)
