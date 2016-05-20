import urlparse
def wsgi_application (environ, start_responce):
  status = '200 OK'
  headers = [
    ('Content-Type', 'text/plain')
  ]
  body = ''
  params = urlparse_qs(environ["QUERY_STRING"]
  start_response (status, headers)
  for i in params:
    body += i[0] + '='+i[1] + '\n'
  return [ body ]
