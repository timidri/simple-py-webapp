from templite import Templite

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = get_text()
    return [txt]

def get_text():
    tmp = """
This is a template --- ${ write("pang") }$ -- That was a template
"""
    t = Templite(tmp)
    rtn = t.render()
    return rtn

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    txt = get_text()
    return [txt]


print get_text()
    
