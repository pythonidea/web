def wsgi_application (environ, start_responce):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  body = '\n'.join(environ['QUERY_STRING'].split('&'))
  start_response (status, headers)
  return [ body ]
