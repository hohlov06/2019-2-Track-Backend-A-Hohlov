#!/usr/bin/env python3

import codecs

filename = '/home/lupa/technotrack/backend/2019-2-Track-Backend-A-Hohlov/app/pupa.html'

    # Read a file and encode it into base64 format
fo =  codecs.open(filename, "r", 'utf-8')
filecontent = fo.read()

def handler(environ, start_response):
	data = filecontent
	headers = [('Content-Type', 'text/html'),
			   ('content-Length', str(len(data)))]
	
	start_response('200 OK', headers)
	return [bytes(data, 'utf-8')]