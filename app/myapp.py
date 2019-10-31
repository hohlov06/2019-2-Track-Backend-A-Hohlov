import datetime

def handler(environ, start_response):
	data = str(environ) + '\n\n'
	data = data + '<b>QWEewq<\\b>\n\t\sRandom  Symbols\n\n' + str(datetime.datetime.now()) + '\n\n'
	data = '<!DOCTYPE html>\n<html><div>' + data + '<\\div><\\html>'
	headers = [('Content-Type', 'text/html'),
			   ('content-Length', str(len(data)))]
	
	start_response('200 OK', headers)
	return [bytes(data, 'utf-8')]