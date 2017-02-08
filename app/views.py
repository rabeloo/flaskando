# -*- coding: UTF-8 -*-
from flask import render_template
from app import app
from functions import *
import ConfigParser

C = ConfigParser.RawConfigParser()
C.read('config.cfg')
profile = C.get('aws', 'profile')
region = C.get('aws', 'region')

@app.route('/')
def home():
    all_accounts = list_accounts()
    all_instances = list_instances(profile, region)
    return render_template('index.html', instances=all_instances, accounts=all_accounts)

@app.route('/poweron/<instanceid>')
def poweron(instanceid):
    return render_template('poweron.html', instance=instanceid)

@app.route('/poweroff/<instanceid>')
def poweroff(instanceid):
    return render_template('poweroff.html', instance=instanceid)
