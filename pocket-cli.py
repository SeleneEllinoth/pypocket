#!/usr/bin/python

import json,ConfigParser,urllib2,os

#read the ~/.cred
if not os.path.exists(os.path.expanduser('~/.config')):
    os.makedirs(os.path.expanduser('~/.config'))
if not os.path.exists(os.path.expanduser('~/.config/pypocket')):
    os.makedirs(os.path.expanduser('~/.config/pypocket'))
creds = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.config/pypocket/creds')])


#if .cred does not exist or --authentify is used, call the authentication method
#create a handle for add operations
#create a handle for get operations
#create a handle for modify operations
#create a handle for batch modify operations
